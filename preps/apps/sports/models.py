from django.db import models
from django.core.templates import slugify
from preps.apps.models import ModelBase
import datetime

class Season(ModelBase):
    '''
    Represents a single sport season.
    '''
    school_year                     = models.IntegerField(max_length=4, help_text="Integer representing the year of the season, e.g., 2011.")
    start_date                      = models.DateField(blank=True, null=True, help_text="Start date for this season.")
    end_date                        = models.DateField(blank=True, null=True, help_text="End date for this season.")
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Season, self).save(*args, **kwargs)
        

class School(ModelBase):
    '''
    Represents a single school.
    '''
    name = models.CharField(max_length=255)
    address = models.TextField(default='', help_text="")
    local = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)

class BaseGame(ModelBase):
    season                          = models.ForeignKey(Season)
    game_date_time                  = models.DateTimeField(blank=True, null=True)
    week                            = models.IntegerField(max_length=2, default=0)
    home_team                       = models.ForeignKey(School, related_name="home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="away_team", null=True)
        
    class Meta:
        abstract=True    