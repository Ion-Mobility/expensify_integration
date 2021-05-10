import frappe
import requests
from frappe import _
import requests
import urllib
import json

# api/method/expensify_integration.expensify_integration.expensify_integration.handle_sample_expense



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

    # Generate your credentials here: https://www.expensify.com/tools/integrations/
    credentials = { 
        "partnerUserID":"INSERT USER ID", 
        "partnerUserSecret":"INSER USER SECRET" 
    }

    credentials["partnerUserID"] = APIKEY
    credentials["partnerUserSecret"] = SECRET

    jobDescriptionExport = { 
        "type":"file", 
        "credentials": credentials, 
        "onReceive":{ "immediateResponse":["returnRandomFileName"] }, 
        "inputSettings":{ "type":"combinedReportData", "filters":{ "reportIDList":"73530462" } }, 
        "outputSettings":{ "fileExtension":"json" } 
    }

    jobDescriptionDownload={
        "type":"download",
        "credentials": credentials,
        "fileName":"RANDOM FILE NAME",
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

        print("REPORTS:")
        for report in reports:
            print(json.dumps(report))
            print()




"""
    claim = frappe.new_doc('Expense Claim')
    claim.save(ignore_permissions=True)
    frappe.db.commit()
"""
