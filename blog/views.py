from django.shortcuts import render, redirect,HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import BlogPostCreateForm, UpdatePostForm
from .models import Blog, EmailList, HomeTag, Tag
	


liveArticles = Blog.objects.filter(content_live = True)


# Process a string and coverts them to SEO keywords
def processKeywords(text):
	keywords = text.split(", ")
	processed = [key.replace(' ', '-') for key in keywords]
	return ",".join(processed)


def home(request):
	tags = HomeTag.objects.all()[0]
	print(tags)
	# the latest 2 artiles to be shown in the big tile
	latestOne = liveArticles[0]
	latestTwo = liveArticles[1]
	latestThree = liveArticles[2]
	
	
	# the medium tile article of recent post 3rd article and on...
	olderPosts = liveArticles[3:]
	
	if len(olderPosts) > 6:  # Check if there are at least 7 articles
		suggested = olderPosts[3:len(olderPosts)-3]
	else:
		suggested = olderPosts 

	# Handling the newsletter form
	error = None
	if request.method == "POST":
		subName = request.POST.get('sub-name')
		subEmail = request.POST.get('sub-email')
		try:	
			email = EmailList(sub_name=subName, sub_email=subEmail)
			email.save()
			return HttpResponseRedirect('/thank-you/')
		except IntegrityError:
			error = "You have arleady Subscribed using this E-mail!"

	title = tags.title
	description = tags.description
	keywords = processKeywords(tags.keyWords)

	context = {
	"latestOne": latestOne,
	"latestTwo": latestTwo,
	"latestThree": latestThree,
	"suggested": suggested,
	"title": title,
	"description": description,
	"keywords": keywords,
	"olderPosts": olderPosts,
	}

	return render(request, 'home.html', context)


def articlePage(request, slug):
	article = Blog.objects.get(slug = slug)
	article.update_view_count()
	title = article.title
	description = article.meta_description
	keywords = processKeywords(article.meta_keywords)
	tag = article.tags.all()[0]
	# Related Tag realted posts
	relatedPosts = article.related_articles.all()

	# Handling the newsletter form
	error = None
	if request.method == "POST":
		subName = request.POST.get('sub-name')
		subEmail = request.POST.get('sub-email')
		try:	
			email = EmailList(sub_name=subName, sub_email=subEmail)
			email.save()
			return HttpResponseRedirect('/thank-you/')
		except IntegrityError:
			error = "You have arleady Subscribed using this E-mail!"


	context = {'article':article, 'title': title, 'description':description,
		'keywords':keywords, 'error': error,
		'tag': tag, 'relatedPosts': relatedPosts}
	
	return render(request,'post.html', context)


def aboutUs(request):
	return render(request, "about.html")



def newsLetterSignUp(request):
	error = None
	if request.method == "POST":
		subName = request.POST.get('sub-name')
		subEmail = request.POST.get('sub-email')
		try:	
			email = EmailList(sub_name=subName, sub_email=subEmail)
			email.save()
			return HttpResponseRedirect('/thank-you/')
		except IntegrityError:
			error = "You have arleady Subscribed using this E-mail!"
	context = {'error': error}

	return render(request,'signup.html', context)

def tagPage(request, tag):

	relatedPosts = Blog.objects.filter(tag = tag)

	context = {'relatedPosts': relatedPosts}

	return render(request, 'categor-page.html', context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def thankYou(request):
	return render(request, 'thanks.html')

def food(request):
	tag = 'food'
	tagData = Tag.objects.filter(name=tag)[0]
	tagArticles = liveArticles.filter(tags__name= tag)
	latestOne = tagArticles[0]
	foodArticles = tagArticles[1:]
	title = f'Discover {tagData.name.upper()}'
	description = tagData.mtag_description
	keywords = processKeywords(tagData.mtag_keywords)
	context = {'foodArticles': foodArticles, 'latestOne': latestOne,
	'tagData': tagData,
	'title': title, 'description': description, 'keywords': keywords}
	return render(request, 'food.html', context)

def health(request):
	tag = 'health'
	tagData = Tag.objects.filter(name=tag)[0]
	tagArticles = liveArticles.filter(tags__name= tag)
	latestOne = tagArticles[0]
	healthArticles = tagArticles[1:]
	title = f'Discover {tagData.name.upper()}'
	description = tagData.mtag_description
	keywords = processKeywords(tagData.mtag_keywords)
	context = {'healthArticles': healthArticles, 'latestOne': latestOne, 'tagData': tagData,
	'title': title, 'description': description, 'keywords': keywords}
	return render(request, 'health.html', context)


def lifestyle(request):
	pass
	tag = 'lifestyle'
	tagData = Tag.objects.filter(name=tag)[0]
	tagArticles = liveArticles.filter(tags__name= tag)
	latestOne = tagArticles[0]
	lifestyleArticles = tagArticles[1:]
	title = f'Discover {tagData.name.upper()}'
	description = tagData.mtag_description
	keywords = processKeywords(tagData.mtag_keywords)
	context = {'lifestyleArticles': lifestyleArticles, 'latestOne': latestOne, 'tagData': tagData,
	'title': title, 'description': description, 'keywords': keywords}
	return render(request, 'lifestyle.html', context)
