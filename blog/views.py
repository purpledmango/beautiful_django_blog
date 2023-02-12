from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import BlogPostCreateForm, UpdatePostForm
from .models import Blog, EmailList
from blog.defaults import keyWords, Title, Description


liveArticles = Blog.objects.filter(content_live = True)


# Process a string and coverts them to SEO keywords
def processKeywords(text):
	keywords = text.split(",")
	processed = [key.replace(' ', '-') for key in keywords]
	return ",".join(processed)


def home(request):
	latest2 = liveArticles[:2]
	
	# Handling the newsletter form
	error = None
	if request.method == "POST":
		subName = request.POST.get('sub-name')
		subEmail = request.POST.get('sub-email')
		try:	
			email = EmailList(sub_name=subName, sub_email=subEmail)
			email.save()
		except IntegrityError:
			error = "You have arleady Subscribed using this E-mail!"

	title = Title
	description = Description
	keywords = processKeywords(keyWords)

	context = {
	"latest2": latest2,
	"title": title,
	"description": description,
	"keywords": keywords,
	}

	return render(request, 'home.html', context)

def articlePage(request, slug):
	article = Blog.objects.get(slug = slug)
	article.update_view_count()
	title = article.title
	description = article.meta_description
	keywords = processKeywords(article.meta_keywords)

	# Handling the newsletter form
	error = None
	if request.method == "POST":
		subName = request.POST.get('sub-name')
		subEmail = request.POST.get('sub-email')
		try:	
			email = EmailList(sub_name=subName, sub_email=subEmail)
			email.save()
		except IntegrityError:
			error = "You have arleady Subscribed using this E-mail!"


	context = {'article':article, 'title': title, 'description':description, 'keywords':keywords, 'error': error}
	
	return render(request,'post.html', context)


def aboutUs(request):
	return render(request, "about.html")


def tagPage(request, tag):

	relatedPosts = Blog.objects.filter(tag = tag)

	context = {'relatedPosts': relatedPosts}

	return render(request, 'categor-page.html', context)




