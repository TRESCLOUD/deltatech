# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
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
#
##############################################################################


from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
import math

 

class res_partner(models.Model):
    _inherit = "res.partner" 

    ref_customer = fields.Char(string="Code Customer SAGA", size=5)
    ref_supplier = fields.Char(string="Code Supplier SAGA", size=5)


    @api.model
    def create(self,   vals ):  
        if ('ref_customer' not in vals) or (vals.get('ref_customer') in ('/', False)):
            if  vals.get('customer',False): 
                sequence = self.env.ref('deltatech_saga.sequence_ref_customer')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )

        if ('ref_supplier' not in vals) or (vals.get('ref_supplier') in ('/', False)):
            if  vals.get('customer',False): 
                sequence = self.env.ref('deltatech_saga.sequence_ref_supplier')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )
        return super(res_partner, self).create( vals )


    @api.multi
    def write(self, vals):
        if ('ref_customer' in vals) and (vals.get('ref_customer') in ('/', False)):
            self.ensure_one()
            if self.customer:
                sequence = self.env.ref('deltatech_saga.sequence_ref_customer')
                if sequence:
                    vals['ref_customer'] = sequence.next_by_id( )
                    
        if ('ref_supplier' in vals) and (vals.get('ref_supplier') in ('/', False)):
            self.ensure_one()
            if self.supplier:
                sequence = self.env.ref('deltatech_saga.sequence_ref_supplier')
                if sequence:
                    vals['ref_supplier'] = sequence.next_by_id( )
        
        return super(res_partner, self).write( vals)
    
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: