# -*- coding: utf-8 -*-
from odoo import http
import smtplib, ssl, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .. import myConfig
# import odoo.addons.web.controllers.main as main

class Project(http.Controller):

    @http.route('/myshop', auth="public", type='http', website=True)
    def shop(self, **kw):
        list_item = http.request.env["items_commodity"].sudo().search([])
        return http.request.render('MyProject.template_master', {'list_item':list_item})

    @http.route('/myshop/detail/<id>', auth='public', type='http', website=True)
    def detail(self, id, **kw):
        item = http.request.env["items_commodity"].sudo().search([['id', '=', id]])
        return http.request.render('MyProject.template_detail', {'item': item})

    # @http.route('/myshop/order/', type='http', auth="public", methods=['POST'], website=True)
    @http.route('/myshop/order/', type='http', website=True, auth="public" , csrf=False)
    def order(self,**kw):
        name = kw.get("contact_name")
        phone = kw.get("phone_from")
        email = kw.get("email_from")
        address = kw.get("address_from")
        amount = kw.get("amount")
        item_id = kw.get("item_id")
        item_name = kw.get("item_name")
        item_unit_price = kw.get("item_unit_price")
        #insert model customers
        http.request.env["customers"].sudo().create({'name': name, 'phone': phone, 'email': email, 'address': address})
        # insert model bills
        id_bills = http.request.env["bills"].sudo().create({'name': name, 'phone': phone, 'email': email, 'address': address})
        # insert model bills_items_commodity_rel
        http.request.billsenv["bills_items_commodity_rel"].sudo().create(
            {'bills_id': id_bills, 'items_commodity_id': item_id})

        self.sent_Mail_Order(email, name, phone, address, item_name, amount,  str(int(item_unit_price) * int(amount)))
        return http.request.render('MyProject.order_success', {'success':True})

    def sent_Mail_Order(self, receiver_order, name, phone, address, items, amount, total):
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = myConfig.CONST_EMAIL
        receiver_email = receiver_order
        password = myConfig.CONST_EPASS
        body =  "                    Kính chào quý khách!\n" \
                "-----Fashion shop gửi thông tin chi tiết đặt hàng-----\n" \
                "Tên khách hàng:    " + name + "\n" \
                "Số điện thoại:         " + phone + "\n" \
                "Địa chỉ:                 " + address + "\n" \
                "Đặt hàng:            " + items + " - Số lượng: " + amount + "\n"\
                "TỔNG HÓA ĐƠN:        " + total + " VNĐ\n" \
                "Xin cám ơn quý khách !"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Fashion shop xác nhận đơn đặt hàng"

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)