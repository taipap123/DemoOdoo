
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Customers(models.Model):
    _name = "customers"
    _inherit = "employees"
    _description = u"Danh sách khách hàng"

    @api.model
    def create(self,vals):
        vals['code'] = int(self.search_count([]))
        return super(Customers, self).create(vals)


    _sql_constraints = [('ma_nha_cung_cap_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
