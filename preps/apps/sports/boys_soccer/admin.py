from django.contrib import admin
from preps.apps.sports.boys_soccer.models import *

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
                ('home_half_1_score', 'home_half_2_score', 'home_overtime_score'), 
                ('away_half_1_score', 'away_half_2_score', 'away_overtime_score')
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