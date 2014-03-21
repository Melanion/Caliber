from django.conf.urls import patterns, include, url
from django.contrib import admin

from vending import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'caliber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('vending.urls')),
    url(r'^rounds/', include('vending.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
