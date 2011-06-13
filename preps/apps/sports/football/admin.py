from django.contrib import admin
from preps.apps.sports.football.models import *

# class TeamFootballGameInline(InlineAutocompleteAdmin):
#     model = TeamFootballGame
#     max_num = 2
#     related_search_fields = {
#         'team': ('school__school', '#sport__sport=Football', '#season__season_start_date__year=2010'),
#     }
# 
# class IndividualFootballGameInline(InlineAutocompleteAdmin):
#     model = IndividualFootballGame
#     extra = 1
#     related_search_fields = {
#         'player': ('player__first_name', 'player__last_name', '#team__sport__sport=Football', '#team__season__season_start_date__year=2010'),
#     }
# 
# 
# class FootballGameAdmin(FkAutocompleteAdmin):
#     form = FootballGameForm
#     def queryset(self, request):
#         qs = super(FootballGameAdmin, self).queryset(request)
#         today = datetime.datetime.today()
#         s = Season.objects.filter(sport__sport="Football", season_start_date__lte=today, season_end_date__gte=today)
#         if s:
#             return qs.filter(season=s[0])
#         else:
#             return qs
#     date_hierarchy = 'game_date_and_time'
#     list_filter = ['game_date_and_time']
#     list_display = ['sport', 'visiting_team', 'home_team', 'game_date_and_time', 'final_score']
#     search_fields = ['visiting_team__school__school', 'home_team__school__school']
#     related_search_fields = {
#         'home_team': ('school__school', '#sport__sport=Football', '#season__season_start_date__year=2010'),
#         'visiting_team': ('school__school', '#sport__sport=Football', '#season__season_start_date__year=2010'),
#         'game_location': ('name',),
#     }
#     fieldsets = (
#         ('The Setup', {
#             'fields': ('game_type', 'season', 'sport')
#         }),
#         ('The Game', {
#             'fields': ('game_date_and_time', 'visiting_team', 'home_team', 'game_location')
#         }),
#         ('Game administration', {
#             'fields': ('game_of_the_week', 'featured_game', 'district_game', 'postponed', 'postponed_notes')
#         }),
#         ('The Scoreboard', {
#             'fields': ('visiting_first_quarter_score', 'visiting_second_quarter_score', 'visiting_third_quarter_score', 'visiting_fourth_quarter_score', 'visiting_overtime_quarter_score', 'visitor_final_score'),
#             'classes': ['scoreboard',],
#         }),
#         (None, {
#             'fields': ('home_first_quarter_score', 'home_second_quarter_score', 'home_third_quarter_score', 'home_fourth_quarter_score', 'home_overtime_quarter_score', 'home_final_score'),
#             'classes': ['scoreboard',],
#         }),
#         ('Final', {
#             'fields': ('final_score',)
#         }),
#     )
#     inlines = [
#       FootballScoringSummaryInline,
#       TeamFootballGameInline,
#       IndividualFootballGameInline,
#     ]

class GameAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': ('home_team', 'away_team', 'season', 'week', 'game_type', 'game_date_time')
        }),
        ('Administration', {
            'fields': ('game_of_the_week', 'featured_game', 'conference_game')
        }),
        ('Location', {
            'fields': ('game_location', 'game_location_address', 'game_location_description')
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Scoreboard', {
            'fields': ('home_q1_score', 'home_q2_score', 'home_q3_score', 'home_q4_score', 'home_ot1_score', 'home_ot2_score', 'home_ot3_score', 'home_total_score'),
            'classes': ('scoreboard',),
        }),
        (None, {
            'fields': ('away_q1_score', 'away_q2_score', 'away_q3_score', 'away_q4_score', 'away_ot1_score', 'away_ot2_score', 'away_ot3_score', 'away_total_score'),
            'classes': ('scoreboard',),
        }),
    )

admin.site.register(Game, GameAdmin)
admin.site.register(TeamGame)
admin.site.register(TeamSeason)
admin.site.register(PlayerGame)
admin.site.register(PlayerSeason)