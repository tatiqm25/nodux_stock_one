# -*- coding: utf-8 -*-
# Copyright (c) 2015, NODUX and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockOne(Document):
	def before_save(self):
		self.docstatus = 1

	def update_to_done(self):
		for line in self.lines:
			if line.item:
				product = frappe.get_doc("Item", line.item)
				if self.type == "Entry":
					if product.total:
						product.total = product.total + line.quantity
					else:
						product.total = line.quantity
				else:
					if product.total:
						product.total = product.total - line.quantity

				product.save()
		self.status = "Done"
		self.save()
