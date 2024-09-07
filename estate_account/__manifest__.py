# -*- coding: utf-8 -*-
{
    'name': "estate account extension",

    'summary': "create invoice for real estate module",

    'description': """
create invoice for real estate module
    """,

    'author': "Mahmoud",
    'website': "https://www.mah007.com",


    'category': 'Accounting/Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','estate','account','sale','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizards/estate_wiz.xml',
        'views/estate_property_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

