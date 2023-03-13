from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogPostSiteMap

sitemaps = {
    'blog': BlogPostSiteMap,
}

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('blog.urls')),
]

if settings.DEBUG == True:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

