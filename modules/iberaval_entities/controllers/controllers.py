# from odoo import http


# class IberavalEntities(http.Controller):
#     @http.route('/iberaval_entities/iberaval_entities', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iberaval_entities/iberaval_entities/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('iberaval_entities.listing', {
#             'root': '/iberaval_entities/iberaval_entities',
#             'objects': http.request.env['iberaval_entities.iberaval_entities'].search([]),
#         })

#     @http.route('/iberaval_entities/iberaval_entities/objects/<model("iberaval_entities.iberaval_entities"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iberaval_entities.object', {
#             'object': obj
#         })

