
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Supplier(models.Model):
    _name = "suppliers"
    _auto = True
    _table = "fashion_supplier"
    _inherit = "employees"
    _description = u"Danh sách các nhà cung cấp"

    code = fields.Char("Mã nhà cung cấp")

