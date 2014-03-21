from django.conf.urls import patterns, url
from vending import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
        url(r'^(?P<round_id>\d+)/$', views.detail, name='detail'))
