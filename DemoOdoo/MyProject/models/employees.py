# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

class Employees(models.Model):
    _name = "employees"
    _description = u"Danh sách nhân viên"

    code = fields.Integer("Mã", required=True)
    name = fields.Char("Tên")
    email = fields.Char("Email")
    address = fields.Char(string="Địa chỉ")
    phone = fields.Char(string="Số điện thoại")

    @api.constrains("phone")
    def _phone_validate(self):
        for employee in self:
            if len(employee.phone) < 10:
                raise exceptions.ValidationError(u"Số điện thoại không hợp lệ")

    @api.model
    def create(self, vals):
        vals['name'] = vals.get('name').title()
        vals['code'] = int(self.search_count([]))
        return super(Employees, self).create(vals)


_sql_constraints = [('ma_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
