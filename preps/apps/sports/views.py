from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from preps.apps.sports.models import School, Player
from preps.apps.sports.football.models import PlayerSeason as FootballPlayerSeason
from preps.apps.sports.volleyball.models import PlayerSeason as VolleyballPlayerSeason

class PlayerDetail(DetailView):
    '''
    Defines a function which provides a detail view of players.
    '''
    context_object_name         = "player"
    model                       = Player
    template_name               = 'players/player_detail.html'
    
    def get_queryset(self):
        return Player.objects.filter(id=self.kwargs['pk'], slug=self.kwargs['player_slug'])
    
    def get_context_data(self, *args, **kwargs):
            context = super(PlayerDetail, self).get_context_data(*args, **kwargs)
            context['football'] = FootballPlayerSeason.objects.filter(player__id=self.kwargs['pk'])
            context['volleyball'] = VolleyballPlayerSeason.objects.filter(player__id=self.kwargs['pk'])
            return context