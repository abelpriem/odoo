# from odoo import models, fields, api


# class iberaval_entities(models.Model):
#     _name = 'iberaval_entities.iberaval_entities'
#     _description = 'iberaval_entities.iberaval_entities'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

