# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.exceptions import ValidationError

class prueba(models.Model):
    _name ='prueba'
    _description = "prueba"
    _order = "name"

    name=fields.Char('CI')
    permitido=fields.Boolean('Cuentas Permitidas')
    otro=fields.Char('Otro campo')
    edad=fields.Char('Edad')
    altura = fields.Char('Altura')
