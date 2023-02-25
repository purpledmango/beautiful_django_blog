from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog

class BlogPostSiteMap(Sitemap):

	changefreq = "weekly"
	priority = 0.8
	protocol = "http"


	def items(self):
		return Blog.objects.filter(content_live=True)

	def location(self, obj):
		return reverse('article', args=[str(obj.slug)])

	def lastmod(self, obj):
		return obj.updated_at