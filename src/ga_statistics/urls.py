from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ga_statistics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^statistics/', 'stathandler.views.statistics', name='statistics'),
    url(r'^submit/', 'stathandler.views.submit', name='submit'),
]
