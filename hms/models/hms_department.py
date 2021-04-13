from odoo import models, fields


class HMSDepartment(models.Model):
    _name = "hms.department"
    _rec_name = 'name'
    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients_ids = fields.One2many(comodel_name="hms.patient", inverse_name="department")
