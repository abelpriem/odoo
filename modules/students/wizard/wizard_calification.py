from odoo import models, fields
from odoo.exceptions import ValidationError

class WizardCalificaciones(models.TransientModel):
    _name = "wizard.calificaciones"
    _description = "Wizard Calificaciones (Udemy)"
    
    estudiante_id = fields.Many2one("students.info", string="Estudiante")
    acta = fields.Char(string="Acta")
    
    def aprobado(self):
        if not self.estudiante_id:
            raise ValidationError("No se ha seleccionado el estudiante")
        
        # Con el metodo .browse() hace la búsqueda el ORM
        student = self.env["students.info"].browse(self.estudiante_id.id)
        
        if student:
            student.esta_aprobado = True
            student.estado_calificacion = "aprobado"
            student.acta = self.acta
            
    def suspender(self):
        if not self.estudiante_id:
            raise ValidationError("No se ha seleccionado el estudiante")
        
        student = self.env["students.info"].browse(self.estudiante_id.id)
        
        if student:
            student.esta_aprobado = False
            student.estado_calificacion = "suspenso"
            student.acta = self.acta 