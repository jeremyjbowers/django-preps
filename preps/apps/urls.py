from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sports/', include('preps.apps.sports.urls')),
    url(r'^blog/', include('preps.apps.blog.urls')),
    url(r'^photo-gallery/', include('preps.apps.photos.urls')),
)