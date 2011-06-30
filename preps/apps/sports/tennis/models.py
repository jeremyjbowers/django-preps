import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class Match(GameBase):
    '''
    A representation of a Tennis match.
    A Tennis match can be best of 3 or best of 5 sets.
    '''
    season                          = models.ForeignKey(Season, related_name="tennis_match_season")
    home_set_1_score                = models.IntegerField(default=0, blank=True)
    home_set_2_score                = models.IntegerField(default=0, blank=True)
    home_set_3_score                = models.IntegerField(default=0, blank=True)
    home_set_4_score                = models.IntegerField(default=0, blank=True)
    home_set_5_score                = models.IntegerField(default=0, blank=True)
    away_set_1_score                = models.IntegerField(default=0, blank=True)
    away_set_2_score                = models.IntegerField(default=0, blank=True)
    away_set_3_score                = models.IntegerField(default=0, blank=True)
    away_set_4_score                = models.IntegerField(default=0, blank=True)
    away_set_5_score                = models.IntegerField(default=0, blank=True)
    home_sets_won                   = models.IntegerField(default=0, blank=True)
    away_sets_won                   = models.IntegerField(default=0, blank=True)
    home_player                     = models.ForeignKey(Player, related_name="tennis_home_player", null=True)
    away_player                     = models.ForeignKey(Player, related_name="tennis_away_player", null=True)
    
    class Meta:
        verbose_name_plural = 'matches'
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        
        # Slugify!
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        
        # Set up a list of two-tuples representing home/away scores.
        games = [('home_set_%d_score', 'away_set_%d_score') % (idx, idx) for idx in range(1,5)]
        
        # Build a private function which can decide a winner by comparing scores.
        def _assign_win(home, away):
            if self.override_game_scores == True:
                return
            if home > away:
                self.home_sets_won += 1
            elif home < away:
                self.away_sets_won += 1
            
        # Use map to iterate over the list of two-tuples and decide a winner for each pair.
        map(_assign_win, games)
        
        # Super!
        super(Game, self).save(*args, **kwargs)
    
