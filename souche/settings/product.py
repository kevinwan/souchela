# -*- coding: utf-8 -*-

'''Configurations for souche in production environment.

All configurations, which is verified in local development environment, should
be synced here also.
'''

try:
    from souche.settings.default import *
except ImportError:
    pass

# Turn off DEBUG mode when on production server
ALIVE_ON_PRODUCTION = True
DEBUG = not ALIVE_ON_PRODUCTION
TEMPLATE_DEBUG = DEBUG

version_info = (0, 1, 0)
VERSION = '.'.join(map(str, version_info))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

####################
# Email Settings #
####################
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gongpingjia@gmail.com'
EMAIL_HOST_PASSWORD = 'Ki89ol.,'
DEFAULT_FROM_EMAIL = '公平价<gongpingjia@gmail.com>'

