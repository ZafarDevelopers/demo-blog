from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
  author= models.ForeignKey(User, on_delete=models.CASCADE)
  title= models.CharField(max_length=255)
  content= models.TextField()
  datePosted= models.DateTimeField(default=timezone.now)


# Create your models here.
