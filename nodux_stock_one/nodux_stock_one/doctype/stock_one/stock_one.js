// Copyright (c) 2016, NODUX and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock One', {

	onload: function(frm) {
		var me = this;

		if (!frm.doc.status)
			frm.doc.status = 'Draft';
		frm.refresh_fields();
	},

	refresh: function(frm) {
		if (frm.doc.status== 'Draft' && frm.doc.lines ) {
			frm.add_custom_button(__("Done"), function() {
				frm.events.update_to_done(frm);
			});
		}

		frm.refresh_fields();

	},
	update_to_done: function(frm) {
		return frappe.call({
			doc: frm.doc,
			method: "update_to_done",
			freeze: true,
			callback: function(r) {
				frm.refresh_fields();
				frm.refresh();
			}
		})
	}

});
