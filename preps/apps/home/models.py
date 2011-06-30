from django.db import models
from preps.apps.models import ModelBase

class SiteSection(ModelBase):
    name                = models.CharField(max_length=150)
    display_name        = models.CharField(max_length=150)
    weight              = models.IntegerField(max_length=2, default=0)
    
    class Meta:
        ordering = ['-weight']
    
    def __unicode__(self):
        return self.site_section
        
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(SiteSection, self).save(*args, **kwargs)
    

# class PhotoBoxItem(ModelBase):
#     headline            = models.CharField(max_length=255)
#     body                = models.CharField(max_length=255)
#     link                = models.URLField(verify_exists=False, max_length=255)
#     photo               = models.ImageField(upload_to="home/photo_box/images/")
#     
#     def __unicode__(self):
#         return self.headline
#     
#     def save(self, *args, **kwargs):
#         if self.slug == None or self.slug == '':
#             self.slug = slugify(self.__unicode__())
#         super(PhotoBoxItem, self).save(*args, **kwargs)
    

class TextBoxItem(ModelBase):
    POSITION_CHOICES = (
        (0,'Not displayed'),
        (1,'Left rail'),
        (2,'Right rail'),
        (8,'Top banner'),
        (9,'Bottom banner'),
    )
    site_section        = models.ManyToManyField(SiteSection, null=True, related_name='home_html_box_site_sections')
    headline            = models.CharField(max_length=255)
    body                = models.TextField()
    show_headline       = models.BooleanField()
    position            = models.IntegerField(max_length=1, choices=POSITION_CHOICES, default=0)
    weight              = models.IntegerField(max_length=2, default=0)
    photo               = models.ImageField(upload_to="home/html_box/images/", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "HTML text boxes"
        ordering = ['-weight']
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(HTMLTextBox, self).save(*args, **kwargs)
    
