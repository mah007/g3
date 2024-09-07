# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id','price_unit')
    def _check_product_unit(self):
        for line in self:

            if line.product_id.lst_price != line.price_unit:
                raise ValidationError('Price not Match : '+str(line.product_id.name)+ ' ' +str(line.product_id.lst_price))
