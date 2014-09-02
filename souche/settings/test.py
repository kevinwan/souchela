# -*- coding: utf-8 -*-

'''Configurations for souche in test environment.
'''

try:
    from souche.settings.product import *
except ImportError:
    pass

# Turn on DEBUG when on test environment
ALIVE_ON_PRODUCTION = False
DEBUG = not ALIVE_ON_PRODUCTION
TEMPLATE_DEBUG = DEBUG

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
