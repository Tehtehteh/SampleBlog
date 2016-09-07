from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'static': staticfiles_storage.url,
       'url': reverse,
    })
    env.filters['localtime'] = datetimeformat
    return env

def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)