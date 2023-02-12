from django.urls import path
from .views import home, articlePage, aboutUs


urlpatterns = [
	path("", home, name='home'),
	path("article/<str:slug>", articlePage, name="article"),
	path("about-us/", aboutUs, name="aboutUs"),
]