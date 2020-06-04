# -*- coding: utf-8 -*-
from odoo import http

# class Loc(http.Controller):
#     @http.route('/loc/loc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc/loc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc.listing', {
#             'root': '/loc/loc',
#             'objects': http.request.env['loc.loc'].search([]),
#         })

#     @http.route('/loc/loc/objects/<model("loc.loc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc.object', {
#             'object': obj
#         })