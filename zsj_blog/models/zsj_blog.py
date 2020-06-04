# -*- coding: utf-8 -*-
from odoo import fields,models,api

class ZsjBlog(models.Model):
    _name = 'zsj.blog'
    _description = u'博客'
    _rec_name = 'zblog_title'
    _inherit = ['mail.thread']
    _order = 'zblog_views asc'

    zblog_title = fields.Char('博文标题',track_visibility='onchange')
    zblog_brief = fields.Text('文章摘要',track_visibility='onchange')
    zblog_cover = fields.Char('文章封面',track_visibility='onchange')
    zuser_id = fields.Many2one('zsj.blog.user',string='作者')
    zblog_content = fields.Html('博文内容',track_visibility='onchange')
    zblog_views = fields.Integer('浏览量')
    zblog_comment_count = fields.Integer('评论总数')
    zblog_like_count = fields.Integer('点赞数量')
    zcreate_date = fields.Datetime('发表时间')
    zdel_flag = fields.Integer('删除标志',default=0)








