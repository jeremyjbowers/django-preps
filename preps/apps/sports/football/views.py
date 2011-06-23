from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from wapo_sports_proj.apps.api.nfl.models import Game, TeamGame, PlayerGame, TeamSeason, PlayerSeason

class GameDetail(DetailView):
    '''
    A detail view of a Football game.
    '''
    context_object_name = "game"
    queryset = Game.objects.all()

    def get_context_data(self, *args, **kwargs):
        '''
        Defines a function which attaches context data to game detail pages.
        '''
        context = super(GameDetail, self).get_context_data(*args, **kwargs)
        game = context.get('game')
        if game:
            context['teamgames'] = TeamGame.objects.filter(game=game).select_related()
            context['playergames'] = PlayerGame.objects.filter(game=game).select_related()
        return context