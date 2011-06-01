from django.db import models
from django.core.templates import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, BaseGame
from preps.apps.utils import functions as preps_utils
import datetime

class Team(ModelBase):
    '''
    Represents a single sport team. Ties a school to a sport.
    '''
    school                          = models.ForeignKey(School)
    sport                           = 'Football'
    
    def save(self, *args, **kwargs):
        self.slug                   = slugify(self.school.name)
        super(Team, self).save(*args, **kwargs)
    
    def get_schedule(self):
        '''
        Defines a function which returns games where this team is either the home or away team,
        ordered by week.
        '''
        return Game.objects.filter(Q(away_team=self) | Q(home_team=self)).order_by('week')
    
    # Defines a field "schedule" as a dynamic property of the get_schedule() function.
    schedule = property(get_schedule)

class Player(ModelBase):
    '''
    A representation of a HS football player.
    '''
    school                          = models.ForeignKey(School)
    first_name                      = models.CharField(max_length=255)
    last_name                       = models.CharField(max_length=255)
    middle_name                     = models.CharField(max_length=255, default='')
    height_feet                     = models.IntegerField(max_length=1, default=0)
    height_inches                   = models.IntegerField(max_length=1, default=0)
    weight_pounds                   = models.IntegerField(max_length=3, default=0)
    number                          = models.IntegerField(max_length=2, default=0)
    position                        = models.CharField(max_length=25, default='')
    
    def __unicode__(self):
        return self.first_name, self.middle_name, self.last_name
    
    def save(self, *args, **kwargs):
        self.slug                   = slugify(u'%s %s' %(self.first_name, self.last_name))
        super(Player, self).save(*args, **kwargs)
    

class Game(GameBase):
    '''
    A representation of a HS football game.
    '''
    home_team                       = models.ForeignKey(Team, related_name="home_team", null=True)
    away_team                       = models.ForeignKey(Team, related_name="away_team", null=True)
    home_q1_score                   = models.IntegerField(default=0)
    home_q2_score                   = models.IntegerField(default=0)
    home_q3_score                   = models.IntegerField(default=0)
    home_q4_score                   = models.IntegerField(default=0)
    home_ot1_score                  = models.IntegerField(default=0)
    home_ot2_score                  = models.IntegerField(default=0)
    home_ot3_score                  = models.IntegerField(default=0)
    home_total_score                = models.IntegerField(default=0)
    away_q1_score                   = models.IntegerField(default=0)
    away_q2_score                   = models.IntegerField(default=0)
    away_q3_score                   = models.IntegerField(default=0)
    away_q4_score                   = models.IntegerField(default=0)
    away_ot1_score                  = models.IntegerField(default=0)
    away_ot2_score                  = models.IntegerField(default=0)
    away_ot3_score                  = models.IntegerField(default=0)
    away_total_score                = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        name_string                 = u'Week %s %s at %s' % (self.week, self.away_team, self.home_team)
        self.slug                   = slugify(name_string)
        self.home_total_score   =   self.home_q1_score  +
                                    self.home_q2_score  +
                                    self.home_q3_score  +
                                    self.home_q4_score  +
                                    self.home_ot1_score +
                                    self.home_ot2_score +
                                    self.home_ot3_score
        self.away_total_score   =   self.away_q1_score  +
                                    self.away_q2_score  +
                                    self.away_q3_score  +
                                    self.away_q4_score  +
                                    self.away_ot1_score +
                                    self.away_ot2_score +
                                    self.away_ot3_score
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase):
    team                            = models.ForeignKey(Team)
    game                            = models.ForeignKey(Game)
    rushing_rushes                  = models.IntegerField(default=0)
    rushing_yards                   = models.IntegerField(default=0)
    rushing_touchdowns              = models.IntegerField(default=0)
    passing_attempts                = models.IntegerField(default=0)
    passing_completions             = models.IntegerField(default=0)
    passing_yards                   = models.IntegerField(default=0)
    passing_interceptions           = models.IntegerField(default=0)
    passing_touchdowns              = models.IntegerField(default=0)
    kicking_xp_attempts             = models.IntegerField(default=0)
    kicking_xp_made                 = models.IntegerField(default=0)
    kicking_fg_attempts             = models.IntegerField(default=0)
    kicking_fg_made                 = models.IntegerField(default=0)
    fumbles                         = models.IntegerField(default=0)
    defense_tackles                 = models.IntegerField(default=0)
    defense_sacks                   = models.IntegerField(default=0)
    defense_interceptions           = models.IntegerField(default=0)
    defense_fumbles_recovered       = models.IntegerField(default=0)
    defense_fumbles_forced          = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    

class TeamSeason(ModelBase):
    team                            = models.ForeignKey(Team)
    season                          = models.ForeignKey(Season)
    rushing_rushes                  = models.IntegerField(default=0)
    rushing_yards                   = models.IntegerField(default=0)
    rushing_touchdowns              = models.IntegerField(default=0)
    passing_attempts                = models.IntegerField(default=0)
    passing_completions             = models.IntegerField(default=0)
    passing_yards                   = models.IntegerField(default=0)
    passing_interceptions           = models.IntegerField(default=0)
    passing_touchdowns              = models.IntegerField(default=0)
    kicking_xp_attempts             = models.IntegerField(default=0)
    kicking_xp_made                 = models.IntegerField(default=0)
    kicking_fg_attempts             = models.IntegerField(default=0)
    kicking_fg_made                 = models.IntegerField(default=0)
    fumbles                         = models.IntegerField(default=0)
    defense_tackles                 = models.IntegerField(default=0)
    defense_sacks                   = models.IntegerField(default=0)
    defense_interceptions           = models.IntegerField(default=0)
    defense_fumbles_recovered       = models.IntegerField(default=0)
    defense_fumbles_forced          = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Season %s: %s stats (%s)' % (self.season.name, self.team, self.id)
    

class PlayerGame(ModelBase):
    player                          = models.ForeignKey(Player)
    game                            = models.ForeignKey(Game)
    rushing_rushes                  = models.IntegerField(default=0)
    rushing_yards                   = models.IntegerField(default=0)
    rushing_touchdowns              = models.IntegerField(default=0)
    passing_attempts                = models.IntegerField(default=0)
    passing_completions             = models.IntegerField(default=0)
    passing_yards                   = models.IntegerField(default=0)
    passing_interceptions           = models.IntegerField(default=0)
    passing_touchdowns              = models.IntegerField(default=0)
    receiving_receptions            = models.IntegerField(default=0)
    receiving_yards                 = models.IntegerField(default=0)
    receiving_touchdowns            = models.IntegerField(default=0)
    kicking_xp_attempts             = models.IntegerField(default=0)
    kicking_xp_made                 = models.IntegerField(default=0)
    kicking_fg_attempts             = models.IntegerField(default=0)
    kicking_fg_made                 = models.IntegerField(default=0)
    fumbles                         = models.IntegerField(default=0)
    defense_tackles                 = models.IntegerField(default=0)
    defense_sacks                   = models.IntegerField(default=0)
    defense_interceptions           = models.IntegerField(default=0)
    defense_fumbles_recovered       = models.IntegerField(default=0)
    defense_fumbles_forced          = models.IntegerField(default=0)
    rushing_yards_per_attempt       = models.FloatField(default=0.0)
    receiving_yards_per_reception   = models.FloatField(default=0.0)
    passing_yards_per_attempt       = models.FloatField(default=0.0)
    passing_completion_percentage   = models.FloatField(default=0.0)
    passing_rating                  = models.FloatField(default=0.0)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        self.rushing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.rushing_yards, self.rushing_attempts), 1))
        self.receiving_yards_per_reception  = float(floatformat(preps_utils.handle_percents(self.receiving_yards, self.receptions), 1))
        self.passing_completion_percentage  = float(floatformat(preps_utils.handle_percents(self.passing_completions, self.passing_attempts), 3))
        self.passing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.passing_yards, self.passing_attempts), 1))
        if self.passing_attempts == 0:
            self.passing_rating = 0.0
        else:
            self.passing_rating             = float(floatformat(handle_hss_passer_rating(
                self.passing_yards,
                self.passing_touchdowns,
                self.passing_completions,
                self.passing_interceptions,
                self.passing_attempts
            ), 1))
        super(PlayerGame, self).save(*args, **kwargs)
    
class PlayerSeason(ModelBase):
    player                          = models.ForeignKey(Player)
    season                          = models.ForeignKey(Season)
    rushing_rushes                  = models.IntegerField(default=0)
    rushing_yards                   = models.IntegerField(default=0)
    rushing_touchdowns              = models.IntegerField(default=0)
    passing_attempts                = models.IntegerField(default=0)
    passing_completions             = models.IntegerField(default=0)
    passing_yards                   = models.IntegerField(default=0)
    passing_interceptions           = models.IntegerField(default=0)
    passing_touchdowns              = models.IntegerField(default=0)
    receiving_receptions            = models.IntegerField(default=0)
    receiving_yards                 = models.IntegerField(default=0)
    receiving_touchdowns            = models.IntegerField(default=0)
    kicking_xp_attempts             = models.IntegerField(default=0)
    kicking_xp_made                 = models.IntegerField(default=0)
    kicking_fg_attempts             = models.IntegerField(default=0)
    kicking_fg_made                 = models.IntegerField(default=0)
    fumbles                         = models.IntegerField(default=0)
    defense_tackles                 = models.IntegerField(default=0)
    defense_sacks                   = models.IntegerField(default=0)
    defense_interceptions           = models.IntegerField(default=0)
    defense_fumbles_recovered       = models.IntegerField(default=0)
    defense_fumbles_forced          = models.IntegerField(default=0)
    rushing_yards_per_attempt       = models.FloatField(default=0.0)
    receiving_yards_per_reception   = models.FloatField(default=0.0)
    passing_yards_per_attempt       = models.FloatField(default=0.0)
    passing_completion_percentage   = models.FloatField(default=0.0)
    passing_rating                  = models.FloatField(default=0.0)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        self.rushing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.rushing_yards, self.rushing_attempts), 1))
        self.receiving_yards_per_reception  = float(floatformat(preps_utils.handle_percents(self.receiving_yards, self.receptions), 1))
        self.passing_completion_percentage  = float(floatformat(preps_utils.handle_percents(self.passing_completions, self.passing_attempts), 3))
        self.passing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.passing_yards, self.passing_attempts), 1))
        if self.passing_attempts == 0:
            self.passing_rating = 0.0
        else:
            self.passing_rating             = float(floatformat(handle_hss_passer_rating(
                self.passing_yards,
                self.passing_touchdowns,
                self.passing_completions,
                self.passing_interceptions,
                self.passing_attempts
            ), 1))
        super(PlayerSeason, self).save(*args, **kwargs)
    

def handle_hss_passer_rating(yds, tds, cmpls, ints, atts):
    '''
    Defines a function which computes NCAA passer rating.
    '''
    yards = 8.4 * yds
    touchdowns = 330 * tds
    completions = 100 * cmpls
    interceptions = 200 * ints
    rating = yards + touchdowns + completions - interceptions
    return floatformat(rating / atts)