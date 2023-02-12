from django.db import models
from auditlog.registry import auditlog
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField



class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default= "")
    mtag_description = models.TextField(blank=True)
    mtag_keywords = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    body = HTMLField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    optimized_thumbnail = ImageSpecField(source='thumbnail',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    related_articles = models.ManyToManyField("self", blank=True)
    tags = models.ManyToManyField(Tag)
    content_live = models.BooleanField(default = False)
    views = models.PositiveIntegerField(default=0)

    def update_view_count(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title

    def author_name(self):
    	return self.author.first_name + " " + self.author.last_name

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"
        ordering = ['-created_at']


class EmailList(models.Model):
    sub_name = models.CharField(max_length=255)
    sub_email = models.EmailField(max_length=255, unique=True)


    def __str__(self):
        return self.sub_name
    class Meta:
        verbose_name_plural = "New Letter Subscribers"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    socail_url = models.CharField(max_length=500)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def __str__(self):
        return self.body




auditlog.register(Blog)
auditlog.register(EmailList)
auditlog.register(Tag)
