from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True)
    bio = models.TextField(max_length=120, blank=True)
    birth_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.username
