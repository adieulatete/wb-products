from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wb_products.settings')

app = Celery('wb_products')

# Loading configurations from Django settings, with the CELERY prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically find and register tasks in the tasks.py application
app.autodiscover_tasks()
