
from odoo import models,fields

class ZsjBlogType(models.Model):
    _name = 'zsj.blog.type'
    _description = u'文章分类'
    _rec_name = 'ztype_name'
    _inherit = ['mail.thread']
    _order = 'zblog_count'

    ztype_name = fields.Char('分类名称',track_visibility='onchange')
    zblog_count = fields.Integer('文章数量',track_visibility='onchange')
    zup_type = fields.Many2one('zsj.blog.type','上级分类')
    zcreate_by = fields.Many2one('zsj.blog.user','创建人')
    zdel_flag = fields.Integer('删除标志',default=0)

