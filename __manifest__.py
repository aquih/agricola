# -*- coding: utf-8 -*-
{
    'name': "Agricola",

    'summary': """ Módulo para RRHH de empresas agropecuarias """,

    'description': """
         Módulo para RRHH de empresas agropecuarias
    """,

    'author': "aquiH",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.2',

    'depends': ['base', 'rrhh', 'hr_timesheet', 'hr_payroll'],

    'data': [
        'views/agricola_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_payslip_run_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_timesheet_views.xml',
        'views/project_task_views.xml',
        'security/ir.model.access.csv',
    ],
}
