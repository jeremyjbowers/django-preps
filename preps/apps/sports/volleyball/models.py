import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, GameBase, Sport, Player, Conference
from preps.apps.utils import functions as preps_utils

class VolleyballFields(models.Model):
    '''
    A representation of stats fields for Volleyball.
    '''
    volleyball_games                = models.IntegerField(default=0)
    volleyball_aces                 = models.IntegerField(default=0)
    volleyball_assists              = models.IntegerField(default=0)
    volleyball_blocks               = models.IntegerField(default=0)
    volleyball_digs                 = models.IntegerField(default=0)
    volleyball_kills                = models.IntegerField(default=0)
    
    class Meta:
        abstract = True

class Position(ModelBase):
    '''
    Represents a single Volleyball position.
    '''
    name                            = models.CharField(max_length=255)
    short_name                      = models.CharField(max_length=5, help_text="5 characters or fewer.")
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)
    

class Game(GameBase):
    '''
    A representation of a Volleyball game.
    '''
    home_game_1_score               = models.IntegerField(default=0)
    home_game_2_score               = models.IntegerField(default=0)
    home_game_3_score               = models.IntegerField(default=0)
    home_game_4_score               = models.IntegerField(default=0)
    home_game_5_score               = models.IntegerField(default=0)
    away_game_1_score               = models.IntegerField(default=0)
    away_game_2_score               = models.IntegerField(default=0)
    away_game_3_score               = models.IntegerField(default=0)
    away_game_4_score               = models.IntegerField(default=0)
    away_game_5_score               = models.IntegerField(default=0)
    home_games_won                  = models.IntegerField(default=0)
    away_games_won                  = models.IntegerField(default=0)
    override_game_scores            = models.BooleanField(default=False)
    home_team                       = models.ForeignKey(School, related_name="volleyball_home_team", null=True)
    away_team                       = models.ForeignKey(School, related_name="volleyball_away_team", null=True)
    
    def __unicode__(self):
        return u'Week %s: %s at %s' % (self.week, self.away_team, self.home_team)
        
    def save(self, *args, **kwargs):
        
        # Slugify!
        name_string                 = u'Week %s %s at %s' % (self.week, self.away_team, self.home_team)
        self.slug                   = slugify(name_string)
        
        # Set up a list of two-tuples representing home/away scores.
        games = [('home_game_%d_score', 'away_game_%d_score') % (idx, idx) for idx in range(1,5)]
        
        # Build a private function which can decide a winner by comparing scores.
        def _assign_win(home, away):
            if self.override_game_scores == True:
                return
            if home > away:
                self.home_games_won += 1
            elif home < away:
                self.away_games_won += 1
            
        # Use map to iterate over the list of two-tuples and decide a winner for each pair.
        map(_assign_win, games)
        
        # Super!
        super(Game, self).save(*args, **kwargs)
    

class TeamGame(GameBase, VolleyballFields):
    '''
    A representation of a single team's performance in a single game.
    '''
    team                            = models.ForeignKey(School, related_name="volleyball_teamgame_team")
    game                            = models.ForeignKey(Game, related_name="volleyball_teamgame_game")
    season                          = models.ForeignKey(Season, related_name="volleyball_teamgame_season")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.team, self.id)
    

class TeamSeason(ModelBase, VolleyballFields):
    '''
    A representation of a single Volleyball team's performance over a season.
    '''
    team                            = models.ForeignKey(School, related_name="volleyball_teamseason_team")
    season                          = models.ForeignKey(Season, related_name="volleyball_teamseason_season")
    wins                            = models.IntegerField(default=0)
    losses                          = models.IntegerField(default=0)
    points_for                      = models.IntegerField(default=0)
    points_against                  = models.IntegerField(default=0)
    place                           = models.IntegerField(default=0)
    conference                      = models.ForeignKey(Conference, related_name="volleyball_teamseason_conference")
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
    

class PlayerGame(GameBase, VolleyballFields):
    '''
    A representation of a single Volleyball player's performance in a single game.
    '''
    player                          = models.ForeignKey(Player, related_name="volleyball_playergame_player")
    game                            = models.ForeignKey(Game, related_name="volleyball_playergame_game")
    season                          = models.ForeignKey(Season, related_name="volleyball_playergame_season")
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        super(PlayerGame, self).save(*args, **kwargs)
    

class PlayerSeason(ModelBase, VolleyballFields):
    '''
    A representation of a single Volleyball player's performance over a single season.
    '''
    player                          = models.ForeignKey(Player, related_name="volleyball_playerseason_player")
    season                          = models.ForeignKey(Season, related_name="volleyball_playerseason_season")
    position                        = models.ForeignKey(Position, related_name="volleyball_playerseason_position")
    number                          = models.IntegerField(blank=True, null=True)
    games                           = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'Week %s: %s stats (%s)' % (self.game.week, self.player, self.id)
    
    def save(self, *args, **kwargs):
        # self.rushing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.rushing_yards, self.rushing_attempts), 1))
        # self.receiving_yards_per_reception  = float(floatformat(preps_utils.handle_percents(self.receiving_yards, self.receptions), 1))
        # self.passing_completion_percentage  = float(floatformat(preps_utils.handle_percents(self.passing_completions, self.passing_attempts), 3))
        # self.passing_yards_per_attempt      = float(floatformat(preps_utils.handle_percents(self.passing_yards, self.passing_attempts), 1))
        # if self.passing_attempts == 0:
        #     self.passing_rating = 0.0
        # else:
        #     self.passing_rating             = float(floatformat(handle_hss_passer_rating(
        #         self.passing_yards,
        #         self.passing_touchdowns,
        #         self.passing_completions,
        #         self.passing_interceptions,
        #         self.passing_attempts
        #     ), 1))
        super(PlayerSeason, self).save(*args, **kwargs)
    
