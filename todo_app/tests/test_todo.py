# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestTodo(TransactionCase):

    def setUp(self,*args,**kwargs):
        result = super(TestTodo,self).setUp(*args,**kwargs)
        user_demo = self.env.ref(user='base.user_demo')
        self.env = self.env(user=user_demo)
        return result

    def test_create(self):
        'Create a simple Todo'
        Todo = self.env['todo.task']
        task = Todo.create({'name':'Tesk Task'})
        self.asserEqual(task.is_done,False)

        task.do_toggle_done()
        self.asserTrue(task.is_done)

        Todo.do_clear_done()
        self.asserFalse(task.active)


    def test_record_rule(self):
        'Test per user record rules'
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name':'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name