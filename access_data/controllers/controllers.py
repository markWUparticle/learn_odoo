# -*- coding: utf-8 -*-
from odoo import http

# class TodoAccess(http.Controller):
#     @http.route('/todo_access/todo_access/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_access/todo_access/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_access.listing', {
#             'root': '/todo_access/todo_access',
#             'objects': http.request.env['todo_access.todo_access'].search([]),
#         })

#     @http.route('/todo_access/todo_access/objects/<model("todo_access.todo_access"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_access.object', {
#             'object': obj
#         })