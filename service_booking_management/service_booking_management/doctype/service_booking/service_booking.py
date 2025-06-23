# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests


class ServiceBooking(Document):
	def on_update(self):
		self.status_change_to_approved()

	def status_change_to_approved(self):
		if self.status == "Approved":
			if self.customer_email:
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
			else:
				frappe.msgprint("Customer email is not set for this booking.")
			self.send_to_webhook()

	def send_to_webhook(self):
		webhook_url = "https://webhook.site/d60ba3fe-0b57-4e20-9cc6-edf99c44e24e"
		payload = {
			"booking_id": self.name,
			"customer_name": self.customer_name,
			"customer_email": self.customer_email,
			"service_type": self.service_type,
			"preferred_datetime": str(self.preferred_datetime),
			"status": self.status
		}
		try:
			response = requests.post(webhook_url, json=payload, timeout=5)
			response.raise_for_status()
			frappe.msgprint("Booking details sent to webhook!")
		except Exception as e:
			frappe.log_error(f"Webhook error: {e}")