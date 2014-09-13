"""
WSGI config for Mingqi_Personl_Website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mingqi_Personl_Website.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
