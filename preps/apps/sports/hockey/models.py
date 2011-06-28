import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Player, Sport, Conference
from preps.apps.utils import functions as preps_utils

class HockeyFields(models.Model):
    '''
    Represents statistics fields for Hockey. Used like a mixin.
    '''
    hockey_goals                    = models.IntegerField(default=0, blank=True)
    hockey_assists                  = models.IntegerField(default=0, blank=True)
    
    class Meta:
        abstract                    = True

class Position(ModelBase):
    '''
    Represents a single Hockey position.
    '''
    name                            = models.CharField(max_length=255)
    short_name                      = models.CharField(max_length=5, help_text="5 characters or fewer.")
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(Position, self).save(*args, **kwargs)
    

class Game(GameBase):
    '''
    Represents a single Hockey game.
    '''
    home_team                       = models.ForeignKey(School, related_name="hockey_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="hockey_away_team", null=True)
    season                          = models.ForeignKey(Season, related_name="hockey_game_season")
    home_period_1_score             = models.IntegerField(default=0, blank=True)
    home_period_2_score             = models.IntegerField(default=0, blank=True)
    home_period_3_score             = models.IntegerField(default=0, blank=True)
    home_total_score                = models.IntegerField(default=0, blank=True)
    away_period_1_score             = models.IntegerField(default=0, blank=True)
    away_period_2_score             = models.IntegerField(default=0, blank=True)
    away_period_3_score             = models.IntegerField(default=0, blank=True)
    away_total_score                = models.IntegerField(default=0, blank=True)
    week                            = models.IntegerField(max_length=2, default=0)
    game_of_the_week                = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s, week %s: %s at %s' % (self.season, self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        self.home_total_score   =   self.home_period_1_score+\
                                    self.home_period_2_score+\
                                    self.home_period_3_score
        self.away_total_score   =   self.away_period_1_score+\
                                    self.away_period_2_score+\
                                    self.away_period_3_score
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase, HockeyFields):
    '''
    Represents a single Hockey team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="hockey_teamgame_team",)
    game                            = models.ForeignKey(Game, related_name="hockey_teamgame_game",)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(TeamGame, self).save(*args, **kwargs)
    

class TeamSeason(ModelBase, HockeyFields):
    '''
    Represents a single Hockey team's performance in a single season.
    '''
    team                            = models.ForeignKey(School, related_name="hockey_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="hockey_teamseason_season")
    wins                            = models.IntegerField(default=0, blank=True)
    losses                          = models.IntegerField(default=0, blank=True)
    points_for                      = models.IntegerField(default=0, blank=True)
    points_against                  = models.IntegerField(default=0, blank=True)
    place                           = models.IntegerField(default=0, blank=True)
    conference                      = models.ForeignKey(Conference, related_name="hockey_teamseason_conference")
    conference_wins                 = models.IntegerField(default=0, blank=True)
    conference_losses               = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Season %s: %s stats (%s)' % (self.season.name, self.team, self.id)
    
    def get_schedule(self):
        '''
        Defines a function which returns games where this team is either the home or away team,
        ordered by week.
        '''
        return Game.objects.filter(Q(away_team=self) | Q(home_team=self)).order_by('week')

    # Defines a field "schedule" as a dynamic property of the get_schedule() function.
    schedule = property(get_schedule)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(TeamSeason, self).save(*args, **kwargs)
    

class PlayerGame(ModelBase, HockeyFields):
    '''
    Represents a single Hockey player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="hockey_playergame_player")
    game                            = models.ForeignKey(Game, related_name="hockey_playergame_game")
    hockey_points                   = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, HockeyFields):
    '''
    Represents a single Hockey player's season performance.
    '''
    player                          = models.ForeignKey(Player, related_name="hockey_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="hockey_playerseason_season")
    position                        = models.ManyToManyField(Position, related_name="hockey_playerseason_position")
    number                          = models.IntegerField(default=0, blank=True)
    hockey_games                    = models.IntegerField(default=0, blank=True)
    hockey_points                   = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PlayerSeason, self).save(*args, **kwargs)
    
