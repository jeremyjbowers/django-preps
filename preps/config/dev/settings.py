try:
    from preps.config.dev.local_settings import *
except ImportError:
    pass

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'preps.apps.sports',
    'preps.apps.sports.football',
    'preps.apps.sports.volleyball',
    'preps.apps.sports.girls_soccer',
    'preps.apps.sports.boys_soccer',
    'preps.apps.sports.softball',
    'preps.apps.sports.baseball',
    'preps.apps.sports.girls_lacrosse',
    'preps.apps.sports.boys_lacrosse',
    'preps.apps.sports.girls_basketball',
    'preps.apps.sports.boys_basketball',
    'preps.apps.sports.hockey',
    'preps.apps.sports.field_hockey',
    'preps.apps.sports.wrestling',
    'preps.apps.sports.golf',
    'preps.apps.sports.swimming',
    'preps.apps.sports.track',
    'preps.apps.sports.cross_country',
    'preps.apps.blog',
    'preps.apps.feeds',
    'preps.apps.photos',
)