# -*- coding: utf-8 -*-
# from odoo import http


# class Tutorials(http.Controller):
#     @http.route('/tutorials/tutorials', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorials/tutorials/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorials.listing', {
#             'root': '/tutorials/tutorials',
#             'objects': http.request.env['tutorials.tutorials'].search([]),
#         })

#     @http.route('/tutorials/tutorials/objects/<model("tutorials.tutorials"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorials.object', {
#             'object': obj
#         })

