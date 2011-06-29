from django.conf.urls.defaults import *
from preps.apps.sports.views import PlayerDetail

urlpatterns = patterns('',
    url(r'^(?P<pk>[-\w]+)/(?P<player_slug>[-\w]+)/$', PlayerDetail.as_view(), name="player_detail"),
)