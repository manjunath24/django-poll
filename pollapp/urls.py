from django.conf.urls import patterns, include, url

from pollapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^(?P<poll_id>\d+)/$',
                           views.poll_details, name='details'),
                       url(r'^(?P<poll_id>\d+)/vote/$',
                           views.vote, name='vote'),)
