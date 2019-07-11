# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions



class CategoryCommodity(models.Model):
    _name = "category_commodity"
    _description = u"Danh sách loại hàng"
    _auto = True
    _table = "fashion_categorys_commodity"
    code = fields.Integer("Mã", required=True, readonly='True')
    name = fields.Char("Tên")

    @api.model
    def create(self,vals):
        vals['code'] = int(self.search_count([])) + 1
        return super(CategoryCommodity, self).create(vals)


    _sql_constraints = [('ma_code duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]


class Items(models.Model):
    _name = "items_commodity"
    _auto = True
    _table = "fashion_items_commodity"
    _description = u"Danh sách mặt hàng"
    _inherit = "category_commodity"

    unit_price = fields.Integer("Đơn giá")
    category_commodity = fields.Many2many(comodel_name="category_commodity", string="Thuộc loại hàng", required=False, )
    unit = fields.Char(string="Đơn vị tính")
    img_link = fields.Char(size = 2000)
    description = fields.Text(size = 2000)
