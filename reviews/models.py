from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    movie = models.CharField(max_length=80)