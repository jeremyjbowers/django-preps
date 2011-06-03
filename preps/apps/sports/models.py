import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase

class Sport(ModelBase):
    GENDER_CHOICES = (
        (0, 'Boys'),
        (1, 'Girls'),
        (2, 'Coed'),        
    )
    name                            = models.CharField(max_length=255)
    gender                          = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)
    

class Conference(ModelBase):
    '''
    Represents a single conference.
    '''
    name                            = models.CharField(max_length=255)
    sport                           = models.ForeignKey(Sport)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Season, self).save(*args, **kwargs)
    

class Season(ModelBase):
    '''
    Represents a single sport season.
    '''
    name                            = models.IntegerField(max_length=4, help_text="Integer representing the year of the season, e.g., 2011.")
    start_date                      = models.DateField(blank=True, null=True, help_text="Start date for this season.")
    end_date                        = models.DateField(blank=True, null=True, help_text="End date for this season.")
    sport                           = models.ForeignKey(Sport)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(u'%s' % self.name)
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
    

class Player(ModelBase):
    '''
    A representation of a player.
    '''
    school                          = models.ForeignKey(School)
    first_name                      = models.CharField(max_length=255)
    last_name                       = models.CharField(max_length=255)
    middle_name                     = models.CharField(max_length=255, default='')
    height_feet                     = models.IntegerField(max_length=1, default=0)
    height_inches                   = models.IntegerField(max_length=1, default=0)
    weight_pounds                   = models.IntegerField(max_length=3, default=0)
    
    def __unicode__(self):
        return self.first_name, self.middle_name, self.last_name
    
    def save(self, *args, **kwargs):
        self.slug                   = slugify(u'%s %s' %(self.first_name, self.last_name))
        super(Player, self).save(*args, **kwargs)
    

class GameBase(ModelBase):
    game_date_time                  = models.DateTimeField(blank=True, null=True)
    week                            = models.IntegerField(max_length=2, default=0)
    STATUS_CHOICES = (
        (0, 'Pregame'),
        (1, 'In progress'),
        (2, 'Delayed'),
        (3, 'Postponed'),
        (9, 'Complete'),
    )
    status                          = models.IntegerField(max_length=1, choices=STATUS_CHOICES, default=0)
    status_description              = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract=True