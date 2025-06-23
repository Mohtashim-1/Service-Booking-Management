# Service Booking Management

A custom Frappe app/module for managing service bookings, with features like email notifications, webhook integration, and reporting.

---

## Features

- **Service Booking DocType**: Manage bookings with customer, service type, preferred date/time, and status fields.
- **Email Notification**: Automatically sends an approval email to the customer when a booking is approved.
- **Webhook Integration**: Sends booking details to a configurable webhook endpoint (e.g., webhook.site) on approval.
- **Script Report**: View all bookings with filters for Service Type and Status, plus a donut chart for status distribution.
- **Print Format**: Professional, print-friendly Jinja template for booking confirmation.

---

## Setup Instructions


1. **Install the app in your Frappe bench:**
   ```sh
   cd /path/to/your/frappe-bench
   bench get-app https://github.com/Mohtashim-1/Service-Booking-Management.git
   bench --site your-site-name install-app service_booking_management
   ```

2. **Migrate and restart:**
   ```sh
   bench --site your-site-name migrate
   bench restart
   ```

3. **Login to your Frappe/ERPNext site and explore the Service Booking module.**

---

## Usage Highlights

- **Booking Approval:**
  - When a booking's status is set to "Approved", the customer receives an email (if email is set) and the booking details are sent to the configured webhook endpoint.
- **Webhook Testing:**
  - You can use [webhook.site](https://webhook.site/) to receive and inspect webhook payloads for testing.
- **Reporting:**
  - Go to the "Service Booking" report to filter bookings by Service Type and Status, and view a donut chart of booking statuses.
- **Print Format:**
  - Use the provided Jinja print format for a professional booking confirmation printout.

---

## System Info

- **OS:** Ubuntu 22.04 LTS
- **Python Version:** 3.10.12
- **Frappe Version:** 15.71.0
- **ERPNext Version:** 15.65.4
- **Service Booking Management:** 0.0.1
- **Tools/Editors:** VS Code, Frappe Bench

---

## Quick Reference

- **Webhook Integration:**
  - Edit `service_booking.py` to set your webhook URL.
- **Email Template:**
  - Edit the message in `status_change_to_approved` in `service_booking.py`.
- **Report Location:**
  - `service_booking_management/service_booking_management/report/service_booking/`
- **Print Format:**
  - Add the Jinja template in the Print Format section for Service Booking.

---

## License

MIT License (see `LICENSE` file)
