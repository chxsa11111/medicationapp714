from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'
        # swappable = 'AUTH_USER_MODEL'