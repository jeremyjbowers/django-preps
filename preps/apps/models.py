from django.db import models

class ModelBase(models.Model):
    slug                            = models.SlugField(max_length=255, blank=True, null=True)
    active                          = models.BooleanField(default=False)
    created                         = models.DateTimeField(auto_now_add=True)
    updated                         = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
