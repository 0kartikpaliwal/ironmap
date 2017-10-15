from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.CharField(max_length=200)
    ques = models.ForeignKey('auth.user')
    ans = models.TextField()