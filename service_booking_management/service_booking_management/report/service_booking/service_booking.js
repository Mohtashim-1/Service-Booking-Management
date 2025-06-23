// Copyright (c) 2025, mohtashim and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking"] = {
	"filters": [
		{
			"fieldname": "service_type",
			"label": __("Service Type"),
			"fieldtype": "Data"
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nRequested\nApproved\nCompleted"
		}
	],
	"formatter": function(value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname === "status") {
			if (value === "Approved") {
				return `<span style="color:green;">${value}</span>`;
			} else if (value === "Requested") {
				return `<span style="color:orange; ">${value}</span>`;
			} else if (value === "Completed") {
				return `<span style="color:blue;">${value}</span>`;
			}
		}
		return value;
	}
};
