from django.conf.urls.defaults import patterns, include, url
from preps.config.dev.settings import MEDIA_ROOT

urlpatterns = patterns('',
    url(r'^sports/high-schools/', include('preps.apps.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
