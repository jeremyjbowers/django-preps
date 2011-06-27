from django.contrib import admin
from preps.apps.feeds.models import Feed, FeedCollection

class FeedInline(admin.TabularInline):
    model = Feed
    extra = 1

class FeedCollectionAdmin(admin.ModelAdmin):
    inlines = [
        FeedInline,
    ]

admin.site.register(FeedCollection, FeedCollectionAdmin)
admin.site.register(Feed)