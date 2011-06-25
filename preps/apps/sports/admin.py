from django.contrib import admin
from preps.apps.sports.models import *

class SeasonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': ('name', 'sport', 'active')
        }),
        ('Season duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )

class SportAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': ('name', 'gender', 'active')
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )    

class ConferenceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': ('name', 'sport', 'active')
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )    

class SchoolAdmin(admin.ModelAdmin):
    filter_horizontal = ('active_sports',)
    fieldsets = (
        ('Basic information', {
            'fields': (
                ('name', 'mascot', 'address', 'url'), 
                ('active_sports'),
                ('local', 'active'),
            )
        }),
        ('Logo', {
            'fields': ('use_custom_logo', 'logo_url')
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic information', {
            'fields': ('first_name', 'last_name', 'middle_name', 'school', 'active')
        }),
        ('Biographical information', {
            'fields': ('height_feet', 'height_inches', 'weight_pounds')
        }),
        ('Advanced', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Sport, SportAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(School, SchoolAdmin)