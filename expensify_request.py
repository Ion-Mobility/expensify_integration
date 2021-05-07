import requests
import urllib
import json

template_string = open('expense_reports.ftl', 'r').read()

url = 'https://integrations.expensify.com/Integration-Server/ExpensifyIntegrations'

# Generate your credentials here: https://www.expensify.com/tools/integrations/
credentials = { 
    "partnerUserID":"INSERT USER ID", 
    "partnerUserSecret":"INSER USER SECRET" 
}

jobDescriptionExport = { 
    "type":"file", 
    "credentials": credentials, 
    "onReceive":{ "immediateResponse":["returnRandomFileName"] }, 
    "inputSettings":{ "type":"combinedReportData", "filters":{ "reportIDList":"1234,1235" } }, 
    "outputSettings":{ "fileExtension":"json" } 
}

jobDescriptionDownload={
    "type":"download",
    "credentials": credentials,
    "fileName":"RANDOM FILE NAME", #Change this
    "fileSystem":"integrationServer"
}

data = {
  'requestJobDescription': str(jobDescriptionExport), 
  'template' : template_string
}

response = requests.post(url, data=data)
print(response.text)

if response.status_code == 200:
    report_file_name = response.text

    print()
    print(response.text)
    print()

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
