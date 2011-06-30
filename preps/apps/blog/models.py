from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from preps.apps.models import ModelBase
from preps.apps.sports.models import Player, School

class Series(ModelBase):
    name                            = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "blog post series"
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(Series, self).save(*args, **kwargs)

    # Use the permalink decorator from models to designate this as our post's absolute URL.
    @models.permalink
    # Define our get_absolute_url method.
    def get_absolute_url(self):
        '''
        Defines a function which returns an absolute URL for a model instance.
        '''
        # Return the reverse of our 'post_detail' view matching the 'series_slug' to the relevant field (self.slug).
        # Note there's a None in there because we're specifying **kwargs and thus not *args. DON'T CROSS THE STREAMS.
        return ('post_list_series', None, { 'series_slug': self.slug, 'pk': self.id })
    

class Post(ModelBase):
    title                           = models.CharField(max_length=255)
    blurb                           = models.TextField(blank=True, null=True)
    body                            = models.TextField(blank=True, null=True)
    lead_image                      = models.ImageField(upload_to='blog/images/lead/', blank=True, null=True)
    author                          = models.ForeignKey(User)
    series                          = models.ForeignKey(Series, null=True)
    teams                           = models.ManyToManyField(School, blank=True, null=True, related_name='blog_post_teams')
    players                         = models.ManyToManyField(Player, blank=True, null=True, related_name='blog_post_players')
    publication_date                = models.DateTimeField()
    external_media_url              = models.URLField(blank=True, null=True, verify_exists=False)
    featured                        = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-publication_date']
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(Post, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', None, { 'post_slug': self.slug, 'pk': self.id })

class RecruitingCollege(ModelBase):
    name                            = models.CharField(max_length=255)
    logo                            = models.ImageField(upload_to='blog/images/colleges/logos/', blank=True, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(RecruitingCollege, self).save(*args, **kwargs)

class RecruitingUpdate(ModelBase):
    COMMITMENT_CHOICES = (
        (0, 'Committed'),
        (3, 'Solid'),
        (5, 'Verbal'),
        (7, 'Soft verbal'),
        (9, 'Unknown'),
    )
    commitment_rating               = models.IntegerField(max_length=1, choices=COMMITMENT_CHOICES)
    player                          = models.ForeignKey(Player)
    post                            = models.ForeignKey(Post)
    college                         = models.ManyToManyField(RecruitingCollege, related_name="blog_recruitingupdate_colleges")
    blurb                           = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "recruiting update"
        verbose_name_plural = "recruiting updates"
        ordering = ['-created']
    
    def __unicode__(self):
        return "Update %s: %s" % (self.id, self.player)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(RecruitingUpdate, self).save(*args, **kwargs)
    

class Link(ModelBase):
    post                        = models.ForeignKey(Post, null=True)
    headline                    = models.CharField(max_length=255)
    link_url                    = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(Link, self).save(*args, **kwargs)

class TopAthletes(ModelBase):
    post                            = models.ForeignKey(Post, related_name="topathletelist_set")
    rank                            = models.IntegerField()
    player                          = models.ForeignKey(Player)
    blurb                           = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Top athlete"
        verbose_name_plural = "Top athletes"
        ordering = ['-created']
    
    def __unicode__(self):
        return "%s.) %s (id: %s/post: %s)" % (self.rank, self.player, self.id, self.post.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(TopAthletes, self).save(*args, **kwargs)

class TopTeams(ModelBase):
    post                            = models.ForeignKey(Post, related_name="topteamlist_set")
    rank                            = models.IntegerField()
    team                            = models.ForeignKey(School)
    blurb                           = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Top team"
        verbose_name_plural = "Top teams"
        ordering = ['-created']
    
    def __unicode__(self):
        return "%s.) %s (id: %s/post: %s)" % (self.rank, self.team, self.id, self.post.id)
    
    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == '':
            self.slug = slugify(self.__unicode__())
        super(TopTeams, self).save(*args, **kwargs)