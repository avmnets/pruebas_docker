# -*- coding: utf-8 -*-
# from odoo import http


# class Merma(http.Controller):
#     @http.route('/merma/merma', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/merma/merma/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('merma.listing', {
#             'root': '/merma/merma',
#             'objects': http.request.env['merma.merma'].search([]),
#         })

#     @http.route('/merma/merma/objects/<model("merma.merma"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('merma.object', {
#             'object': obj
#         })
