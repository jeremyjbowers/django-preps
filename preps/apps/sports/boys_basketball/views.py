from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from preps.apps.sports.boys_basketball.models import Game, TeamGame, TeamSeason, PlayerGame, PlayerSeason

class GameDetail(DetailView):
	'''
	A detail view of a Boys Basketball game
	'''
	context_object_name = "games"
	queryset = Game.objects.all()
		
			def get_context_data(self, *args, **kwargs):
			'''
			Defines a function which attaches context data to game detail pages
			'''
			context  = super(GameDetail, self).get_context_data(*args, **kwargs)
			game = context.get('games')
			if game:
				context['teamgames'] = TeamGame.objects.filter(game=game).select_related()
				context['playergames'] = PlayerGame.objects.filter(game=game).select_related()
			return context