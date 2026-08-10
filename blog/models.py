from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager



class Category (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    tags = TaggableManager()
    destination = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    travel_style = models.CharField(max_length=100)
    
    class Meta :
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    
    
class Comment (models.Model):
    posts = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    
    

# Create your models here.
