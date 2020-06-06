
from odoo import models,fields,api
import hashlib
class ZsjBlogUser(models.Model):
    _name = 'zsj.blog.user'
    _description = '用户'
    _rec_name = 'zuser_name'
    _inherit = ['mail.thread']
    _order = 'zaccount asc'

    zaccount = fields.Char('账号',track_visibility='onchange')
    zpwd = fields.Char('密码',track_visibility='onchange')
    zsex = fields.Selection([
        ('0','男'),
        ('1','女')],string ='性别', track_visibility='onchange')
    zphone = fields.Char('电话',track_visibility='onchange')
    zemail = fields.Char('邮箱',track_visibility='onchange')
    zgithub_token = fields.Char('GitHub',track_visibility='onchange')
    zuser_name = fields.Char('用户名称',track_visibility='onchange')
    zuser_photo = fields.Char('用户头像',track_visibility='onchange')
    zdel_flag = fields.Integer('删除标志', default=0)

    @api.model
    def create(self, vals):
        pwd = vals.get('zpwd')
        if pwd:
            hl = hashlib.md5(pwd.encode(encoding='utf-8'))
            vals['zpwd'] = hl.hexdigest()
        res =  super(ZsjBlogUser,self).create(vals)
        return res

    def write(self, vals):
        pwd = vals.get('zpwd')
        if pwd:
            hl = hashlib.md5(pwd.encode(encoding='utf-8'))
            vals['zpwd'] = hl.hexdigest()
        res = super(ZsjBlogUser,self).write(vals)
        return res