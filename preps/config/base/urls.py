from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^sports/high-schools/', include('preps.apps.urls')),
)