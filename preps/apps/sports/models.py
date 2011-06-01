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
    name                            = models.CharField(max_length=255)
    address                         = models.TextField(default='')
    local                           = models.BooleanField(default=False)
    url                             = models.URLField(blank=True, null=True)
    mascot                          = models.CharField(max_length=255, blank=True, null=True)
    boys_baseball                   = models.BooleanField(default=False)
    boys_crosscountry               = models.BooleanField(default=False)
    boys_golf                       = models.BooleanField(default=False)
    boys_rugby                      = models.BooleanField(default=False)
    boys_swimming                   = models.BooleanField(default=False)
    boys_track                      = models.BooleanField(default=False)
    boys_wrestling                  = models.BooleanField(default=False)
    boys_badminton                  = models.BooleanField(default=False)
    boys_basketball                 = models.BooleanField(default=False)
    boys_football                   = models.BooleanField(default=False)
    boys_lacrosse                   = models.BooleanField(default=False)
    boys_soccer                     = models.BooleanField(default=False)
    boys_tennis                     = models.BooleanField(default=False)
    boys_waterpolo                  = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(School, self).save(*args, **kwargs)

class GameBase(ModelBase):
    season                          = models.ForeignKey(Season)
    game_date_time                  = models.DateTimeField(blank=True, null=True)
    week                            = models.IntegerField(max_length=2, default=0)
    
    status                          = models.CharField(max_length=255, choices=STATUS_CHOICES, default='')
    
    class Meta:
        abstract=True