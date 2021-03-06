# -*- encoding: utf-8 -*-
##############################################################################
#    ecoservice_partner_account_company_automatic
#    Copyright (c) 2016 ecoservice GbR (<http://www.ecoservice.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    This program based on OpenERP.
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
##############################################################################
from openerp.osv import osv


class partner(osv.osv):
    _inherit = 'res.partner'

    def create(self, cr, uid, vals, context=None):
        """ Inherit method to create the accounts automatically for partners without parent
        """
        result = super(partner, self).create(cr, uid, vals, context=context)
        if 'parent_id' in vals and 'is_company' in vals:
            if not vals['parent_id'] or (vals['parent_id'] and vals['is_company']):
                if 'customer' in vals and vals['customer']:
                    context['type'] = 'receivable'
                    self.create_accounts(cr, uid, [result], context=context)
                if 'supplier' in vals and vals['supplier']:
                    context['type'] = 'payable'
                    self.create_accounts(cr, uid, [result], context=context)
        return result
partner()
