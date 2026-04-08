from odoo.http import Controller, route, request, json
from odoo.exceptions import ValidationError
import json
import logging

# Para el uso/acceso de console.log() como en Nodejs
_logger = logging.getLogger(__name__)

class UserController(Controller):
    """ Controller | Es la parte del servidor de rutas. Importamos elementos como Controller, Route, Request o JSON del propio HTTP (Odoo)."""
    @route("/students", auth="user", type="http", methods=["GET"])
    def students(self):
        return request.make_response(
            json.dumps({"name": "PeterPan"})
        )
        
    @route('/new/students', auth='public', type='http', methods=['POST'], csrf=False)
    def _new_students(self, **kwargs):
        name = kwargs.get("name")
        
        return request.make_response(
            json.dumps({"name": name})
        )
        
    @route("/students/<int:id>", auth="public", type="http", methods=["GET"], csrf=False)
    def _get_student(self, id):
        try:
            student = request.env["students.info"].sudo().browse(id)
            if not student.exists():
                return self._response({'Error': 'Estudiante no encontrado'}, 404)
            
            result = {
                'id': student.id,
                'nombre': student.estudiante_id.name,
                'edad': getattr(student, 'edad', 'N/A'), # Evita error si el campo no existe
                'esta_aprobado': student.esta_aprobado
            }
            
            return self._response(result)
                
        except Exception as error:
            _logger.error({"Error en API:" , str(error)}, 500)
            return self._response({'Error': 'Error interno del servidor'}, 500)
        
    @route("/students/web", type="http", auth="public", csrf=False, website=True)
    def students_web(self):
        return request.render("students.view_students_web")
        
    def _response(self, data, status=200):
        """ Método auxiliar para estrucutar la respuesta JSON"""
        return request.make_response(
            json.dumps(data),
            status=status,
            headers={'Content-Type': 'application/json'}
        )