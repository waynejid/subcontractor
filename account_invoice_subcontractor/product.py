# -*- coding: utf-8 -*-
###############################################################################
#
#   account_invoice_subcontractor for OpenERP
#   Copyright (C) 2013-TODAY Akretion <http://www.akretion.com>.
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

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    no_commission = fields.Boolean(
        help="This product has no commission for subcontractor work.")
    subcontracted = fields.Boolean(
        company_dependent=True,
        help="This product is subcontracted, and so the subcontractor work"
            "will be required on the invoice")
