# -*- coding: utf-8 -*-

from odoo import models, fields, api


class merma(models.Model):
     _name = 'merma.merma'
     _description = 'merma.merma'

     primero = fields.Char()
     segundo = fields.Integer()
     tercero = fields.Float(compute="_value_pc", store=True)
     pais = fields.Many2one('res.country', String="Pais")
     productos = fields.Many2one('product.template', String="productos")
     vehiculos = fields.Many2one('fleet.vehicle.model', String="vehiculos")
     empleado = fields.Many2one('hr.employee', String="empleado")
     description = fields.Text()
     
@api.depends('value')
def _value_pc(self):
       for record in self:
           record.value = float(record.value) / 100
