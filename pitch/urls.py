from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='pitches'),
    path('about/', views.about, name='about'),
]
