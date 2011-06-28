from django.contrib import admin
from preps.apps.photos.models import Photo, PhotoGallery

class PhotoInline(admin.StackedInline):
    model                           = Photo
    extra                           = 0
    filter_horizontal               = ('players', 'teams')
    fieldsets                       = ((None, {'fields': (('caption', 'photo'), 'active', 'players', 'teams',)}),)

class PhotoGalleryAdmin(admin.ModelAdmin):
    model                           = PhotoGallery
    fieldsets                       = (('Basics', {'fields': ('headline', 'body', 'active')}),)
    inlines                         = [PhotoInline,]

admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Photo)