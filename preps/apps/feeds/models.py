from django.db import models

class FeedCollection(ModelBase):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['widget_name']
    
    def __unicode__(self):
        return self.widget_name
    
    def get_related_feeds(self):
        return Feed.objects.filter(widget__id=self.id)
    

class Feed(ModelBase):
    feed_collection = models.ForeignKey(FeedCollection)
    feed_name = models.CharField(max_length=255)
    feed_url = models.URLField(verify_exists=True)
    
    def __unicode__(self):
        return self.feed_name
    
    def get_related_feeditems(self):
        related = FeedItem.objects.filter(feed_name__id=self.id)
        return related
    
    def kill_old_feeditems(self):
        tombstones = []
        feeds = FeedItem.objects.filter(feed_name__id=self.id).filter(active=False)
        for item in feeds:
            tombstones.append('%s (%s) %s' % (r.feed_name, r.id, r.headline))
        feeds.delete()
        return tombstones
    

class FeedItem(ModelBase):
    feed_collection = models.ForeignKey(FeedCollection)
    feed = models.ForeignKey(Feed)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    story_link = models.URLField()
    publication_date = models.DateTimeField()
    
    def __unicode__(self):
        return "%s: %s" % (self.feed_name, self.headline)
    
    @property
    def get_pretty_date(self):
        return self.publication_date.strftime('%I:%M%p %x')