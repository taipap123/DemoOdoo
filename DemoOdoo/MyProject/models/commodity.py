# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions



class CategoryCommodity(models.Model):
    _name = "category_commodity"
    _description = u"Danh sách loại hàng"

    code = fields.Integer("Mã", required=True)
    name = fields.Char("Tên")


    _sql_constraints = [('ma_loai_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]


class Items(models.Model):
    _name = "items_commodity"
    _description = u"Danh sách mặt hàng"
    _inherit = "category_commodity"

    unit_price = fields.Integer("Đơn giá")
    new_field_id = fields.Many2one(comodel_name="category_commodity", string="Thuộc loại hàng", required=False, )
    unit = fields.Char(string="Đơn vị tính")


    _sql_constraints = [('ma_mat_hang_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]