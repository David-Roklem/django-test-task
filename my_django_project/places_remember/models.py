from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


# class StartPage(models.Model):
#     '''This page will be shown to a new user'''
#     username = models.CharField('Name of the user', max_length=100)
#     photo = models.ImageField('')