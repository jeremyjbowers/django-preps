import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class BoysBasketballFields(models.Model):
    '''
    Represents statistics fields for BoysBasketball. Used like a mixin.
    '''
    basketball_shots                = models.IntegerField(default=0, blank=True)
    basketball_field_goals          = models.IntegerField(default=0, blank=True)
    basketball_three_pointers       = models.IntegerField(default=0, blank=True)
    basketball_rebounds             = models.IntegerField(default=0, blank=True)
    basketball_assists              = models.IntegerField(default=0, blank=True)
    basketball_steals               = models.IntegerField(default=0, blank=True)
    basketball_turnovers            = models.IntegerField(default=0, blank=True)
    basketball_minutes              = models.IntegerField(default=0, blank=True)
    
    class Meta:
        abstract                    = True

class Position(ModelBase):
    '''
    Represents a single Boys Basketball position.
    '''
    name                            = models.CharField(max_length=255)
    short_name                      = models.CharField(max_length=5, help_text="5 characters or fewer.")
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(Position, self).save(*args, **kwargs)
    

class Game(GameBase):
    '''
    A representation of a Boys Basketball game.
    '''
    home_team                       = models.ForeignKey(School, related_name="boys_basketball_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="boys_basketball_away_team", null=True)
    season                          = models.ForeignKey(Season, related_name="boys_basketball_game_season")
    home_q1_score                   = models.IntegerField(default=0, blank=True)
    home_q2_score                   = models.IntegerField(default=0, blank=True)
    home_q3_score                   = models.IntegerField(default=0, blank=True)
    home_q4_score                   = models.IntegerField(default=0, blank=True)
    home_ot1_score                  = models.IntegerField(default=0, blank=True)
    home_ot2_score                  = models.IntegerField(default=0, blank=True)
    home_ot3_score                  = models.IntegerField(default=0, blank=True)
    home_total_score                = models.IntegerField(default=0, blank=True)
    away_q1_score                   = models.IntegerField(default=0, blank=True)
    away_q2_score                   = models.IntegerField(default=0, blank=True)
    away_q3_score                   = models.IntegerField(default=0, blank=True)
    away_q4_score                   = models.IntegerField(default=0, blank=True)
    away_ot1_score                  = models.IntegerField(default=0, blank=True)
    away_ot2_score                  = models.IntegerField(default=0, blank=True)
    away_ot3_score                  = models.IntegerField(default=0, blank=True)
    away_total_score                = models.IntegerField(default=0, blank=True)
    week                            = models.IntegerField(max_length=2, default=0)
    game_of_the_week                = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        self.home_total_score   =   self.home_q1_score+\
                                    self.home_q2_score+\
                                    self.home_q3_score+\
                                    self.home_q4_score+\
                                    self.home_ot1_score+\
                                    self.home_ot2_score+\
                                    self.home_ot3_score
        self.away_total_score   =   self.away_q1_score+\
                                    self.away_q2_score+\
                                    self.away_q3_score+\
                                    self.away_q4_score+\
                                    self.away_ot1_score+\
                                    self.away_ot2_score+\
                                    self.away_ot3_score
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase, BoysBasketballFields):
    '''
    Represents single Boys Basketball team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="boys_basketball_teamgame_team")
    game                            = models.ForeignKey(Game, related_name="boys_basketball_teamgame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(TeamSeason, self).save(*args, **kwargs)
    

class TeamSeason(ModelBase, BoysBasketballFields):
    '''
    Represents a single Boys Basketball team's performance over a season.
    '''
    team                            = models.ForeignKey(School, related_name="boys_basketball_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="boys_basketball_teamseason_season")
    wins                            = models.IntegerField(default=0, blank=True)
    losses                          = models.IntegerField(default=0, blank=True)
    points_for                      = models.IntegerField(default=0, blank=True)
    points_against                  = models.IntegerField(default=0, blank=True)
    place                           = models.IntegerField(default=0, blank=True)
    conference                      = models.ForeignKey(Conference, related_name="boys_basketball_teamseason_conference")
    conference_wins                 = models.IntegerField(default=0, blank=True)
    conference_losses               = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Season %s: %s stats (%s)' % (self.season.name, self.team, self.id)
    
    def get_schedule(self):
        '''
        Defines a function which returns games where this team is either the home or away team,
        ordered by week.
        '''
        return Game.objects.filter(Q(away_team=self.team) | Q(home_team=self.team)).order_by('week')
        
    # Defines a field "schedule" as a dynamic property of the get_schedule() function.
    schedule = property(get_schedule)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(TeamSeason, self).save(*args, **kwargs)

class PlayerGame(GameBase, BoysBasketballFields):
    '''
    Represents a single Boys Basketball player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="boys_basketball_playergame_player")
    game                            = models.ForeignKey(Game, related_name="boys_basketball_playergame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, BoysBasketballFields):
    '''
    Represents a single Boys Basketball player's performance over a single season.
    '''
    player                          = models.ForeignKey(Player, related_name="boys_basketball_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="boys_basketball_playerseason_season")
    position                        = models.ManyToManyField(Position, related_name="boys_basketball_playerseason_position")
    number                          = models.IntegerField(default=0, blank=True)
    basketball_games                = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerSeason, self).save(*args, **kwargs)
    
