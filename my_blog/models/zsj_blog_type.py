
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


    def get_zsj_blog(self):
        sql = """
        select id from zsj_blog where zblog_type='%s'
        """%self.id
        self._cr.execute()
        res = self._cr_fetchall()
        blog_list = [blog_id[0] for blog_id in res]
        formview_ref = self.env.ref('my_blog.view_my_blog_form',False)
        treeview_ref = self.env.ref('my_blog.view_my_blog_tree',False)
        return {
            'name': '所有文章',
            'view_type': 'form',
            'view_model': 'form,tree',
            'res_model': 'zsj.blog',
            'domain':"[('zblog_type','in',%s)]"%blog_list,
            'views':[(treeview_ref and treeview_ref.id or False,'tree'),
                     (formview_ref and formview_ref.id or False,'form')],
            'type':'ir.actions.act_window',
            'target':'new'
        }