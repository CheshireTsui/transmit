from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'transmit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
)
