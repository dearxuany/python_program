#! /bin/usr/env python3

import jinja2
import os

# tpl_path 指的是写有格式的html文件，**kwargs 指的是待渲染的多个输入
def render(tpl_path,**kwargs):
    path,filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                             ).get_template(filename).render(**kwargs)

