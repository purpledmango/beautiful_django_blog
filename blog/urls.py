from django.urls import path
from .views import home, articlePage


urlpatterns = [
	path("", home, name='home'),
	path("article/<str:slug>", articlePage, name="article")	
]