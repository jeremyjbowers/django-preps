from django.db import models
from django.core.templates import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, BaseGame
import datetime

class Player(ModelBase):
    '''
    A representation of a HS football player.
    '''
    school                          = models.ForeignKey(School)
    first_name                      = models.CharField(max_length=255)
    last_name                       = models.CharField(max_length=255)
    middle_name                     = models.CharField(max_length=255, default='', help_text='This can be a full name, initial, or just left blank.')
    height_feet                     = models.IntegerField(max_length=1, default=0)
    height_inches                   = models.IntegerField(max_length=1, default=0)
    weight_pounds                   = models.IntegerField(max_length=3, default=0)
    number                          = models.IntegerField(max_length=2, default=0)
    position                        = models.CharField(max_length=25, default='')
    
    def __unicode__(self):
        return self.first_name, self.middle_name, self.last_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(u'%s %s' %(self.first_name, self.last_name))
        super(Player, self).save(*args, **kwargs)

class Game(BaseGame):
    '''
    A representation of a HS football game.
    '''
    home_q1_score                   = models.IntegerField(default=0)
    home_q2_score                   = models.IntegerField(default=0)
    home_q3_score                   = models.IntegerField(default=0)
    home_q4_score                   = models.IntegerField(default=0)
    home_ot_score                   = models.IntegerField(default=0)
    home_total_score                = models.IntegerField(default=0)
    away_q1_score                   = models.IntegerField(default=0)
    away_q2_score                   = models.IntegerField(default=0)
    away_q3_score                   = models.IntegerField(default=0)
    away_q4_score                   = models.IntegerField(default=0)
    away_ot_score                   = models.IntegerField(default=0)
    away_total_score                = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        name_string = u'Week %s %s at %s' % (self.week, self.away_team, self.home_team)
        self.slug = slugify(name_string)
        self.home_total_score = self.home_q1_score+self.home_q2_score+self.home_q3_score+self.home_q4_score
        self.away_total_score = self.away_q1_score+self.away_q2_score+self.away_q3_score+self.away_q4_score
        super(Game, self).save(*args, **kwargs)