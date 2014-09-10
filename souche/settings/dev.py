# -*- coding: utf-8 -*-

'''Configurations for souche in development environment.
'''

try:
    from souche.settings.test import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'souche',                      # Or path to database file if using sqlite3.
        'USER': 'zhangzupeng',                      # Not used with sqlite3.
        'PASSWORD': 'zhangzupeng',                  # Not used with sqlite3.
        'HOST': '192.168.1.245',                      # Set to empty string for localhost. Not used with sqlite3.
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
        'LOCATION': 'wwwcache',  # Set file cache directory
        'TIMEOUT': 61200, # 07-24 17 hours
        'OPTIONS': {
            'MAX_ENTRIES': 100000,
            'CULL_FREQUENCY': 3,
        }
    },
}

# Django debug toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1', )

# Override some settings in local_settings
try:
    from souche.settings.local_settings import *
except:
    pass
