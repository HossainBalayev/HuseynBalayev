from django.db import models
from django.contrib.auth.models import AbstractUser

class MY_USER(AbstractUser):
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user/')
    about = models.TextField(blank=True)
    



