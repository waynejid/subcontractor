# -*- coding: utf-8 -*-
###############################################################################
#
#   account_invoice_subcontractor for OpenERP
#   Copyright (C) 2015-TODAY Akretion <http://www.akretion.com>.
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'account_invoice_subcontractor',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        'account',
        'hr',
        'inter_company_rules',
    ],
    'init_xml': [],
    'data': [
        'data/cron_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'hr_view.xml',
        'subcontractor_work_view.xml',
        'invoice_view.xml',
        'wizard/subcontractor_invoice_work_view.xml',
        'wizard/supplier_invoice_work_view.xml',
        'product_view.xml',
    ],
    'installable': True,
}
