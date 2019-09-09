from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    picture = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        

class Profile(models.Model):
    infor = models.IntegerField(default=0)
    name=models.CharField( max_length=50, default='')
    bio = models.CharField(max_length=80 , blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['profile_picture']

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    name = models.CharField(max_length=70)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10, blank=True)
    profile = models.CharField(max_length=30, blank=True)
    link = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    caption = models.TextField()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(image__name__icontains=search_term)
        return images

    class Meta:
        ordering = ['-id']


class Rating(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save_rates(self):
        self.save()

    def delete_rates(self):
        self.delete()
