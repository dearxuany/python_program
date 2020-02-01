import jinja2
import os

def get_format(tplPath,**kwargs):
    path,filename = os.path.split(tplPath)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)
