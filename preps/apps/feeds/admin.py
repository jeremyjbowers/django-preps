from django.contrib import admin
from preps.apps.feeds.models import Feed, FeedCollection

class FeedInline(admin.TabularInline):
    model                           = Feed
    extra                           = 0
    fieldsets                       = ((None, {'fields': ('feed_name', 'feed_url', 'active')}),)

class FeedCollectionAdmin(admin.ModelAdmin):
    model                           = FeedCollection
    fieldsets                       = (('Basics', {'fields': ('name', 'active')}),)
    inlines                         = [FeedInline,]

admin.site.register(FeedCollection, FeedCollectionAdmin)
admin.site.register(Feed)