from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Students(models.Model):
    _name = "students.info"
    _description = "Estudiantes (Udemy)"
    _rec_name = "estudiante_id"
        
    estudiante_id = fields.Many2one("res.partner", string="Estudiante", required=True, domain=[("es_profesor", "=", False)])
    curso_id = fields.Many2one("cursos.students", string="Curso")
    esta_aprobado = fields.Boolean(string="¿Está aprobado?", default=False)
    comentarios = fields.Html(string="Comentarios")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    # calificacion = fields.Float(string="Calificación")
    calificaciones_ids = fields.One2many("students.calificaciones", "estudiante_id", string="Calificaciones")
    country_id = fields.Many2one("res.country", string="País", related='estudiante_id.country_id')
    tag_id = fields.Many2many("res.partner.category", string="Etiquetas")
    address = fields.Char(string="URL Google")
    acta = fields.Char(string="Acta")
    estado_calificacion = fields.Selection(
        [
            ("suspenso","Suspenso"),
            ("aprobado","Aprobado"),
            ("sin_calificar","Sin Calificar")
        ], default="sin_calificar"
    )
    
    # @api.model_create_multi 
    # def create(self, vals):
    #     """ Método de creación | Se le añaden validaciones para que, en caso de coincidir el estudiante_id
    #     no coincida con un estudiante_id que ya esté creado en la BD. """
        
    #     for val in vals:
    #         estudiante_id = val.get("estudiante_id")
    #         existe_estudiante = self.env["students.info"].search([("estudiante_id", "=", estudiante_id)], limit=1)
            
    #         if existe_estudiante:
    #             raise ValidationError("El estudiante ya está creado")
        
    #         res = super().create(vals)
    #         return res
    
    # def write(self, vals):
    #     """ Método de edición | Cuando editemos un contacto, comprobar que no se pueda cambiar de estudiante_id 
    #     por uno que ya esté creado en BD. """
    #     if "estudiante_id" in vals:
    #         estudiante_id = vals.get("estudiante_id")
    #         existe_estudiante = self.env["students.info"].search([("estudiante_id", "=", estudiante_id)], limit=1)
            
    #         if existe_estudiante:
    #             raise ValidationError("El estudiante ya está creado")
            
    #     return super().write(vals)
    
    @api.constrains("estudiante_id")
    def _check_estudiante_id(self):
        """ Método de validación mediante 'CONSTRAINS' | Se dispara ANTES de la consulta SQL pero DESPUÉS de las funciones create y write.   """
        for record in self:
            # Buscamos si hay OTROS registros con el mismo estudiante
            count = self.search_count([
                ("estudiante_id", "=", record.estudiante_id.id),  # .id porque es Many2one
                ("id", "!=", record.id) # Que no sea YO mismo
            ])
            
            if count > 0:
                raise ValidationError("El estudiante ya está creado")
    
    def unlink(self):
        """ Método de eliminación | Cuando eliminemos un contacto, comprobar previamente que el estudiante NO tenga un 
        curso asignado; si tiene curso, no se permite eliminar. """
        for record in self:
            if record.curso_id:
                raise ValidationError("Este estudiante ya está asignado a un curso y no se puede eliminar")
        
        return super().unlink()
    
    def copy(self, default=None):
        """ Método de duplicado | Directamente añadimos la validación de lanzar error para no permitir duplicar ningún
        estudiante ya creado, evitando así duplicidades. """
        raise ValidationError("No se puede duplicar registros")
    
    def aprobar(self):
        """ Método para aprobar (acta final) | Levanta un pop-up (wizard) tipo formulario, con la etiqueta "Aprobar" y llama al modelo de wizard.calificaciones,
        concretamente al método interno de aprobar. """
        return {
            "name": "Acta - Aprobar Estudiante",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref('students.wizard_view_aprobar_form').id,
            "res_model": "wizard.calificaciones",
            "target": "new",
            "context": {
                # Con default_variable : self.id elegimos por defecto el seleccionado
                "default_estudiante_id": self.id 
            }
        }
        
    def suspender(self):
        """ Método para suspender (acta final) | Levanta un pop-up (wizard) tipo formulario, con la etiqueta "Suspender" y llama al modelo de wizard.calificaciones,
        concretamente al método interno de suspender. """
        return {
            "name": "Acta - Suspender Estudiante",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref('students.wizard_view_suspender_form').id,
            "res_model": "wizard.calificaciones",
            "target": "new",
            "context": {
                # Con default_variable : self.id elegimos por defecto el seleccionado
                "default_estudiante_id": self.id 
            }
        }
    
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
    profesor_id = fields.Many2one("students.profesores", string="Profesor", required=True)
    
class Profesores(models.Model):
    _name = "students.profesores"
    _description = "Profesores (Udemy)"
    _rec_name = "profesor_id"
    
    profesor_id = fields.Many2one("res.partner", string="Profesor", required=True, domain=[("es_profesor", "=", True)])
    
class Calificaciones(models.Model):
    _name = "students.calificaciones"
    _description = "Calificaciones (Udemy)"
    _rec_name = "calificacion"
    
    estudiante_id = fields.Many2one("students.info", string="Estudiante")
    asignatura_id = fields.Many2one("students.asignaturas", string="Asignatura")
    profesor_id = fields.Many2one("students.profesores", string="Profesor", related="asignatura_id.profesor_id")
    calificacion = fields.Float(string="Calificación")
    
class ResPartner(models.Model):
    _inherit = "res.partner"
    
    es_profesor = fields.Boolean(string="¿Es profesor?", store=True)
    
