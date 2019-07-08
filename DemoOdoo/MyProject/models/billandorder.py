# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

class Bill(models.Model):
    _name = "bills"
    _description = u"Danh sách các hóa đơn"
    code = fields.Integer("Mã", required=True)
    # default = datetime.datetime.now()
    datecurrent = fields.Date(string='Ngày lập', default=datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

_sql_constraints = [('ma_don_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]


class Order(models.Model):
    _name = "oders"
    _description = u"Danh sách các đơn đặt hàng"
    _inherit = "bills"
_sql_constraints = [('ma_don_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
