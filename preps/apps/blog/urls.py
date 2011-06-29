from django.conf.urls.defaults import *
from preps.apps.blog.views import PostList, PostDetail

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name="post_list"),
    url(r'^(?P<pk>[-\w]+)/(?P<post_slug>[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
)