
frappe.listview_settings['Service Booking'] = {
    // ensure status is fetched
    add_fields: ['status'],
    get_indicator: function(doc) {
      if (doc.status === 'Requested') {
        // label, color, filter
        return [__('Requested'), 'orange', 'status,=,Requested'];
      }
      else if (doc.status === 'Approved') {
        return [__('Approved'), 'blue', 'status,=,Approved'];
      }
      else if (doc.status === 'Completed') {
        return [__('Completed'), 'green', 'status,=,Completed'];
      }
    }
  };
  