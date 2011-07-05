from preps.config.base.settings import *

try:
    from preps.config.stage.local_settings import *
except ImportError:
    pass

DEBUG                       = True
TEMPLATE_DEBUG              = DEBUG

MEDIA_ROOT                  = os.path.join(PROJECT_DIR, '%s/media' % (PROJECT_SLUG))
MEDIA_URL                   = ''

# GRAPPELLI SETTINGS
ADMIN_MEDIA_PREFIX          = 'http://preps.s3.amazonaws.com/static/grappelli/'

# CKEDITOR SETTINGS
CKEDITOR_MEDIA_URL          = 'http://preps.s3.amazonaws.com/static/ckeditor2/'
STATIC_URL                  = '/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              # '-', 'Format',
              # '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
        ],
        'width': 750,
        'height': 300,
        'toolbarCanCollapse': False,
    },
    
    'simple_toolbar': {
        'toolbar': [
            [ 'Bold', 'Italic', 'Underline' ],
        ],
        'width': 500,
        'height': 150,
    },
}

# DJANGO-STORAGES SETTINGS
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
DEFAULT_FILE_STORAGE        = 'storages.backends.s3.S3Storage'
AWS_STORAGE_BUCKET_NAME     = 'preps'

# SORL-THUMBNAIL SETTINGS

ADMINS = (
     ('Jeremy Bowers', 'jeremyjbowers@gmail.com'),
)
MANAGERS = ADMINS