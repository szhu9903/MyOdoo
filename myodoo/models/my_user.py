# -*- coding: utf-8 -*-
from odoo import fields,models,api
import hashlib
class Myuser(models.Model):
    _name = 'my.user'
    _description = u'用户'
    _rec_name = 'fname'
    _inherit = ['mail.thread']
    _order = 'fname asc'

    fname = fields.Char('用户姓名',track_visibility='onchange')


