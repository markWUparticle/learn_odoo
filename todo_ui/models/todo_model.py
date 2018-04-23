# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Tag(models.Model):
    _name='todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char('Name',40,translate=True)


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'

    # String fields:
    name = fields.Char('Name',40)
    desc = fields.Text('Description')
    state = fields.Selection([('draft','New'),('open','Started'),('done','Closed')],'State')
    desc = fields.Html('Documentation')

    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete',(3,2))

    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage','Stage')
    tag_ids = fields.Many2many('todo.task.tag',string='Tags')