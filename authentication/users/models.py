from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserList(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)


    def __str__(self):
        return self.get_username()