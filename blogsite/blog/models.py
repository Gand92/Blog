from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Model representing the blog post"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=5000, help_text="Enter the content of the blog post")
    post_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular blog post"""
        return reverse('blogpost-detail', kwargs={'pk': self.pk}) #args=[str(self.id)]

    def __str__(self):
        return self.title
