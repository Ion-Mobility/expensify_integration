import frappe
import requests
from frappe import _
import urllib
import json

# api/method/expensify_integration.expensify_integration.expensify_integration.handle_sample_expense

# LOGIC TO INTERACT WITH FRAPPE
def get_employee(full_name):
    employee_doc = frappe.get_doc(doctype="Employee", employee_name = full_name)
    employee_id_list = frappe.db.get_list('Employee', 
        filters = {
            "employee_name":full_name
        }
    )
    print("Retrieving Employee with name")
    print(full_name)
    print("Employee list")
    print(employee_id_list)
    employee_id = employee_id_list[0] if employee_id_list else ""
    return employee_id["name"]

def get_payable_account():
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

# MOST IMPORTANT METHOD
def handle_expenses(**kwargs):

    # RETRIEVE API KEYS
    credentials = { 
        "partnerUserID":frappe.db.get_single_value("Expensify Settings", "apikey"), 
        "partnerUserSecret":frappe.db.get_single_value("Expensify Settings", "secret") 
    }

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

    jobDescriptionExport = { 
        "type":"file", 
        "credentials": credentials, 
        "onReceive":{ "immediateResponse":["returnRandomFileName"] }, 
        "limit":"3",
        "inputSettings":{ 
            "type":"combinedReportData", 
            "filters":{
                "startDate":"2019-01-01",
                "markedAsExported":"Exported8"
            }
        }, 
        "outputSettings":{ "fileExtension":"json" },
        "onFinish":[
            {"actionName":"markAsExported","label":"Exported8"}
        ]
    }

    jobDescriptionDownload = {
        "type":"download",
        "credentials": credentials,
        "fileName":"_INSERT_FILE_NAME_",
        "fileSystem":"integrationServer"
    }

    # SEND REQUEST TO EXPENSIFY 
    
    data = {
        'requestJobDescription': str(jobDescriptionExport), 
        'template' : template_string
    }
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

        for report in reports:
            claim = frappe.get_doc({
                "doctype":"Expense Claim",
                "title":report["title"],
                "expense_approver":get_expense_approver(),
                "employee":get_employee(report["employee_name"]),
                "payable_account":get_payable_account(),
                "expenses":get_expense_list(report)
            })
            claim.save()
            frappe.db.commit()

            
