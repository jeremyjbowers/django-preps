from django.db import models
from django.core.templates import slugify
import datetime

class Season(models.Model):
    '''
    Represents a single Boys sport season.
    '''
    name = models.CharField(max_length=255, help_text="The name of the season, e.g., 2011 or 2011-2012."
    start_date = models.DateField(blank=True, null=True, help_text="Start date for this season.")
    end_date = models.DateField(blank=True, null=True, help_text="End date for this season.")
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Season, self).save(*args, **kwargs)
        
