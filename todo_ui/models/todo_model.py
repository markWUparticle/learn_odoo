# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Tag(models.Model):
    _name='todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char('Name',40,translate = True)