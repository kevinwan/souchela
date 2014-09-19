# -*- coding; utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url

from souche.apps.carsource.views.car_source import SearchCarView
from souche.apps.carsource.views.car_source import CarSourceDetailView

from souche.apps.carsource.views.car_contrast import AddCarContrastView
from souche.apps.carsource.views.car_contrast import CarContrastDetailView
from souche.apps.carsource.views.car_contrast import CarContrastPreviewListView
from souche.apps.carsource.views.car_contrast import DeleteCarContrastView
from souche.apps.carsource.views.car_contrast import EmptyCarContrastView



urlpatterns = patterns('',
    url(r'^$', SearchCarView.as_view(), name='car_search'),
    url(r'^(?P<car_id>\d+)/$', CarSourceDetailView.as_view(), name='car_detail'),

    # Car contrast.
    url(r'^contrast/preview/$', CarContrastPreviewListView.as_view(), \
                name='car_contrast_preview'),
    url(r'^contrast/$', CarContrastDetailView.as_view(), \
                name='car_contrast_detail'),
    url(r'^contrast/add/$', AddCarContrastView.as_view(), \
                name='add_car_contrast'),
    url(r'^contrast/delete/$', DeleteCarContrastView.as_view(), \
                name='delete_car_contrast'),
    url(r'^contrast/empty/$', EmptyCarContrastView.as_view(), \
                name='empty_car_contrast'),
)
