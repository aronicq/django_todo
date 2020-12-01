from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

# Create your models here.
class AppUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, password]

    objects = BaseUserManager()


class Tasks(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True, null=True)
    completed_date = models.DateField(default=datetime.date.today)

