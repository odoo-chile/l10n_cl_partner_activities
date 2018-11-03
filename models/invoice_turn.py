# -*- coding: utf-8 -*-
from openerp import models, fields, api


class InvoiceTurn(models.Model):
    _inherit = "account.invoice"

    @api.one
    @api.depends('partner_id')
    def _get_available_turns(self):
        self.ensure_one()
        available_turn_ids = self.partner_id.partner_activities_ids
        for turn in available_turn_ids:
            self.invoice_turn = turn.id

    invoice_turn = fields.Many2one(
        'partner.activities',
        'Giro Receptor',
        readonly=True,
        store=True,
        states={'draft': [('readonly', False)]},
        compute=_get_available_turns)
