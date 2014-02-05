from django.conf.urls import patterns, include, url

from pollapp import views

urlpatterns = patterns('',
                       url(r'^(?P<poll_id>\d+)/$',
                           views.poll_details, name='details'),
                       url(r'^(?P<poll_id>\d+)/vote/$',
                           views.vote, name='vote'),)
