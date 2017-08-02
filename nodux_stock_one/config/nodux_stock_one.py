from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Reporte Stock"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"name": "Stock",
					"doctype": "Stock One",
					"is_query_report": True
				}
			]
		}
	]
