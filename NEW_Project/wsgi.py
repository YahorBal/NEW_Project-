"""
WSGI config for NEW_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
#
## assuming your django settings file is at '/home/YahorBal/mysite/mysite/settings.py'
## and your manage.py is is at '/home/YahorBal/mysite/manage.py'
path = '/home/YahorBal/NEW_Project-'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'NEW_Project.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
