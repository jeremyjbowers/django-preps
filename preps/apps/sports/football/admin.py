from django.contrib import admin
from preps.apps.sports.football.models import *

admin.site.register(Game)
admin.site.register(TeamGame)
admin.site.register(TeamSeason)
admin.site.register(PlayerGame)
admin.site.register(PlayerSeason)