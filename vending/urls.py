from django.conf.urls import patterns, url
from vending.views import dispatcher

urlpatterns = patterns('', url(r'^$', dispatcher.index, name='index'),
        url(r'^(?P<round_id>\d+)/$', dispatcher.detail, name='detail'))
