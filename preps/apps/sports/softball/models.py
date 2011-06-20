import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class BaseballFields(models.Model):
    '''
    Represents statistics fields for Baseball. Used like a mixin.
    '''
    batting_at_bats                 = models.IntegerField(default=0)
    batting_hits                    = models.IntegerField(default=0)
    batting_doubles                 = models.IntegerField(default=0)
    batting_triples                 = models.IntegerField(default=0)
    batting_home_runs               = models.IntegerField(default=0)
    batting_runs_scored             = models.IntegerField(default=0)
    batting_runs_batted_in          = models.IntegerField(default=0)
    batting_games                   = models.IntegerField(default=0)
    batting_strikeouts              = models.IntegerField(default=0)
    batting_walks                   = models.IntegerField(default=0)
    pitching_games                  = models.IntegerField(default=0)
    pitching_innings_pitched        = models.IntegerField(default=0)
    pitching_strikeouts             = models.IntegerField(default=0)
    pitching_walks                  = models.IntegerField(default=0)
    pitching_hits                   = models.IntegerField(default=0)
    pitching_home_runs              = models.IntegerField(default=0)
    pitching_hits                   = models.IntegerField(default=0)
    pitching_doubles                = models.IntegerField(default=0)
    pitching_runs                   = models.IntegerField(default=0)
    pitching_earned_runs            = models.IntegerField(default=0)
    
    class Meta:
        abstract                    = True
    

class Position(ModelBase):
    '''
    Represents a single Baseball position.
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
    A representation of a Baseball game.
    '''
    season                          = models.ForeignKey(Season, related_name="baseball_game_season")
    home_h1_score                   = models.IntegerField(default=0)
    home_h2_score                   = models.IntegerField(default=0)
    home_ot_score                   = models.IntegerField(default=0)
    away_h1_score                   = models.IntegerField(default=0)
    away_h2_score                   = models.IntegerField(default=0)
    away_ot_score                   = models.IntegerField(default=0)
    override_game_scores            = models.BooleanField(default=False)
    home_team                       = models.ForeignKey(School, related_name="baseball_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="baseball_away_team", null=True)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase, BaseballFields):
    '''
    Represents single Baseball team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="baseball_teamgame_team")
    game                            = models.ForeignKey(Game, related_name="baseball_teamgame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(TeamSeason, self).save(*args, **kwargs)
    

class TeamSeason(ModelBase, BaseballFields):
    '''
    Represents a single Baseball team's performance over a season.
    '''
    team                            = models.ForeignKey(School, related_name="baseball_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="baseball_teamseason_season")
    wins                            = models.IntegerField(default=0)
    losses                          = models.IntegerField(default=0)
    points_for                      = models.IntegerField(default=0)
    points_against                  = models.IntegerField(default=0)
    place                           = models.IntegerField(default=0)
    conference                      = models.ForeignKey(Conference, related_name="baseball_teamseason_conference")
    conference_wins                 = models.IntegerField(default=0)
    conference_losses               = models.IntegerField(default=0)
    
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

class PlayerGame(GameBase, BaseballFields):
    '''
    Represents a single Baseball player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="baseball_playergame_player")
    game                            = models.ForeignKey(Game, related_name="baseball_playergame_game")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        super(PlayerGame, self).save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, BaseballFields):
    '''
    Represents a single Baseball player's performance over a single season.
    '''
    player                          = models.ForeignKey(Player, related_name="baseball_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="baseball_playerseason_season")
    position                        = models.ForeignKey(Position, related_name="baseball_playerseason_position")
    number                          = models.IntegerField(blank=True, null=True)
    games                           = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug               = slugify(self.__unicode__())
        super(PlayerSeason, self).save(*args, **kwargs)
    
