# -*- coding: utf-8 -*-
import os, sys
from myapp.wsgi import application
sys.path.insert(0, '/var/www/u0932024/data/www/faq-reg.ru/project_name')
sys.path.insert(1, '/var/www/u0932024/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'edrop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()