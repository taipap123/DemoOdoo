
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Supplier(models.Model):
    _name = "suppliers"
    _inherit = "employees"
    _description = u"Danh sách các nhà cung cấp"


_sql_constraints = [('ma_nha_cung_cap_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
