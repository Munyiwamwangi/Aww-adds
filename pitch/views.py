from django.shortcuts import render, redirect
from .models import Project, Profile, Comment
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, login_required

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return HttpResponse('<h1>about pitch</h1>')
