from django.conf.urls import patterns, url
from vending import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))
