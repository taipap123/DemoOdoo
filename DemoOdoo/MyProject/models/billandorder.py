# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

class Bill(models.Model):
    _name = "bills"
    _description = u"Danh sách các hóa đơn"
    _rec_name ="code"
    # _inherit = "items_commodity"
    # _inherits = {"items_commodity": 'goods'}
    code = fields.Integer("Mã", required=True)
    goods = fields.Many2many(comodel_name="items_commodity", ondelete='cascade', column1="name", required=True, string="Thông tin mặt hàng", )
    name_employees = fields.Many2one(comodel_name="employees", string="Nhân viên bán hàng", required=True, )
    name_customer = fields.Many2one(comodel_name="customers", string="Khách hàng", required=True, )
    datecurrent = fields.Date(string='Ngày lập', default=datetime.today().strftime("%Y-%m-%d %H:%M:%S"), readonly=True)

_sql_constraints = [('ma_don_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]


class Order(models.Model):
    _name = "oders"
    _description = u"Danh sách các đơn đặt hàng"
    _inherit = "bills"
_sql_constraints = [('ma_don_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
