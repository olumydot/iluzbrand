"""
WSGI config for myshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import signal
import sys
import traceback
import time

from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)



