from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ga_statistics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^statistics/$', 'stathandler.views.committee_list', name='statistics'),
    url(r'^statistics/(?P<pk>\d+)/$', 'stathandler.views.committee_single', name='statistics'),
    url(r'^submit/', 'stathandler.views.submit', name='submit'),
    url(r'^about$', 'web.views.about', name='about'),
]
