from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Input(models.Model):
    User = models.CharField(max_length=150)
    Question = models.TextField()

class TestCase(models.Model):
    InputS = models.ForeignKey('Input')
    OutputS = models.ForeignKey('Input')
