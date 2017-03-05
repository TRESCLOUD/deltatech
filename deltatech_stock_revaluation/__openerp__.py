# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2017 Deltatech All Rights Reserved
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

{
    "name" : "Deltatech Stock Revaluation",
    "version" : "2.0",
    "author" : "Dorin Hongu",
    "website" : "",
    "description": """
    
Functionalitati:

    - reevaluare stoc
    

    """,
    
    "category" : "Generic Modules/Stock",
    "depends" : ['deltatech','stock'],


    "data" : [ 
                  'stock_view.xml', 
                  'stock_revaluation_view.xml',
                  'data/stock_revaluation_data.xml',
                  'security/stock_revaluation_security.xml',
                  'security/ir.model.access.csv',
                  
             ],
    
    
    "active": False,
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

