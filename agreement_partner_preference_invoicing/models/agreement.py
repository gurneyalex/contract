# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class Agreement(models.Model):
    _inherit = 'agreement'

    req_cust_invoice_transmission_mode = fields.Many2one(
        'agreement.parameter.value',
        string='Invoice sending mode',
        domain=[('parameter', '=', 'req_cust_invoice_transmission_mode')],
    )
    req_cust_invoice_transmission_frequency = fields.Many2one(
        'agreement.parameter.value',
        string='Invoice sending frequency',
        domain=[
            ('parameter', '=', 'req_cust_invoice_transmission_frequency')
        ],
    )
    req_cust_invoice_ref = fields.Many2one(
        'agreement.parameter.value',
        string='Invoice reference',
        domain=[('parameter', '=', 'req_cust_invoice_ref')],
    )

    @api.model
    def _get_customer_agreement_fields(self):
        """return a list of field names which are related to sale conditions"""
        # extend the list in modules implementing specific conditions
        return super()._get_customer_agreement_fields() + [
            'req_cust_invoice_transmission_mode',
            'req_cust_invoice_transmission_frequency',
            'req_cust_invoice_ref',
        ]
