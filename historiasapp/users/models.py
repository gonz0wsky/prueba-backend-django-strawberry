import uuid
from django.db import models

# Create your models here.

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    hash = models.CharField(max_length=128)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=40)
