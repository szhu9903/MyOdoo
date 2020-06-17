# -*- coding: utf-8 -*-
from odoo import fields,models,api,osv
import traceback,base64
from xlrd import open_workbook
from io import StringIO
from PIL import Image



class ZsjBlog(models.Model):
    _name = 'zsj.blog'
    _description = u'博客'
    _rec_name = 'zblog_title'
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = 'zblog_views asc'

    zblog_title = fields.Char('博文标题',track_visibility='onchange')
    zblog_brief = fields.Text('文章摘要',track_visibility='onchange')
    zblog_cover = fields.Char('文章封面url',track_visibility='onchange')
    zblog_data = fields.Binary('文章封面文件',track_visibility='onchange')
    zuser_id = fields.Many2one('zsj.blog.user',string='作者')
    zblog_type = fields.Many2one('zsj.blog.type',string='文章分类')
    zblog_content = fields.Html('博文内容',track_visibility='onchange')
    zblog_views = fields.Integer('浏览量')
    zblog_comment_count = fields.Integer('评论总数')
    zblog_like_count = fields.Integer('点赞数量')
    zcreate_date = fields.Datetime('发表时间')
    zdel_flag = fields.Integer('删除标志',default=0)
    zsta = fields.Float('a')
    zend = fields.Float('b')
    znum = fields.Float(compute='_compute_znum',store=True)   #store 是否实际存在数据库中

    color = fields.Integer('颜色')
    priority = fields.Selection([
        ('0','低'),
        ('1','中'),
        ('2','高')],
        '优先级',default='1')
    kanban_state = fields.Selection([
        ('normal','进行中'),
        ('blocked','挂起'),
        ('done','完成')],
    '看板状态',default='normal')


    @api.model
    def create(self, vals):
        zblog_data = vals.get('zblog_data')
        if zblog_data:
            img_data = base64.b64decode(zblog_data)
            with open('test.jpg', 'wb') as af:
                af.write(img_data)
                af.close()
        res = super(ZsjBlog,self).create(vals)
        return res


    def write(self, vals):
        zblog_data = vals.get('zblog_data')
        # if self.zblog_views <0:
        #     raise osv.except_osv(_(u'警告'),_(u'浏览量不小于0'))
        if zblog_data:
            img_data = base64.b64decode(zblog_data)
            with open('test.jpg', 'wb') as af:
                af.write(img_data)
                af.close()
        res = super(ZsjBlog,self).write(vals)
        return res




#图片文件读取
    def get_zblog_data(self):
        try:
            actives = self.browse(self.env.context.get('active_ids'))
            for record in actives and actives:
                bytes_data = record.zblog_data
                if bytes_data:
                    img_data = base64.b64decode(bytes_data)
                    with open('test.jpg','wb') as af:
                        af.write(img_data)
                        af.close()
        except:
            traceback.print_exc()

    #动态字段
    @api.depends('zsta','zend')
    def _compute_znum(self):
        for record in self:
            if record.zend == 0:
                record.znum = record.zsta
            else:
                record.znum = round(record.zsta/record.zend,2)

    @api.onchange('zblog_views')
    def _onchange_zblog_views(self):
        if self.zblog_views < 0:
            return {
                'warning':{
                    'title':'警告',
                    'message':'浏览量不能小于0'
                }
            }





