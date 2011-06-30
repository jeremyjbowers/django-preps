from django.contrib import admin
from preps.apps.sports.tennis.models import Match

class MatchAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('home_player', 'away_player'), 'season', 'game_type', 'game_date_time')
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
                    'home_set_1_score', 'home_set_2_score', 'home_set_3_score', 'home_set_4_score', 
                    'home_set_5_score'
                ), 
                ('home_sets_won')
            ),
            'classes': ('scoreboard',),
        }),
        (None, {
            'fields': (
                (
                    'away_set_1_score', 'away_set_2_score', 'away_set_3_score', 'away_set_4_score', 
                    'away_set_5_score'
                ), 
                ('away_sets_won')
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

admin.site.register(Match, MatchAdmin)