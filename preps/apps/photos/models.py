from django.db import models
from django.contrib.auth.models import User
from preps.apps.models import ModelBase
from preps.apps.sports.models import Player, School

class PhotoGallery(ModelBase):
    headline                        = models.CharField(max_length=255)
    body                            = models.TextField(max_length=255)
    
    class Meta:
        verbose_name                = 'Gallery'
        verbose_name_plural         = 'Galleries'
    
    def __unicode__(self):
        return self.headline
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PhotoGallery, self).save(*args, **kwargs)

class Photo(ModelBase):
    gallery                         = models.ForeignKey(PhotoGallery, related_name='gallery_photo_gallery')
    caption                         = models.CharField(max_length=255)
    photo                           = models.ImageField(upload_to='gallery/images/')
    players                         = models.ManyToManyField(Player, null=True, related_name='gallery_photo_players')
    teams                           = models.ManyToManyField(School, null=True, related_name='gallery_photo_teams')
    
    def __unicode__(self):
        return self.headline
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(PhotoGallery, self).save(*args, **kwargs)
