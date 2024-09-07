# -*- coding: utf-8 -*-
# from odoo import http


# class SaleWorn(http.Controller):
#     @http.route('/sale_worn/sale_worn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_worn/sale_worn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_worn.listing', {
#             'root': '/sale_worn/sale_worn',
#             'objects': http.request.env['sale_worn.sale_worn'].search([]),
#         })

#     @http.route('/sale_worn/sale_worn/objects/<model("sale_worn.sale_worn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_worn.object', {
#             'object': obj
#         })

