# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class Agreement(models.Model):
    _inherit = 'agreement'

    req_cust_order_kept_open = fields.Many2one(
        'agreement.parameter.value',
        string='Order kept open',
        domain=[
            ('parameter', '=',
             'req_cust_order_kept_open')
        ],
    )
    req_cust_backorder_shipment = fields.Many2one(
        'agreement.parameter.value',
        string='Back order shipment',
        domain=[
            ('parameter', '=', 'req_cust_backorder_shipment')
        ],
    )
    req_so_partial_delivery = fields.Many2one(
        'agreement.parameter.value',
        string='Partial deliveries',
        domain=[('parameter', '=', 'req_so_partial_delivery')],
    )

    @api.model
    def _get_customer_agreement_fields(self):
        return super()._get_customer_agreement_fields() + [
            'req_cust_backorder_shipment',
            'req_cust_order_kept_open',
            'req_cust_invoice_ref',
        ]

    @api.model
    def _get_sale_agreement_fields(self):
        return super()._get_sale_agreement_fields() + [
            'req_so_partial_delivery',
        ]
