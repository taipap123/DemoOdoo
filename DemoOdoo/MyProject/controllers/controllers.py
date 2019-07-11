# -*- coding: utf-8 -*-
from odoo import http
# import odoo.addons.web.controllers.main as main

class Project(http.Controller):

    @http.route('/myshop', auth="public", type='http', website=True)
    def shop(self, **kw):
        list_item = http.request.env["items_commodity"].sudo().search([])
        return http.request.render('MyProject.template_master', {'list_item':list_item})

    @http.route('/myshop/detail/<id>', auth='public', type='http', website=True)
    def detail(self, id, **kw):
        item = http.request.env["items_commodity"].sudo().search([['id', '=', id]])
        return http.request.render('MyProject.template_detail', {'item': item})

    # @http.route('/myshop/order/', type='http', auth="public", methods=['POST'], website=True)
    @http.route('/myshop/order/', type='http', website=True, auth="public" , csrf=False)
    def order(self,**kw):
        name = kw.get("contact_name")
        phone = kw.get("phone_from")
        email = kw.get("email_from")
        address = kw.get("address_from")
        http.request.env["customers"].sudo().create({'name': name, 'phone': phone, 'email': email, 'address': address})
        return http.request.render('MyProject.order_success', {'success':True})