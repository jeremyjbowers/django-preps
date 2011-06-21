from django.contrib import admin
from preps.apps.sports.softball.models import *

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
                (
                    'home_inning_1_score', 'home_inning_2_score', 'home_inning_3_score', 'home_inning_4_score', 
                    'home_inning_5_score', 'home_inning_6_score', 'home_inning_7_score', 'home_inning_8_score',
                    'home_inning_9_score'
                ), 
                ('home_total_score')
            ),
            'classes': ('scoreboard',),
        }),
        ('Scoreboard', {
            'fields': (
                (
                    'away_inning_1_score', 'away_inning_2_score', 'away_inning_3_score', 'away_inning_4_score', 
                    'away_inning_5_score', 'away_inning_6_score', 'away_inning_7_score', 'away_inning_8_score',
                    'away_inning_9_score'
                ), 
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