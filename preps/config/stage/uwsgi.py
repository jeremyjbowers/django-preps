#! /usr/bin/env python
import sys
import os
import django.core.handlers.wsgi
sys.path.append('/data/django/django-preps/src/django-preps/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'preps.config.dev.settings'
application = django.core.handlers.wsgi.WSGIHandler()
