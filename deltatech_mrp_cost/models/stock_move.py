# -*- coding: utf-8 -*-


from odoo import api
from odoo import models


class StockMove(models.Model):
    _inherit = 'stock.move'


    @api.multi
    def action_done(self):
        for move in self:
            for op in move.picking_id.pack_operation_ids:
                if op.product_id == move.product_id:
                    if not op.qty_done:
                        op.qty_done = op.product_qty
        return super(StockMove,self).action_done()
