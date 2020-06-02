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
    fuser_code = fields.Char('账号',track_visibility='onchange')
    fuser_pwd = fields.Char('密码',track_visibility='onchange')
    fdel_flag = fields.Integer('删除标志',default=0)

    @api.model
    def create(self, vals):
        pwd = vals.get('fuser_pwd')
        if pwd:
            hl = hashlib.md5(pwd.encode(encoding='utf-8'))
            vals['fuser_pwd'] = hl.hexdigest()
        res = super(Myuser,self).create(vals)
        return res

    def write(self, vals):
        pwd = vals.get('fuser_pwd') or ''
        if pwd:
            hl = hashlib.md5(pwd.encode(encoding='utf-8'))
            vals['fuser_pwd'] = hl.hexdigest()
        result = super(Myuser,self).write(vals)
        return result






