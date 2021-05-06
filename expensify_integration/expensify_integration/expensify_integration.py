import frappe
import requests
from frappe import _

# api/method/expensify_integration.expensify_integration.expensify_integration.handle_sample_expense

@frappe.whitelist(allow_guest=True)
def handle_sample_expense(**kwargs):
	claim = frappe.new_doc('Expense Claim')
	claim.save(ignore_permissions=True)
	frappe.db.commit()

