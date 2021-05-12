import frappe
import requests
from frappe import _
import requests
import urllib
import json

# api/method/expensify_integration.expensify_integration.expensify_integration.handle_sample_expense

# LOGIC TO INTERACT WITH FRAPPE

def get_employee(full_name):
    employee_doc = frappe.get_doc(doctype="Employee", employee_name = full_name)
    return employee_doc.name

def get_payable_account(expense_type):
    return frappe.db.get_single_value("Expensify Settings", "payable_account") 

def get_expense_approver():
    return frappe.db.get_single_value("Expensify Settings", "expense_approver")

# Helper method to extract individual expenses
def get_expense_list(report):
    expenses = []
    for report_expense_detail in report["expenses"]:
        expense = {
            "description":report_expense_detail["description"],
            "expense_date":report_expense_detail["expense_date"],
            "expense_type":report_expense_detail["expense_type"],
            "amount":int(report_expense_detail["amount"]) / 100.0,  #Amount from expensify in cents
            "sanctioned_amount":int(report_expense_detail["amount"]) / 100.0  #Amount from expensify in cents
        } 
        expenses.append(expense)
    return expenses

@frappe.whitelist(allow_guest=True)
def handle_sample_expense(**kwargs):

    # RETRIEVE API KEYS

    APIKEY = frappe.db.get_single_value("Expensify Settings", "apikey")
    SECRET = frappe.db.get_single_value("Expensify Settings", "secret")


    # DECLARE VARIABLES      

    template_string = """
    [<#lt>
    <#list reports as report>
        {<#lt>
            "title":"${report.reportName}",<#lt>
            "employee_name":"${report.submitter.fullName}",<#lt>
            "expense_approver":"${report.managerEmail}",<#lt>
            "posting_date":"${report.submitted}",<#lt>
            "expenses":[<#lt>
            <#list report.transactionList as expense>
                {<#lt>
                    "amount":"${expense.amount}",<#lt>
                    "expense_type":"${expense.category}",<#lt>
                    "description":"${expense.comment}",<#lt>
                    "expense_date":"${expense.created}"<#lt>
                }<#sep>,</#sep><#lt>
            </#list>]<#lt>
        }<#sep>,</#sep><#lt>
    </#list>]
    """

    url = 'https://integrations.expensify.com/Integration-Server/ExpensifyIntegrations'

    # Generate your credentials here: https:#www.expensify.com/tools/integrations/
    credentials = { 
        "partnerUserID":APIKEY, 
        "partnerUserSecret":SECRET 
    }

    jobDescriptionExport = { 
        "type":"file", 
        "credentials": credentials, 
        "onReceive":{ "immediateResponse":["returnRandomFileName"] }, 
        "limit":"3",
        "inputSettings":{ 
            "type":"combinedReportData", 
            "filters":{
                "startDate":"2019-01-01",
                "markedAsExported":"Exported4"
            }
        }, 
        "outputSettings":{ "fileExtension":"json" },
        "onFinish":[
            {"actionName":"markAsExported","label":"Exported3"}
          # {"actionName":"email","recipients":"manager@domain.com,finances@domain.com", "message":"Report is ready."}
        ]
    }

    jobDescriptionDownload = {
        "type":"download",
        "credentials": credentials,
        "fileName":"_INSERT_FILE_NAME_",
        "fileSystem":"integrationServer"
    }

    data = {
        'requestJobDescription': str(jobDescriptionExport), 
        'template' : template_string
    }

    # SEND REQUEST TO EXPENSIFY 

    response = requests.post(url, data=data)

    if response.status_code == 200:
        report_file_name = response.text

        jobDescriptionDownload["fileName"] = report_file_name
        data = {
            'requestJobDescription': str(jobDescriptionDownload)
        }
        response = requests.post(url, data=data)
        reports = json.loads(response.text)

        # EXTRACT, TRANSFORM, LOAD

        print("REPORTS:")
        for report in reports:
            print(json.dumps(report))
            print()
            
            expense_list = get_expense_list(report)

            claim = frappe.get_doc({
                "doctype":"Expense Claim",
                "title":report["title"],
                "expense_approver":get_expense_approver(),
                "employee":get_employee(report["employee_name"]),
                "payable_account":get_payable_account(""),
                "expenses":expense_list
            })
            #claim.flags.ignore_mandatory = True
            claim.save()
            frappe.db.commit()

            