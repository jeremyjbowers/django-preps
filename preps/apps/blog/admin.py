from django.contrib import admin
from preps.apps.blog.models import *

# class PhotoInline(InlineAutocompleteAdmin):
#     model = Photo
#     related_search_fields = {
#         'photographer': ('first_name', 'last_name',),
#     }
#     extra = 0
#     allow_add = True
#     exclude = ('gallery', 'players', 'schools')

class TopAthletesInline(admin.TabularInline):
    model = TopAthletes
    # related_search_fields = {
    #     'player': ('player__first_name', 'player__last_name',),
    # }
    extra = 0
    allow_add = True

class TopTeamsInline(admin.TabularInline):
    model = TopTeams
    # related_search_fields = {
    #     'team': ('school__school',),
    # }
    extra = 0
    allow_add = True

class RecruitingUpdateInline(admin.TabularInline):
    model = RecruitingUpdate
    # related_search_fields = {
    #     'player': ('player__first_name', 'player__last_name',),
    # }
    extra = 0
    allow_add = True

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
            'fields': (('players', 'teams'), )
        })
    )
    inlines = [
        # PhotoInline,
        RecruitingUpdateInline,
        TopTeamsInline,
        TopAthletesInline,
    ]

# class RecruitingCollegeAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name', )}
# 
# 
# class RecruitingUpdateAdmin(FkAutocompleteAdmin):
#     model = RecruitingUpdate
#     filter_horizontal = ['college']
#     related_search_fields = {
#         'player': ('player__first_name', 'player__last_name',),
#     }

admin.site.register(TopAthletes)
admin.site.register(TopTeams)
# admin.site.register(RecruitingUpdate, RecruitingUpdateAdmin)
# admin.site.register(RecruitingCollege, RecruitingCollegeAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(County)