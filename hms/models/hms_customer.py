from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HmsCustomer(models.Model):
    _inherit = "res.partner"

    email = fields.Char()
    patient_id = fields.Many2one("hms.patient")
    related_patient_id = fields.Integer(related="patient_id.id")
    website = fields.Char()