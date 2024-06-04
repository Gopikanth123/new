from django.db import models
from django.utils import timezone


class Registration(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mobile
