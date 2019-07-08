# -*- coding: utf-8 -*-
{
    'name': "Fashion Shop",

    'summary': """
        Tổng hợp các mẫu thời trang mới nhất dành cho mọi lứa tuổi kể cả trẻ sơ sinh và trẻ nhỏ """,

    'description': """
        Shop thời trang với mọi lứa tuổi""",

    'author': "Fashion Shop",
    'website': "http://www.FashionShop.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}