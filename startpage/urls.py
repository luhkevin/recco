from django.conf.urls import patterns, url

from startpage import views

urlpatterns = patterns('', url(r'^$', views.index, name='index')
