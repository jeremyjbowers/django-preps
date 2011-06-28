from django.contrib import admin
from preps.apps.home.models import SiteSection, PhotoBoxItem, TextBoxItem

class TextBoxItemAdmin(admin.ModelAdmin):
    list_display                    = ['headline', 'active', 'weight', 'position']
    list_editable                   = ['active', 'weight', 'position']
    filter_horizontal               = ['site_section',]
    fieldsets                       = (
        ('Basics', {
            'fields': (
                ('headline', 'show_headline'), 
                'body', 
                'photo', 
                'site_section', 
                ('weight', 'active'),
            )
        }),
    )

class SiteSectionAdmin(admin.ModelAdmin):
    list_display                    = ['name', 'weight']
    list_editable                   = ['weight']
    prepopulated_fields             = {'display_name': ('name',)}
    fieldsets                       = (('Basics', {'fields': ('name', 'display_name', ('weight', 'active'))}),)

admin.site.register(TextBoxItem, TextBoxItemAdmin)
admin.site.register(SiteSection, SiteSectionAdmin)
admin.site.register(PhotoBoxItem)