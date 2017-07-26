# Copyright (c) 2013, NODUX and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe import msgprint, _

def execute(filters=None):
	if not filters: filters = {}

	stock_list = get_stock(filters)
	columns = get_columns(stock_list)

	if not stock_list:
		msgprint(_("No record found"))
		return columns, stock_list

	data = []
	for inv in stock_list:
		row = [inv.item_code, inv.item_name, inv.total, inv.list_price,
		inv.cost_price, inv.barcode]
		data.append(row)
	return columns, data

def get_columns(stock_list):
	"""return columns based on filters"""
	columns = [
		_("Code")+ "::120",
		_("Product") + "::480", _("Total Stock") + "::80",
		_("List Price") + ":Currency/currency:120",
		_("Cost Price") + ":Currency/currency:120", _("Barcode")+ "::120"]

	return columns

def get_conditions(filters):
	conditions = ""

	if filters.get("barcode"): conditions += " and barcode = %(barcode)s"
	if filters.get("code"): conditions += " and item_code regexp %(code)s"
	if filters.get("item"): conditions += " and item_name regexp %(item)s"

	return conditions

def get_stock(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select item_code, item_name, total, list_price,
		cost_price, barcode
		from `tabItem`
		where disabled = 0 %s order by name desc""" %
		conditions, filters, as_dict=1)
