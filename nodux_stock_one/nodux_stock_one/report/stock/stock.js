// Copyright (c) 2016, NODUX and contributors
// For license information, please see license.txt

frappe.query_reports["Stock"] = {
	"filters": [
		{
			"fieldname":"code",
			"label": __("Code"),
			"fieldtype": "Data",
			"default": "",
			"width": "80"
		},
		{
			"fieldname":"barcode",
			"label": __("Barcode"),
			"fieldtype": "Data",
			"default": "",
			"width": "80"
		},
		{
			"fieldname":"item",
			"label": __("Item"),
			"fieldtype": "Data",
			"default": "",
			"width": "80"
		}
	]
}
