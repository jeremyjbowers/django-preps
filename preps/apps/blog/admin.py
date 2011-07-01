from django.contrib import admin
from preps.apps.blog.models import Series, Link, Post, TopAthletes, TopTeams, RecruitingUpdate

class SeriesAdmin(admin.ModelAdmin):
    model = Series
    fieldsets = (
        (None, {'fields': ('name', 'active'), }),
    )
class LinkInline(admin.TabularInline):
    model = Link
    extra = 0
    allow_add = True
    fieldsets = (
        (None, {'fields': ('headline', 'link_url', 'active'), }),
    )

class TopAthletesInline(admin.TabularInline):
    model = TopAthletes
    # related_search_fields = {
    #     'player': ('player__first_name', 'player__last_name',),
    # }
    extra = 0
    allow_add = True
    fieldsets = (
        (None, {'fields': ('rank', 'player', 'blurb', 'active'), }),
    )
    

class TopTeamsInline(admin.TabularInline):
    model = TopTeams
    # related_search_fields = {
    #     'team': ('school__school',),
    # }
    extra = 0
    allow_add = True
    fieldsets = (
        (None, {'fields': ('rank', 'team', 'blurb', 'active'), }),
    )

class RecruitingUpdateInline(admin.TabularInline):
    model = RecruitingUpdate
    # related_search_fields = {
    #     'player': ('player__first_name', 'player__last_name',),
    # }
    extra = 0
    allow_add = True
    fieldsets = (
        (None, {'fields': ('commitment_rating', 'player', 'college', 'blurb', 'active'), }),
    )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'publication_date', 'author',)
    list_editable = ('active', 'publication_date',)
    search_fields = ('title', 'blurb', 'body',)
    filter_horizontal = ['players', 'teams']
    fieldsets = (
        ('Basics', {
            'fields': ('title', 'lead_image', 'blurb', 'body', 'active', 'publication_date', 'author',)
        }),
        ('Links', {
            'fields': ('series', 'players', 'teams')
        })
    )
    inlines = [
        LinkInline,
        RecruitingUpdateInline,
        TopTeamsInline,
        TopAthletesInline,
    ]

admin.site.register(TopAthletes)
admin.site.register(TopTeams)
admin.site.register(Post, PostAdmin)
admin.site.register(Series, SeriesAdmin)