from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns ('',

    url(r'^(?P<target>[a-zA-Z]+/$)', views.index, name='index'),

)
