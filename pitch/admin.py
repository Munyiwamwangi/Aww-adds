from django.contrib import admin
from .models import Profile, Comment, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Profile)