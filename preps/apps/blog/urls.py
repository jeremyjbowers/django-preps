from django.conf.urls.defaults import *
from preps.apps.blog.views import PostList, PostDetail, PostListBySeries

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name="post_list"),
    url(r'^series/(?P<pk>[-\w]+)/(?P<series_slug>[-\w]+)/$', PostListBySeries.as_view(), name="post_list_series"),
    url(r'^post/(?P<pk>[-\w]+)/(?P<post_slug>[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
)