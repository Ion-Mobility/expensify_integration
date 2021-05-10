# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "expensify_integration"
app_title = "Expensify Integration"
app_publisher = "Ion"
app_description = "Integrate Expensify to ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "uriel@ionmobility.asia"
app_license = "MIT"



# include js, css files in header of web template
# web_include_css = "/assets/expensify_integration/css/expensify_integration.css"
# web_include_js = "/assets/expensify_integration/js/expensify_integration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "expensify_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "expensify_integration.install.before_install"
# after_install = "expensify_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "expensify_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"expensify_integration.tasks.all"
# 	],
# 	"daily": [
# 		"expensify_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"expensify_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"expensify_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"expensify_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "expensify_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "expensify_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "expensify_integration.task.get_dashboard_data"
# }

