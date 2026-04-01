from odoo import models, fields
class Students(models.Model):
    _name = "students.info"
    _description = "Estudiantes (Udemy)"
    _rec_name = "estudiante_id"
        
    estudiante_id = fields.Many2one("res.partner", string="Estudiante", required=True)
    curso_id = fields.Many2one("cursos.students", string="Curso")
    esta_aprobado = fields.Boolean(string="¿Está aprobado?", default=False)
    comentarios = fields.Html(string="Comentarios")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    # calificacion = fields.Float(string="Calificación")
    calificaciones_ids = fields.One2many("students.calificaciones", "estudiante_id", string="Calificaciones")
    country_id = fields.Many2one("res.country", string="País", related='estudiante_id.country_id')
    tag_id = fields.Many2many("res.partner.category", string="Etiquetas")
    address = fields.Char(string="URL Google")
    estado_calificacion = fields.Selection(
        [
            ("suspenso","Suspenso"),
            ("aprobado","Aprobado")
        ]
    )
    
class Cursos(models.Model):
    _name = "cursos.students"
    _description = "Cursos (Udemy)"
    _rec_name = "nombre_curso"
    
    asignatura_ids = fields.Many2many("students.asignaturas", string="Asignaturas",)
    profesor_id = fields.Many2one("students.profesores", string="Tutor", required=True)
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
    
class Asignaturas(models.Model):
    _name = "students.asignaturas"
    _description = "Asignaturas (Udemy)"
    _rec_name = "nombre_asignatura"
    
    nombre_asignatura = fields.Char(string="Asignatura", required=True)
    
class Profesores(models.Model):
    _name = "students.profesores"
    _description = "Profesores (Udemy)"
    _rec_name = "nombre_profesor"
    
    nombre_profesor = fields.Many2one("res.partner", string="Profesor", required=True)
    
class Calificaciones(models.Model):
    _name = "students.calificaciones"
    _description = "Calificaciones (Udemy)"
    _rec_name = "calificacion"
    
    estudiante_id = fields.Many2one("students.info", string="Estudiante")
    asignatura_id = fields.Many2one("students.asignaturas", string="Asignatura")
    calificacion = fields.Float(string="Calificación")
    
