
# Create your models here

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=123)  # Store hashed password
    otp = models.CharField(max_length=6, blank=True, null=True)  # Store OTP as string
    user_schema = models.TextField(blank=True, null=True)  # JSON schema for user data
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
