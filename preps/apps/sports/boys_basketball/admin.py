from django.contrib import admin
from preps.apps.sports.boys_basketball.models import *

class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('home_team', 'away_team'), 'season', 'week', 'game_type', 'game_date_time')
        }),
        ('Administration', {
            'fields': (('game_of_the_week', 'featured_game', 'conference_game'),)
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Scoreboard', {
            'fields': (
                ('home_quarter_1_score', 'home_quarter_2_score', 'home_quarter_3_score', 'home_quarter_4_score'), 
                ('home_overtime_1_score', 'home_overtime_2_score', 'home_overtime_3_score'),
                ('home_total_score')
            ),
            'classes': ('scoreboard',),
        }),
        (None, {
            'fields': (
                ('away_quarter_1_score', 'away_quarter_2_score', 'away_quarter_3_score', 'away_quarter_4_score'), 
                ('away_overtime_1_score', 'away_overtime_2_score', 'away_overtime_3_score'), 
                ('away_total_score')
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