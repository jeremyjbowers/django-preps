import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class SoftballFields(models.Model):
    '''
    Represents statistics fields for Softball. Used like a mixin.
    '''
    batting_at_bats                 = models.IntegerField(default=0, blank=True)
    batting_hits                    = models.IntegerField(default=0, blank=True)
    batting_doubles                 = models.IntegerField(default=0, blank=True)
    batting_triples                 = models.IntegerField(default=0, blank=True)
    batting_home_runs               = models.IntegerField(default=0, blank=True)
    batting_runs_scored             = models.IntegerField(default=0, blank=True)
    batting_runs_batted_in          = models.IntegerField(default=0, blank=True)
    batting_games                   = models.IntegerField(default=0, blank=True)
    batting_strikeouts              = models.IntegerField(default=0, blank=True)
    batting_walks                   = models.IntegerField(default=0, blank=True)
    pitching_games                  = models.IntegerField(default=0, blank=True)
    pitching_innings_pitched        = models.IntegerField(default=0, blank=True)
    pitching_strikeouts             = models.IntegerField(default=0, blank=True)
    pitching_walks                  = models.IntegerField(default=0, blank=True)
    pitching_hits                   = models.IntegerField(default=0, blank=True)
    pitching_home_runs              = models.IntegerField(default=0, blank=True)
    pitching_hits                   = models.IntegerField(default=0, blank=True)
    pitching_doubles                = models.IntegerField(default=0, blank=True)
    pitching_runs                   = models.IntegerField(default=0, blank=True)
    pitching_earned_runs            = models.IntegerField(default=0, blank=True)
    
    class Meta:
        abstract                    = True
    

class Position(ModelBase):
    '''
    Represents a single Softball position.
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
    A representation of a Softball game.
    '''
    season                          = models.ForeignKey(Season, related_name="softball_game_season")
    home_inning_1_score             = models.IntegerField(default=0, blank=True)
    home_inning_2_score             = models.IntegerField(default=0, blank=True)
    home_inning_3_score             = models.IntegerField(default=0, blank=True)
    home_inning_4_score             = models.IntegerField(default=0, blank=True)
    home_inning_5_score             = models.IntegerField(default=0, blank=True)
    home_inning_6_score             = models.IntegerField(default=0, blank=True)
    home_inning_7_score             = models.IntegerField(default=0, blank=True)
    home_inning_8_score             = models.IntegerField(default=0, blank=True)
    home_inning_9_score             = models.IntegerField(default=0, blank=True)
    away_inning_1_score             = models.IntegerField(default=0, blank=True)
    away_inning_2_score             = models.IntegerField(default=0, blank=True)
    away_inning_3_score             = models.IntegerField(default=0, blank=True)
    away_inning_4_score             = models.IntegerField(default=0, blank=True)
    away_inning_5_score             = models.IntegerField(default=0, blank=True)
    away_inning_6_score             = models.IntegerField(default=0, blank=True)
    away_inning_7_score             = models.IntegerField(default=0, blank=True)
    away_inning_8_score             = models.IntegerField(default=0, blank=True)
    away_inning_9_score             = models.IntegerField(default=0, blank=True)
    home_total_score                = models.IntegerField(default=0, blank=True)
    away_total_score                = models.IntegerField(default=0, blank=True)
    override_game_scores            = models.BooleanField(default=False)
    home_team                       = models.ForeignKey(School, related_name="softball_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="softball_away_team", null=True)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())            
        self.home_total_score   =   self.home_inning_1_score+\
                                    self.home_inning_2_score+\
                                    self.home_inning_3_score+\
                                    self.home_inning_4_score+\
                                    self.home_inning_5_score+\
                                    self.home_inning_6_score+\
                                    self.home_inning_7_score+\
                                    self.home_inning_8_score+\
                                    self.home_inning_9_score
        self.away_total_score   =   self.away_inning_1_score+\
                                    self.away_inning_2_score+\
                                    self.away_inning_3_score+\
                                    self.away_inning_4_score+\
                                    self.away_inning_5_score+\
                                    self.away_inning_6_score+\
                                    self.away_inning_7_score+\
                                    self.away_inning_8_score+\
                                    self.away_inning_9_score
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase, SoftballFields):
    '''
    Represents single Softball team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="softball_teamgame_team")
    game                            = models.ForeignKey(Game, related_name="softball_teamgame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(TeamSeason, self).save(*args, **kwargs)
    

class TeamSeason(ModelBase, SoftballFields):
    '''
    Represents a single Softball team's performance over a season.
    '''
    team                            = models.ForeignKey(School, related_name="softball_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="softball_teamseason_season")
    wins                            = models.IntegerField(default=0, blank=True)
    losses                          = models.IntegerField(default=0, blank=True)
    points_for                      = models.IntegerField(default=0, blank=True)
    points_against                  = models.IntegerField(default=0, blank=True)
    place                           = models.IntegerField(default=0, blank=True)
    conference                      = models.ForeignKey(Conference, related_name="softball_teamseason_conference")
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

class PlayerGame(GameBase, SoftballFields):
    '''
    Represents a single Softball player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="softball_playergame_player")
    game                            = models.ForeignKey(Game, related_name="softball_playergame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        super(PlayerGame, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, SoftballFields):
    '''
    Represents a single Softball player's performance over a single season.
    '''
    player                          = models.ForeignKey(Player, related_name="softball_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="softball_playerseason_season")
    position                        = models.ManyToManyField(Position, related_name="softball_playerseason_position")
    number                          = models.IntegerField(default=0, blank=True)
    games                           = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerSeason, self).save(*args, **kwargs)
    
