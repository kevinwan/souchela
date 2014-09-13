# -*- coding; utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url

from souche.apps.carsource.views import SearchCarView
from souche.apps.carsource.views import CarSourceDetailView



urlpatterns = patterns('',
    url(r'^$', SearchCarView.as_view(), name='car_search'),
    url(r'^(?P<car_id>\d+)/$', CarSourceDetailView.as_view(), name='car_detail'),
)
