from django.contrib import admin
from preps.apps.sports.volleyball.models import *

class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('home_team', 'away_team'), 'season', 'game_type', 'game_date_time')
        }),
        ('Administration', {
            'fields': (('featured_game', 'conference_game'),)
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Scoreboard', {
            'fields': (
                (
                    'home_game_1_score', 'home_game_2_score', 'home_game_3_score', 'home_game_4_score', 
                    'home_game_5_score'
                ), 
                ('home_games_won')
            ),
            'classes': ('scoreboard',),
        }),
        (None, {
            'fields': (
                (
                    'away_game_1_score', 'away_game_2_score', 'away_game_3_score', 'away_game_4_score', 
                    'away_game_5_score'
                ), 
                ('away_games_won')
            ),
            'classes': ('scoreboard',),
        }),
        ('Location', {
            'fields': ('game_location', 'game_location_address', 'game_location_description'),
            'classes': ('collapse',),
        }),
        ('Summary', {
            'fields': ('game_result_headline', 'game_result_summary'),
            'classes': ('scoreboard', 'collapse'),
        })
    )

admin.site.register(Game, GameAdmin)
admin.site.register(TeamGame)
admin.site.register(TeamSeason)
admin.site.register(PlayerGame)
admin.site.register(PlayerSeason)
admin.site.register(Position)