# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from souche.apps.core.views import IndexView
from souche.apps.core.views import SearchCarView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^souche/', include('souche.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'search-car/', SearchCarView.as_view(), name='search_car'),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
