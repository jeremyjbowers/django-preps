import datetime
from django.db import models
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Season, School, Sport, Conference, MeetBase
from preps.apps.utils import functions as preps_utils

class Meet(MeetBase):
    teams = models.ManyToManyField(School)
    