from django.contrib.auth.models import AbstractUser, Group, Permission # type: ignore
from django.db import models # type: ignore

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    image_url = models.URLField()