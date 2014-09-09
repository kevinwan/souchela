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


# Django south migration
INSTALLED_APPS += (
    'south',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'souche',                      # Or path to database file if using sqlite3.
        'USER': 'pingjia',                      # Not used with sqlite3.
        'PASSWORD': 'hNMJU76Y',                  # Not used with sqlite3.
        'HOST': '211.149.206.212',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}
