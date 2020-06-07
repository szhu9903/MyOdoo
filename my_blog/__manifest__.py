# -*- coding: utf-8 -*-
{
    # 模块名称
    'name': "my_blog",
    #关键词
    'summary': "个人博客",
    #模块说明
    'description': "个人博客",
    #作者 网站
    'author': "ZSJ",
    'website': "https://www.zsjblog.com",
    #类别
    'category': 'Blog',
    'version': '0.1',

    # 本模块所依赖的模块，安装本模块会同时安装依赖的模块
    'depends': ['base','mail'],

    # 加载的处理文件，总是加载
    'data': [
        'views/zsj_blog.xml',
        'views/zsj_blog_user.xml',
        'views/zsj_blog_type.xml',
        'views/index.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}