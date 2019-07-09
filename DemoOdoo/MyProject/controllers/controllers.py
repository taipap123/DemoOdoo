# -*- coding: utf-8 -*-
from odoo import http
# import odoo.addons.web.controllers.main as main

class Project(http.Controller):

    @http.route('/myshop', auth="public", type='http', website=True)
    def shop(self, **kw):
        list_item = http.request.env["MyProject.items_commodity"].sudo().search([])
        return http.request.render('MyProject.template_master', {'list_item':list_item})

#     @http.route('/project/project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project.listing', {
#             'root': '/project/project',
#             'objects': http.request.env['project.project'].search([]),
#         })

#     @http.route('/project/project/objects/<model("project.project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project.object', {
#             'object': obj
#         })