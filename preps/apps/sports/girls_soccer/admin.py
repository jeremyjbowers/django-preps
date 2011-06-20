from django.contrib import admin
from preps.apps.sports.girls_soccer.models import *

class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('home_team', 'away_team'), 'season', 'game_type', 'game_date_time')
        }),
        ('Administration', {
            'fields': (('featured_game', 'conference_game'),)
        }),
        ('Location', {
            'fields': ('game_location', 'game_location_address', 'game_location_description')
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Scoreboard', {
            'fields': (
                ('home_h1_score', 'home_h2_score', 'home_ot_score'), 
                ('away_h1_score', 'away_h2_score', 'away_ot_score')
            ),
            'classes': ('scoreboard',),
        }),
    )

admin.site.register(Game, GameAdmin)
admin.site.register(TeamGame)
admin.site.register(TeamSeason)
admin.site.register(PlayerGame)
admin.site.register(PlayerSeason)
admin.site.register(Position)