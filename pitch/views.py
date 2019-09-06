from django.shortcuts import render, redirect
from .models import Project, Profile, Comment
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, login_required

# Create your views here.
posts = [
{
'author':'Joe',
'title':'Post One',
'content': 'Checker',
'date':'Jan 21, 019'
},
{
'author':'Munyi',
'title':'Post Two',
'content': 'checker2',
'date':'Feb 21, 019'
}

]

def home(request):

	context={
	'posts':posts
	}

	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {'title':'About'})
