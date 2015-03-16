from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', include('movies.urls')),
    url(r'^movies/', include('movies.urls'))
)