from django.db import models

class BoxPosition(models.Model):
    position = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.position
    

class SiteSection(models.Model):
    site_section = models.CharField(max_length=150)
    site_section_slug = models.SlugField()
    site_section_short_name = models.CharField(max_length=150)
    site_section_seo_description = models.TextField(blank=True, null=True)
    site_section_seo_title = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(max_length=3, default=0)
    
    class Meta:
        ordering = ['-weight']
    
    def __unicode__(self):
        return self.site_section
    

class PhotoBoxItem(models.Model):
    headline = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    photograph = models.ImageField(upload_to="photobox/")
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.headline
    

class HTMLTextBox(models.Model):
    site_section = models.ManyToManyField(SiteSection, blank=True, null=True)
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    show_header = models.BooleanField()
    position = models.ForeignKey(BoxPosition)
    weight = models.IntegerField(max_length=3, default=0)
    lead_art = models.ImageField(upload_to="box/art/", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "HTML text boxes"
        ordering = ['-weight']
    
    def __unicode__(self):
        return self.title
    

class QuickLink(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title
    
