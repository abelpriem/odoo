from odoo import models, fields

class Students(models.Model):
        _name = "students.info"
        _description = "Estudiantes (Udemy)"
        
        # nombre = fields.Char(string="Nombre del estudiante")
        # apellido = fields.Char(string="Apellidos")
        # edad = fields.Integer(string="Edad")
        # email = fields.Char(string="Email")
        
        estudiante_id = fields.Many2one("res.partner", string="Estudiante", required=True)

        # curso = fields.Char(string="Curso")
        curso_id = fields.Many2one("cursos.students", string="Curso")
        
        fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
        calificacion = fields.Float(string="Calificación")
        estado_calificacion = fields.Selection(
             [
                 {"suspenso","Suspenso"},
                 {"aprobado","Aprobado"},
                 {"notable","Notable"},
                 {"sobresaliente","Sobresaliente"}
             ]
        )
        esta_aprobado = fields.Boolean(string="¿Está aprobado?", default=False)
        comentarios = fields.Html(string="Comentarios")
        
class Cursos(models.Model):
    _name = "cursos.students"
    _description = "Cursos (Udemy)"
    
    nombre_curso = fields.Selection([
        ('primero_a', '1A'),
        ('primero_b', '1B'),
        ('segundo_a', '2A'),
        ('segundo_b', '2B'),
        ('tercero_a', '3A'),
        ('tercero_b', '3B'),
        ('cuarto_a', '4A'),
        ('cuarto_b', '4B')
    ], string="Curso")
    
    