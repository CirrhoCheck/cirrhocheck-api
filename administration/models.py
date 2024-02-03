from django.db import models
from django.contrib.auth.models import User

class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    # Add other fields as needed

class DummyItem(models.Model):
    description = models.CharField()
    # Add other fields as needed