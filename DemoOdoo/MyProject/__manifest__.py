# -*- coding: utf-8 -*-
{
    'name': "Fashion Shop",
    'sequence': 1,
    'summary': """
        Tổng hợp các mẫu thời trang mới nhất dành cho mọi lứa tuổi kể cả trẻ sơ sinh và trẻ nhỏ """,

    'description': """
        Shop thời trang với mọi lứa tuổi""",

    'author': "Fashion Shop",
    'website': "http://www.FashionShop.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', "crm", "sale"],

    # always loaded
    "css": ["static/src/css/customtreeview.css"],
    'qweb': [
        'report/templates.xml',
    ],
    'data': [
        'views/customer.xml',
        'views/employee.xml',
        'views/items_commodity.xml',
        'views/supplier.xml',
        'views/bill.xml',
        'views/orders.xml',
        'report/templates.xml',
        'report/report.xml',
        # 'security/ir.model.access.csv',

        'views/base.xml',
        'views/detail.xml',
        'views/order_success.xml',
        # 'views/theme.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}