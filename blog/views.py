from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import BlogPostCreateForm, UpdatePostForm
from .models import Blog, EmailList


def home(request):
	posts = Blog.objects.all()
	status = len(posts)
	
	return render(request, 'home.html', {"posts": posts})

def articlePage(request, slug):
	article = Blog.objects.get(slug = slug)
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

