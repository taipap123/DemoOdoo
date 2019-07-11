
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Customers(models.Model):
    _name = "customers"
    _inherit = "employees"
    _description = u"Danh sách khách hàng"
    _auto = True
    _table = "fashion_customers"
