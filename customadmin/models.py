from django.db import models
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=220, unique=True)
    password=models.CharField(max_length=16)
    address=models.TextField()
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    deleted_at=models.DateTimeField(blank=True, null=True)
    created_at=models.DateTimeField(default=datetime.now)