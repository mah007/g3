#
from odoo import api, fields, models


class EstatWiz(models.TransientModel):
    _name = 'estate.wiz'
    _description = 'Estat Wizard payment'

    payment_type = fields.Selection([("cash", "Cash"), ("install", "Installment")],default='cash', string="Payment Type")
    installment_period = fields.Selection([("1", "instant"), ("6", "6 months"), ("12", "12 months"), ("24", "24 months")],default='1' ,string="Installment Period")
    fees = fields.Float(string="Administration Fees")


    # Actions
    def do_payment(self):
        print('Payed')
        pay_id = self.env.context.get('active_id')
        if pay_id:
            pay = self.env['estate.property'].browse(pay_id)
            pay.action_solds(installments=self.installment_period,fees=self.fees)
        return pay


