# -*- coding: utf-8 -*-
{
    'name': 'To–Do App',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': 'Manage your personal To–Do tasks.',

    'application': True,
    'author': "MARK",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}