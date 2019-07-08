# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Employees(models.Model):
    _name = "employees"
    _description = u"Danh sách nhân viên"

    code = fields.Integer("Mã", required=True)
    name = fields.Char("Tên")
    address = fields.Char(string="Địa chỉ")
    phone = fields.Char(string="Số điện thoại")

    @api.constrains("phone")
    def _phone_validate(self):
        for employee in self:
            if len(employee.phone) < 10:
                raise exceptions.ValidationError(u"Số điện thoại không hợp lệ")


_sql_constraints = [('ma_nhan_vien_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
