from odoo import models, fields

class Students(models.Model):
        _name = "students.info"
        _description = "Estudiantes (Udemy)"
        
        nombre = fields.Char(string="Nombre del estudiante")
        edad = fields.Char(string="Edad")
        email = fields.Char(string="Email")