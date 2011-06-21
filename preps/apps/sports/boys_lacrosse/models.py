import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Player, Sport, Conference
from preps.apps.utils import functions as preps_utils

class BoysLacrosseFields(models.Model):
    '''
    Represents statistics fields for Boys Lacrosse. Used like a mixin.
    '''
    lacrosse_goals                  = models.IntegerField(default=0, blank=True)
    lacrosse_assists                = models.IntegerField(default=0, blank=True)
    
    class Meta:
        abstract                    = True

class Position(ModelBase):
    '''
    Represents a single Boys Lacrosse position.
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
    Represents a single Boys Lacrosse game.
    '''
    home_team                       = models.ForeignKey(School, related_name="boys_lacrosse_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="boys_lacrosse_away_team", null=True)
    season                          = models.ForeignKey(Season, related_name="boys_lacrosse_game_season")
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
        return u'%s, week %s: %s at %s' % (self.season, self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
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
    

class TeamGame(GameBase, BoysLacrosseFields):
    '''
    Represents a single Boys Lacrosse team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="boys_lacrosse_teamgame_team",)
    game                            = models.ForeignKey(Game, related_name="boys_lacrosse_teamgame_game",)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(TeamGame, self).save(*args, **kwargs)
    

class TeamSeason(ModelBase, BoysLacrosseFields):
    '''
    Represents a single Boys Lacrosse team's performance in a single season.
    '''
    team                            = models.ForeignKey(School, related_name="boys_lacrosse_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="boys_lacrosse_teamseason_season")
    wins                            = models.IntegerField(default=0, blank=True)
    losses                          = models.IntegerField(default=0, blank=True)
    points_for                      = models.IntegerField(default=0, blank=True)
    points_against                  = models.IntegerField(default=0, blank=True)
    place                           = models.IntegerField(default=0, blank=True)
    conference                      = models.ForeignKey(Conference, related_name="boys_lacrosse_teamseason_conference")
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
    

class PlayerGame(ModelBase, BoysLacrosseFields):
    '''
    Represents a single Boys Lacrosse player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="boys_lacrosse_playergame_player")
    game                            = models.ForeignKey(Game, related_name="boys_lacrosse_playergame_game")
    lacrosse_points                 = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, BoysLacrosseFields):
    '''
    Represents a single Boys Lacrosse player's season performance.
    '''
    player                          = models.ForeignKey(Player, related_name="boys_lacrosse_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="boys_lacrosse_playerseason_season")
    position                        = models.ManyToManyField(Position, related_name="boys_lacrosse_playerseason_position")
    number                          = models.IntegerField(default=0, blank=True)
    lacrosse_games                  = models.IntegerField(default=0, blank=True)
    lacrosse_points                 = models.IntegerField(default=0, blank=True)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PlayerSeason, self).save(*args, **kwargs)
    
