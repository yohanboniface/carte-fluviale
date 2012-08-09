from carte_fluviale.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'carte_fluviale',
        'PORT': '5433'
    }
}

WSGI_APPLICATION = 'carte_fluviale.wsgi.dev.application'
