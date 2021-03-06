from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    image = models.ImageField(upload_to="images")
    cups = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created_on"]
