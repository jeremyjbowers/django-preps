from django.contrib import admin
from preps.apps.sports.football.models import *

class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('home_team', 'away_team'), 'season', 'week', 'game_type', 'game_date_time')
        }),
        ('Administration', {
            'fields': (('game_of_the_week', 'featured_game', 'conference_game'),)
        }),
        ('Location', {
            'fields': ('game_location', 'game_location_address', 'game_location_description')
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Scoreboard', {
            'fields': (
                ('home_q1_score', 'home_q2_score', 'home_q3_score', 'home_q4_score'), 
                ('home_ot1_score', 'home_ot2_score', 'home_ot3_score'),
                ('home_total_score')
            ),
            'classes': ('scoreboard',),
        }),
        ('Scoreboard', {
            'fields': (
                ('away_q1_score', 'away_q2_score', 'away_q3_score', 'away_q4_score'), 
                ('away_ot1_score', 'away_ot2_score', 'away_ot3_score'), 
                ('away_total_score')
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