
# -*- coding: utf-8 -*-
{
    'name': "hms",

    'summary': "Human management system",

    'description': "Human management system",
    'author': "Mohammed Hamdy Ayada",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'report/hms_patient_reports.xml',
        'report/hms_patient_template.xml',
        'views/hms_patient.xml',
        'views/hms_doctor.xml',
        'views/hms_department.xml',
        'views/hms_customer.xml',

    ],

}




