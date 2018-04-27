from odoo import api,models,fields
from odoo.exceptions import ValidationError


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char(string='Name',size=40, translate=True)

    task_ids = fields.Many2many('todo.task',string='Tasks')

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'

    name = fields.Char('Name')
    desc = fields.Text('Description')
    state = fields.Selection([('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], 'State')

    docs = fields.Html('Documentation')
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Date('Last Changed')

    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    tasks = fields.One2many('todo.task', 'stage_id', 'Tasks in this stage')

class TodoTask(models.Model):
    _inherit = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')

    tag_ids = fields.Many2many(
            comodel_name='todo.task.tag',
            relation='todo_task_tag_rel',
            column1='task_id',
            column2='tag_id',
            string='Tags')

    refers_to = fields.Reference([('res.user', 'User'), ('res.partner', 'Partner')], 'Refers to')

    stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold', )

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold',
                                search='_search_stage_fold',
                                inverse='_write_stage_fold'
                                )

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    stage_state = fields.Selection(related='stage_id.state', string='Stage State',store=True, inverse='_write_state')


    _sql_constraints = [(
        'todo_task_name_uniq','UNIQUE(name,active)','Task title must be unique!')]

    @api.constrains('name')
    def _check_name_size(self):
        for task in self:
            if len(task.name)< 5:
                raise ValidationError('Must have 5 chars!')

    def compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])

    user_todo_count = fields.Integer('User To-Do Count', compute='compute_user_todo_count')

    effort_estimate = fields.Integer('effort estimate')
