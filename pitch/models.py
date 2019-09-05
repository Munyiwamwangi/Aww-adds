from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField('profile/', null=True)
    bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        Profile.objects.all().delete()

