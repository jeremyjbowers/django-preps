from preps.config.base.settings import *

# try:
#     from preps.config.dev.local_settings import *
# except ImportError:
#     pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_preps',
        'USER': 'pguser',
        'PASSWORD': 'wapo',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DEBUG                       = True
TEMPLATE_DEBUG              = DEBUG

MEDIA_ROOT                  = os.path.join(PROJECT_DIR, '%s/media' % (PROJECT_SLUG))
MEDIA_URL                   = ''
ADMIN_MEDIA_PREFIX          = '/static/admin/'


ADMINS = (
     ('Jeremy Bowers', 'jeremyjbowers@gmail.com'),
)
MANAGERS = ADMINS

INSTALLED_APPS              = ()