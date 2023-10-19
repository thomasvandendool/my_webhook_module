# -*- coding: utf-8 -*-
# from odoo import http


# class MyWebhookModule(http.Controller):
#     @http.route('/my_webhook_module/my_webhook_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_webhook_module/my_webhook_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_webhook_module.listing', {
#             'root': '/my_webhook_module/my_webhook_module',
#             'objects': http.request.env['my_webhook_module.my_webhook_module'].search([]),
#         })

#     @http.route('/my_webhook_module/my_webhook_module/objects/<model("my_webhook_module.my_webhook_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_webhook_module.object', {
#             'object': obj
#         })
