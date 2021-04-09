# -*- coding: utf-8 -*-
# from odoo import http


# class ParcheInfosolnet(http.Controller):
#     @http.route('/parche_infosolnet/parche_infosolnet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parche_infosolnet/parche_infosolnet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parche_infosolnet.listing', {
#             'root': '/parche_infosolnet/parche_infosolnet',
#             'objects': http.request.env['parche_infosolnet.parche_infosolnet'].search([]),
#         })

#     @http.route('/parche_infosolnet/parche_infosolnet/objects/<model("parche_infosolnet.parche_infosolnet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parche_infosolnet.object', {
#             'object': obj
#         })
