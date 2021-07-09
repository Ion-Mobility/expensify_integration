# -*- coding: utf-8 -*-galois theory
# Copyright (c) 2021, Ion and Contributors
# See license.txt
from __future__ import unicode_literals
import frappe
import unittest
import expensify_integration
import requests
import urllib
import json
import os

class TestExpensifySettings(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_simple_test(self):
		self.assertTrue(200 == 200)



	def test_data_ingestion():
		data_input = 
		{
		"title":"Stationery",
		"employee_name":"Uriel",
		"expense_approver":"uriel@ionmobility.asia",
		"posting_date":"03-04-2021",
		"expenses":[
				{
					"amount":"1",
					"expense_type":"Office Equipment",
					"description":"Whiteboard markers",
					"expense_date":"03-04-2021"
				}
			]
		}

		expensify_integration.expensify_integration.doctype.expensify_settings.convert_expenses(data_input)


	def test_frappe_doctypes():



