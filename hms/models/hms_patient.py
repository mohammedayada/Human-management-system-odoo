from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
class HMSPatient(models.Model):
    _name = "hms.patient"
    _rec_name = 'first_name'
    _sql_constraints = [("duplicate_email", "UNIQUE(email)", "The email you entered exist")]
    first_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B-', 'B-'),
            ('o-', 'o-'),
            ('o+', 'o+'),
        ]
    )
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer()
    department = fields.Many2one(comodel_name="hms.department")
    capacity = fields.Integer(related='department.capacity')
    doctor = fields.Many2many(comodel_name="hms.doctor")
    status = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    @api.onchange('age')
    def onchange_age(self):
        if self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': "PCR Checked",
                    'message': "you should set CR ratio ",
                }
            }

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail')

    #@api.onchange('birth_date')
    #def calculate_age(self):
     #   a = (date.today() - self.birth_date) // timedelta(days=365.2425)
      #  self['age'] = a


    #calculate age from birthday
    @api.onchange('birth_date')
    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                dt = str(rec.birth_date)
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                rec.age = rd.years
