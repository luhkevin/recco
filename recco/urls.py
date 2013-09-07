from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recco.views.home', name='home'),
    # url(r'^recco/', include('recco.foo.urls')),
    url(r'^login/$', 'auth.views.login_user'),

    url(r'^createaccount/$', 'createaccount.views.createaccount'),

    url(r'^home/', 'startpage.views.homepage'),

    url(r'^mymedia/', 'MyMedia.views.index'),

    url(r'^profiles/', include('profiles.urls')),

    url(r'^friends/', 'friends.views.index'),

    url(r'^totalrecommendations/', 'TotalRecommendations.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
