# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)

	status_counts = {}
	for row in data:
		status = row.get("status")
		status_counts[status] = status_counts.get(status, 0) + 1
	chart = {
		"data": {
			"labels": list(status_counts.keys()),
			"datasets": [{
				"name": "Bookings by Status",
				"values": list(status_counts.values())
			}]
		},
		"type": "donut",
		"height": 300
	}

	return columns, data, None, chart

def get_columns():
	return [
		{"label": "Booking ID", "fieldname": "name", "fieldtype": "Link", "options": "Service Booking", "width": 120},
		{"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
		{"label": "Customer Email", "fieldname": "customer_email", "fieldtype": "Data", "width": 180},
		{"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data", "width": 120},
		{"label": "Preferred Date & Time", "fieldname": "preferred_datetime", "fieldtype": "Data", "width": 150},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100}
	]

def get_data(filters):
	conditions = {}
	if filters.get("service_type"):
		conditions["service_type"] = filters["service_type"]
	if filters.get("status"):
		conditions["status"] = filters["status"]

	bookings = frappe.get_all(
		"Service Booking",
		filters=conditions,
		fields=[
			"name", "customer_name", "customer_email", "service_type",
			"preferred_datetime", "status", "creation"
		],
		order_by="creation desc"
	)
	return bookings
