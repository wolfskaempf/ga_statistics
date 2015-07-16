from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ga_statistics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # This file defines which view will be shown when the corresponding URL is requested.

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^statistics/$', 'stathandler.views.committee_list', name='committee_list'),
    url(r'^statistics/(?P<pk>\d+)/$', 'stathandler.views.committee_single', name='committee_single'),
    url(r'^submit/', 'stathandler.views.submit', name='submit'),
    url(r'^login/$', 'ga_auth.views.ga_login', name='login'),
    url(r'^logout/$', 'ga_auth.views.ga_logout', name='logout'),
    url(r'^about/$', 'web.views.about', name='about'),
]
