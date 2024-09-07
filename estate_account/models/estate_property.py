# -*- coding: utf-8 -*-

from odoo import models, Command,fields
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ---------------------------------------- Action Methods -------------------------------------

    def action_solds(self,installments=None,fees=None):

        res = super().action_sold()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        # Another way to get the journal:2
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        #invoice_date = ""
        vals =[]
        invoices = self.env["account.move"]
        if installments:
            no_month = int(installments)
            for i in range(no_month):
                print(i)
                for prop in self:
                    if prop.property_type_id.product_id.id:
                        print(prop.property_type_id.product_id.name)
                        val =(
                            {
                                "partner_id": prop.buyer_id.id,
                                "move_type": "out_invoice",
                                "invoice_date": fields.Date.context_today(self) + relativedelta(months=i+1),
                                "journal_id": journal.id,
                                "invoice_line_ids": [
                                    Command.create({
                                        "product_id": prop.property_type_id.product_id.id,
                                        "name": prop.name,
                                        "quantity": 1.0,
                                        "price_unit": (prop.selling_price/no_month) ,
                                    }),
                                    Command.create({
                                        'product_id': self.env.ref('estate_account.product_product_admin_fee').id,
                                        "name": "Administrative fees",
                                        "quantity": 1.0,
                                        "price_unit": 100.0 or fees,
                                    }),
                                ],
                            }
                        )
                        print(val,'val')
                        vals.append(val)
                        print(vals,'vals')
                    else:
                        raise UserError('Product not defined')
                print(vals)
            invoices.create(vals)

            print('Done')
            return res