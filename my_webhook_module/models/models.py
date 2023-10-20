from odoo import api, models, fields
import requests
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    track_and_trace_field = fields.Text(string="Track and Trace", readonly=False, copy=True, tracking=True, default="")

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        webhook_url = "http://host.docker.internal:3000/api/v1/orders"
        payload = {
            'order': order.id,
        }
        try:
            response = requests.post(webhook_url, json=payload, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            _logger.error("Error sending webhook: %s", e)

        return order


# from odoo import api, models, fields
# import requests
# import logging

# _logger = logging.getLogger(__name__)

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     track_and_trace_field = fields.Text(string="Track and Trace", readonly=False, copy=True, tracking=True, default="")

#     @api.model
#     def create(self, vals_list):
#         # Ensure vals_list is always a list
#         # this should  prevent batch creation from failing
#         # and should prevent the relevant warning in th container logs
#         if isinstance(vals_list, dict):
#             vals_list = [vals_list]

#         orders = super(SaleOrder, self).create(vals_list)

#         # webhook_url = "https://webhook.site/e96c9c48-116d-4cce-9629-014595a1d519"
#         webhook_url = "http://host.docker.internal:3000/api/v1/orders"

#         for order in orders:
#             payload = {
#                 'order': order.id,
#                 'version': '1.0.0'
#             }
#             try:
#                 response = requests.post(webhook_url, json=payload, timeout=5)
#                 response.raise_for_status()
#             except requests.RequestException as e:
#                 _logger.error("Error sending webhook for order %s: %s", order.id, e)

#         return orders

