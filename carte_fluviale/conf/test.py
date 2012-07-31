from carte_fluviale.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
WSGI_APPLICATION = 'carte_fluviale.wsgi.test.application'
