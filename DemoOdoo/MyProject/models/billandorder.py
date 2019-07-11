# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime


class Bill(models.Model):
    _name = "bills"
    _description = u"Danh sách các hóa đơn"
    _rec_name = "code"
    _auto = True
    _table = "fashion_bills"
    # _inherit = "items_commodity"
    # _inherits = {"items_commodity": 'goods'}

    code = fields.Integer("Mã", required=False)
    goods = fields.Many2many(comodel_name="items_commodity", ondelete='cascade', required=False,
                             string="Thông tin mặt hàng", )
    name_employees = fields.Many2one(comodel_name="employees", string="Nhân viên bán hàng", required=True, )
    name_customer = fields.Many2one(comodel_name="customers", string="Khách hàng", required=True, )
    datecurrent = fields.Date(string='Ngày lập', default=datetime.today().strftime("%Y-%m-%d %H:%M:%S"), readonly=True)
    total_price = fields.Integer(string="Tổng giá tiền", compute="_create_total_price", store=True)
    # goods = fields.One2many(comodel_name="details_bills", inverse_name="bill_loan", string="Danh sách mặt hàng", required=False, )
    mount = fields.Integer(string="Số lượng mua", default=1)
    # @api.depends("goods")
    # def _create_total_price(self):
    #     for rec in self:
    #       rec.total_price = 0
    #       if len(rec.goods) > 0:
    #           for i in range(len(rec.goods)):
    #             rec.total_price += rec.goods[i].unit_price
    #       else:
    #           pass


    @api.model
    def create(self, vals):
      vals['code'] = int(self.search_count([])) + 1
      return super(Bill, self).create(vals)


    _sql_constraints = [('ma_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]


class Order(models.Model):
    _name = "oders"
    _description = u"Danh sách các đơn đặt hàng"
    _auto = True
    _table = "fashion_orders"
    _inherit = "bills"
    name_customer = fields.Many2one(comodel_name="suppliers", string="Đối tác", required=True, )
#
#
# class DetailBill(models.Model):
#     _name = "details_bills"
#     _description = u"Danh sách chi tiết các hóa đơn"
#     _auto = True
#     _table = "fashion_details_bills"
#
#     bill_loan = fields.Many2one(comodel_name="bills", string="Mã phiếu", required=False, )
#     items_loan = fields.Many2one(comodel_name="items_commodity", string="Tên mặt hàng", required=False,)
#     mount = fields.Integer(string="Số lượng mua", default=1)
#
#     @api.constrains("mount")
#     def _check_mount(self):
#         for rec in self:
#             if rec.mount < 1:
#                 raise exceptions.ValidationError("Vui lòng xem lại số lượng hàng mua")

