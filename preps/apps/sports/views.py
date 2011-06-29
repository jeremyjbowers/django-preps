from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from preps.apps.sports.models import School, Player
# When adding each of the sports, you'll need to import them as different names. All of them.
from preps.apps.sports.football import models as football
from preps.apps.sports.volleyball import models as volleyball

class PlayerDetail(DetailView):
    '''
    Defines a function which provides a detail view of players.
    '''
    context_object_name         = "player"
    model                       = Player
    template_name               = 'players/player_detail.html'
    
    def get_queryset(self):
        '''
        Defines a function which overrides the queryset backing this generic view.
        '''
        # This queryset selects a single player. Don't get thrown off by the .filter().
        return Player.objects.filter(id=self.kwargs['pk'], slug=self.kwargs['player_slug'])
    
    def get_context_data(self, *args, **kwargs):
        '''
        Defines a function which overrides the context object with new context.
        '''
        # Super!
        context = super(PlayerDetail, self).get_context_data(*args, **kwargs)
        
        # These lines add player-related football and volleyball playerseasons to the context object. 
        context['football'] = football.PlayerSeason.objects.filter(player__id=self.kwargs['pk'])
        context['volleyball'] = volleyball.PlayerSeason.objects.filter(player__id=self.kwargs['pk'])
        
        return context
    

class SchoolDetail(DetailView):
    '''
    Defines a function which provides a detail view of schools.
    '''
    context_object_name         = "team"
    model                       = School
    template_name               = 'teams/school_detail.html'
    
    def get_queryset(self):
        '''
        Defines a function which overrides the queryset backing this generic view.
        '''
        # This queryset selects a single player. Don't get thrown off by the .filter().
        return School.objects.filter(id=self.kwargs['pk'], slug=self.kwargs['school_slug'])
    
    def get_context_data(self, *args, **kwargs):
        '''
        Defines a function which overrides the context object with new context.
        '''
        # Super!
        context = super(SchoolDetail, self).get_context_data(*args, **kwargs)
        
        # These lines add player-related football and volleyball playerseasons to the context object. 
        context['football'] = football.TeamSeason.objects.filter(team__id=self.kwargs['pk'])
        context['volleyball'] = volleyball.TeamSeason.objects.filter(team__id=self.kwargs['pk'])
        
        return context
    
