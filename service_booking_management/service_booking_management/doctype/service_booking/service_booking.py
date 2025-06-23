# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServiceBooking(Document):
	def on_update(self):
		self.status_change_to_approved()

	def status_change_to_approved(self):
		if self.status == "Approved":
			message = f"""
			<p>Dear {self.customer_name},</p>
			<p>Your service booking has been <b>approved</b>!</p>
			<h4>Booking Details:</h4>
			<ul>
				<li><b>Booking ID:</b> {self.name}</li>
				<li><b>Service Type:</b> {self.service_type}</li>
				<li><b>Preferred Date and Time:</b> {self.preferred_datetime}</li>
			</ul>
			<p>We look forward to serving you. If you have any questions, feel free to reply to this email.</p>
			<br>
			<p>Best regards,<br>
			Service Booking Team</p>
			"""
			frappe.sendmail(
				recipients=self.customer_email,
				subject="Service Booking Approved",
				message=message
			)