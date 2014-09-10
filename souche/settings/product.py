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
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'souche',                      # Or path to database file if using sqlite3.
        'USER': 'pingjia',                      # Not used with sqlite3.
        'PASSWORD': 'hNMJU76Y',                  # Not used with sqlite3.
        'HOST': '192.168.206.212',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Use redis backend as default cache.
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            'PASSWORD': '',
        }
    },
    'file_cache': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'wwwcache',   # Set file cache directory
        'TIMEOUT': 61200, # 07-24 17 hours
        'OPTIONS': {
            'MAX_ENTRIES': 100000,
            'CULL_FREQUENCY': 3,
        }
    },
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

