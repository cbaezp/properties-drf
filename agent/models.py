from datetime import datetime

from django.db import models

# Create your models here.


class Agent(models.Model):

    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    langages = models.CharField(max_length=50)

    def __str__(self):
        return self.name
