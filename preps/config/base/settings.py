import os
'''
Identify the project and its location on the filesystem.
'''
PROJECT_SLUG                = 'django-preps'
PROJECT_MODULE              = 'preps'
ROOT_URLCONF                = 'preps.config.base.urls'
PROJECT_DIR                 = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
'''
Below is the generic project stuff. This shouldn't change between environments.
'''
TIME_ZONE                   = 'America/New_York'
LANGUAGE_CODE               = 'en-us'
SITE_ID                     = 1
USE_L10N                    = True

SECRET_KEY = '1ai9a+8(!l$!0!qhy(*op^_f2w#x&haz2jh#%&0y@qj3))be99'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
)

GRAPPELLI_INDEX_DASHBOARD = 'preps.config.grappelli.dashboard.CustomIndexDashboard'

TEMPLATE_DIRS = (
   PROJECT_DIR + '/%s/%s/templates' % (PROJECT_SLUG, PROJECT_MODULE),
)

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
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
    'preps.apps.sports.tennis',
    'preps.apps.blog',
    'preps.apps.feeds',
    'preps.apps.photos',
    'preps.apps.home',
    'ckeditor',
    'sorl.thumbnail',
)