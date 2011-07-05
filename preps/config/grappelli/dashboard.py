from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.AppList(
            _('Blog'),
            collapsible=True,
            column=1,
            models=('wapo_allmet_proj.apps.blog.*',),
        ))
        self.children.append(modules.AppList(
            _('Feeds'),
            collapsible=True,
            column=1,
            models=('wapo_allmet_proj.apps.feeds.*',),
        ))
        self.children.append(modules.AppList(
            _('Home'),
            collapsible=True,
            column=1,
            models=('wapo_allmet_proj.apps.home.*',),
        ))
        self.children.append(modules.ModelList(
            _('Administration'),
            column=2,
            collapsible=True,
            models=('django.contrib.*',),
        ))
        self.children.append(modules.AppList(
            _('Meet Sports'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'wapo_allmet_proj.apps.sports.cross_countr*',
                'wapo_allmet_proj.apps.sports.gol*',
                'wapo_allmet_proj.apps.sports.swimmin*',
                'wapo_allmet_proj.apps.sports.trac*',
                'wapo_allmet_proj.apps.sports.wrestlin*',
                'wapo_allmet_proj.apps.sports.tenni*'
            ),
        ))
        self.children.append(modules.AppList(
            _('Boys Sports'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'wapo_allmet_proj.apps.sports.boys_*',
                'wapo_allmet_proj.apps.sports.foot*',
                'wapo_allmet_proj.apps.sports.base*',
                'wapo_allmet_proj.apps.sports.hock*'
            ),
        ))
        self.children.append(modules.AppList(
            _('Girls Sports'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=(
                'wapo_allmet_proj.apps.sports.girls_*',
                'wapo_allmet_proj.apps.sports.volley*',
                'wapo_allmet_proj.apps.sports.soft*',
                'wapo_allmet_proj.apps.sports.field_*'
            ),
        ))
        self.children.append(modules.Feed(
            _('Latest Django News'),
            column=2,
            feed_url='http://feeds.washingtonpost.com/rss/sports/highschools',
            limit=10
        ))
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=15,
            collapsible=False,
            column=3,
        ))