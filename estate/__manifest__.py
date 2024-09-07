# -*- coding: utf-8 -*-
{
    'name': "Real Estate Advertisement ",

    'summary': "The Real Estate Advertisement module",

    'description': """
    
    Our new module will cover a business area which is very specific and therefore not included in the standard set of modules:
     real estate. It is worth noting that before developing a new module, it is good practice to verify that Odoo doesn’t already provide a way to answer the specific business case
    
    """,

    'author': "Mahmoud",
    'website': "https://www.mah007.com",

    'version': '0.1',
    'category': 'Sales/Sales',
    'sequence': 10,

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product'],

    # always loaded
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
        'report/ir_report.xml',
        'report/report_template.xml',
        'views/template_property.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "license": "LGPL-3",
}

