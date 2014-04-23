from django.conf.urls import patterns, include, url
from django.contrib import admin

from vending.views import dispatcher

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('vending.urls')),
    url(r'^rounds/', include('vending.urls')),
    url(r'^round/(?P<round_id>\d+)/', dispatcher.round_details),
    url(r'^cartridge/(?P<cartridge_id>\d+)/', dispatcher.cartridge_details),
    url(r'^manufacturer/(?P<mfgr_id>\w+)/', dispatcher.manufacturer_details),
    url(r'^about$', dispatcher.about),
    url(r'^admin/', include(admin.site.urls)),
)
