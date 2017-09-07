"""
WSGI config for kontrola project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys




sys.path.append('/home/pi/django/kontrola')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/pi/django/kontrola/kontrolaenv/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kontrola.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
