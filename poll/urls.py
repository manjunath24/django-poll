from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('common.urls')),
                       url(r'^poll/', include('pollapp.urls')),
                       url(r'^admin/', include(admin.site.urls)),)
