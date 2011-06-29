from django.conf.urls.defaults import *
from preps.apps.photos.views import GalleryList, GalleryDetail

urlpatterns = patterns('',
    url(r'^$', GalleryList.as_view(), name="gallery_list"),
    url(r'^(?P<pk>[-\w]+)/(?P<gallery_slug>[-\w]+)/$', GalleryDetail.as_view(), name="gallery_detail"),
)