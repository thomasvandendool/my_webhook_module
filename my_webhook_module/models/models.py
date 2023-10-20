from odoo import api, models, fields
import requests
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    track_and_trace_field = fields.Text(string="some track and trace data")

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        
        # webhook_url = "https://webhook.site/e96c9c48-116d-4cce-9629-014595a1d519"
        webhook_url = "http://host.docker.internal:3000/api/v1/orders"
        payload = {
            'orderd': order.id
        }
        try:
            response = requests.post(webhook_url, json=payload, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            _logger.error("Error sending webhook: %s", e)

        return order
