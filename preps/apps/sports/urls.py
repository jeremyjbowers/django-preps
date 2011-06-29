from django.conf.urls.defaults import *
from preps.apps.sports.views import PlayerDetail, SchoolDetail

urlpatterns = patterns('',
    url(r'^players/(?P<pk>[-\w]+)/(?P<player_slug>[-\w]+)/$', PlayerDetail.as_view(), name="player_detail"),
    url(r'^teams/(?P<pk>[-\w]+)/(?P<school_slug>[-\w]+)/$', SchoolDetail.as_view(), name="school_detail"),
)