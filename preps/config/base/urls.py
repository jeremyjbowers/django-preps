from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^sports/high-schools/', include('preps.apps.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': preps.config.dev.settings.MEDIA_ROOT}),
)
