from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.contrib.auth.models import User

    

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class blogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    blogImg =  models.ImageField(upload_to='blogImg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    categories = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title