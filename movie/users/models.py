from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
	email = models.EmailField(unique=True)
	number = models.IntegerField(null=True)
	otp = models.IntegerField(null=True)
