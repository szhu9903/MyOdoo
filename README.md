# MyOdoo
My odoo13.0
初始化test

#store 是否同步更新数据库字段
znum = fields.Float(compute='_compute_znum',store=True)


@api.depends('字段','字段')
def _compute_znum():
    pass
