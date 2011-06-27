#!/usr/bin/env python
import datetime, feedparser, os, string
from datetime import timedelta
from string import encode, decode
from BeautifulSoup import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify, urlize, striptags, escape
from preps.apps.feeds.models import FeedCollection, Feed, FeedItem

class Command(BaseCommand):
    args = '<none>'
    help = 'Updates RSS feed items.'
    
    def handle(self, *args, **options):
        '''
        Defines a function which fetches RSS feed items.
        '''
        
        # Get all of the feeds. 
        # I SAID ALL OF THEM, SMITHERS.
        feeds = Feed.objects.all()
        
        # Deactivate old feed items in preparation for replacing them with newer ones.
        if feeds.count() > 0:
            for feed in feeds:
                old_feed_items = feed.get_related_feeditems()
                for item in old_feed_items:
                    item.active=False
                    item.save()
        
        # Start the process of importing new feed items.
        try:
            # Using feedparser. It's lighter-weight than BeautifulSoup, but might bork on crappy feeds.
            # I'm importing BeautifulSoup above. Use it if you're getting lots of errors.
            parsed_feed = feedparser.parse(feed.feed_url)
            
            # Loop through the parsed feed.
            for entry in parsed_feed.entries:
                
                # The import fails here sometimes, but don't let this stop the feed engine.
                # Some items just fail to save; skip them and move on.
                try:
                    
                    # Get the collection.
                    collection = FeedCollection.objects.get(id=feed.feed_collection.id)
                    
                    # Construct our feed item.
                    f = FeedItem(
                        feed_collection=collection,
                        feed=feed,
                        headline=entry.title.encode('utf-8', 'replace'),
                        content=entry.description.encode('utf-8', 'replace'),
                        story_link=entry.link,
                        active=True,
                        publication_date=datetime.datetime(
                            entry.date_parsed[0], 
                            entry.date_parsed[1], 
                            entry.date_parsed[2], 
                            entry.date_parsed[3], 
                            entry.date_parsed[4], 
                            entry.date_parsed[5]
                        )-timedelta(hours=7)
                    )
                    
                    # SAVE!
                    f.save()
                    
                    # Be verbose, dammit.
                    print "Saved new item: %s: %s" % (f.story_link, f.headline)
                
                # If things aren't working for this feed item, just keep going.
                except:
                    if entry.link:
                        print "Oops, this item is broken: %s" % (entry.link)
                    else:
                        print "Oops, this item is so broken I can't print a link."
                    pass
            
            # Call a model method on this feed that deletes all of the inactive feed items.
            feed.kill_old_feeditems()
        
        # If the feed import process fails, mark all the old feeds as active so we're not left without content.
        except:
            
            # Loop through the old feed items.
            for item in old_feed_items:
                item.active=True
                item.save()
    