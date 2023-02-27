from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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

	# the latest 2 artiles to be shown in the big tile
	latest2 = liveArticles[:2]
	
	# the medium tile article of recent post 3rd article and on...
	olderPosts = liveArticles[2:]

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
	
	related = Blog.objects.all()
	p = Paginator(related, 3)
	page_num = request.GET.get('page')
	page_obj = p.get_page(page_num)
	

	
	# prev_page = 
	# page_obj =  = pagination.get_page(page_number)

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


	context = {'article':article, 'title': title, 'description':description,
		'keywords':keywords, 'error': error,
		'tag': tag, 'page_obj': page_obj}
	
	return render(request,'post.html', context)


def aboutUs(request):
	return render(request, "about.html")


def tagPage(request, tag):

	relatedPosts = Blog.objects.filter(tag = tag)

	context = {'relatedPosts': relatedPosts}

	return render(request, 'categor-page.html', context)




