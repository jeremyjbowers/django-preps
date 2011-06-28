from django.contrib import admin
from preps.apps.sports.swimming.models import Meet

class MeetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': (('meet_type', 'meet_date_time'), ('teams', 'season'))
        }),
        ('Administration', {
            'fields': (('featured_meet', 'conference_meet'),)
        }),
        ('Status', {
            'fields': ('status', 'status_description')
        }),
        ('Location', {
            'fields': ('meet_location', 'meet_location_address', 'meet_location_description'),
            'classes': ('collapse',),
        }),
        ('Summary', {
            'fields': ('meet_result_headline', 'meet_result_summary'),
            'classes': ('scoreboard', 'collapse'),
        })
    )

admin.site.register(Meet, MeetAdmin)