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

    @api.model
    def create(self, vals):
        vals['name'] = vals.get('name').title()
        # Tạo record cho model
        # self.env['quanlysachlienlac'].create({'name': vals['name']})
        # Chỉnh sửa record cho model
        # self.env['quanlysachlienlac'].browse(20).name
        # Tìm kím
        vals['code'] = int(self.search_count([]))
        # self.env['quanlysachlienlac'].search([])
        return super(Employees, self).create(vals)


_sql_constraints = [('ma_nhan_vien_duy_nhat', 'UNIQUE(code)', u'Mã trùng rồi điền mã cái khác đi')]
