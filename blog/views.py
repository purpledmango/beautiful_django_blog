from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import BlogPostCreateForm, UpdatePostForm
from .models import Blog, EmailList

liveArticles = Blog.objects.filter(content_live = True)

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

	context = {"latest2": latest2}

	return render(request, 'home.html', context)

def articlePage(request, slug):
	article = Blog.objects.get(slug = slug)
	article.update_view_count()

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



	context = {'article':article, 'error': error}
	
	return render(request,'post.html', context)



def tagPage(request, tag):

	relatedPosts = Blog.objects.filter(tag = tag)

	context = {'relatedPosts': relatedPosts}

	return render(request, 'categor-page.html', context)
