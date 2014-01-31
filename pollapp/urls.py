from django.conf.urls import patterns, include, url

from pollapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.poll_details,name='details'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote,name='vote'),
)
