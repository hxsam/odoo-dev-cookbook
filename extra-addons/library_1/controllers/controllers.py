# -*- coding: utf-8 -*-
from odoo import http

# class Library1(http.Controller):
#     @http.route('/library_1/library_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_1/library_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_1.listing', {
#             'root': '/library_1/library_1',
#             'objects': http.request.env['library_1.library_1'].search([]),
#         })

#     @http.route('/library_1/library_1/objects/<model("library_1.library_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_1.object', {
#             'object': obj
#         })