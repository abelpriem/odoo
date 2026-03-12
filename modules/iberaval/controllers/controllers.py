# from odoo import http


# class Iberaval(http.Controller):
#     @http.route('/iberaval/iberaval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iberaval/iberaval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('iberaval.listing', {
#             'root': '/iberaval/iberaval',
#             'objects': http.request.env['iberaval.iberaval'].search([]),
#         })

#     @http.route('/iberaval/iberaval/objects/<model("iberaval.iberaval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iberaval.object', {
#             'object': obj
#         })

