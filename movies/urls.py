from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'movies.views.home', name='home'),
    url(r'^get/(?P<start>\d{1,2})/(?P<count>\d{1,2})/(?P<xres>\d{2,4})/(?P<yres>\d{2,4})/$', 'movies.views.get', name='get')
)