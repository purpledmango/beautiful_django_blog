from django.urls import path
from .views import home, articlePage, aboutUs, newsLetterSignUp, thankYou, food, health, lifestyle


urlpatterns = [
	path("", home, name='home'),
	path("article/<str:slug>", articlePage, name="article"),
	path("about-us/", aboutUs, name="aboutUs"),
	path("about-us/", aboutUs, name="aboutUs"),
	path("news-letter/", newsLetterSignUp, name="newsLetterSignUp"),
	path("thank-you/", thankYou, name="thankYou"),
	path("food/", food, name="food"),
	path("health/", health, name="health"),
	path("lifestyle/", lifestyle, name="lifestyle"),
]