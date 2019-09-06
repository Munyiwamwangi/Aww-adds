from django.shortcuts import render, redirect
from .models import Project, Profile, Comment
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, login_required

# Create your views here.
def home(request):

	context={
	'posts':Project.objects.all()
	}

	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {'title':'About'})
