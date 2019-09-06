import datetime as dt
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    jobtitle = models.TextField()
    email = models.EmailField(unique=True, max_length=254)
    country = models.TextField(max_length=50, default='Anonymous')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        Profile.objects.all().delete()


class Project(models.Model):
    title = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='project_images/', null=True)
    description = models.TextField(max_length=200, null=True)
    link = models.TextField(max_length=200, null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    design = models.IntegerField(default = 0)
    Usability = models.IntegerField(default = 0)
    content = models.IntegerField(default = 0)
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_posted']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_user(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls, project_id):
        projects = cls.objects.get(id=project_id)
        return projects
    
class Comment(models.Model):
    comment = models.CharField(null=True, max_length=5000, verbose_name='name')
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "comments"
        verbose_name_plural = "comments"
        ordering = ['-date']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
