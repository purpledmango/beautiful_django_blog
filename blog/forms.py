from django import forms
from .models import Blog

class BlogPostCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'thumbnail', 'meta_description','meta_keywords', 'related_articles', 'author']
        # fields = "__all__"

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'thumbnail', 'meta_description','meta_keywords', 'related_articles']
