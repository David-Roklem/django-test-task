from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Memory(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000)
    # lat = models.FloatField(blank=True, null=True)
    # lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.title)


class Userpic(models.Model):
    username = models.CharField(max_length=100)
    pic = models.CharField(max_length=500)
