from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

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
