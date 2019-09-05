from django.shortcuts import render, redirect
from .models import Project, Profile, Comments

from django.contrib.auth import authenticate, login, login_required

# Create your views here.

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home.html', {})
    else:
        return redirect('%s?next=%s' % (awwards.settings.LOGIN_URL, request.path))
