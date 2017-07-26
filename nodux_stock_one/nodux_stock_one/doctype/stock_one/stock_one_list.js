// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

// render
frappe.listview_settings['Stock One'] = {
	add_fields: ["date", "status"],
	get_indicator: function(doc) {
		if((doc.status)=="Draft") {
			return [__("Draft"), "red", "status,=,Draft"];
		} else if((doc.status)=="Done") {
			return [__("Done"), "green", "status,=,Done"]
		}
	},
	right_column: "date"
};
