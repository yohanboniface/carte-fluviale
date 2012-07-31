from carte_fluviale.settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'carte_fluviale'
    }
}

WSGI_APPLICATION = 'carte_fluviale.wsgi.dev.application'
