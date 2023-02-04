from django.contrib import admin
from .models import Blog, Tag, EmailList

class BlogAdmin(admin.ModelAdmin):
	list_display  = ('title', 'author_name', 'created_at', 'updated_at', 'thumbnail',)
	filter_horizontal = ('related_articles', 'tags',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(EmailList)