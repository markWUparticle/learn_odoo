from odoo import models, fields,api

class Res_Car(models.Model):
    _name='res.car'
    _description='car'

    name = fields.Char(string='Numer')
    active = fields.Boolean('is ',default=False)
    data = fields.Date(string='date',default=fields.Date.context_today)
    data_order = fields.Datetime(string='longdate',default=fields.Date.context_today)
    image = fields.Binary('logo')
    discount = fields.Float(string='discount(%)',default=0.0)


