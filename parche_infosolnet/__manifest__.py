# -*- coding: utf-8 -*-
{
    'name': "parche_infosolnet",

    'summary': """
        Adaptación de la base de datos para Info Solutions Networking.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Info Solutions Networking",
    'website': "http://www.infosolutionsnetworking.com.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tecnico',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/contacto_view.xml',
        'views/templates.xml',
        'views/contrato_view.xml',
        'views/productos_licencia.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
