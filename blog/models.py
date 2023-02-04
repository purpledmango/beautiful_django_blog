from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default= "")
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
    

    def __str__(self):
        return self.title

    def author_name(self):
    	return self.author.first_name + " " + self.author.last_name

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"


class EmailList(models.Model):
    sub_name = models.CharField(max_length=255)
    sub_email = models.EmailField(max_length=255, unique=True)
    

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "New Letter Subscribers"