# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ion and Contributors
# See license.txt
from __future__ import unicode_literals
import frappe
import unittest
import expensify_integration
		
def request_report():
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

	return response

class TestExpensifySettings(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_simple_test(self):
		self.assertTrue(200 == 200)

	def test_expensify_connection(self):
		report = request_report()
		self.assertTrue(report.status_code == 200)


