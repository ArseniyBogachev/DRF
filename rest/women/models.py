from django.contrib.auth.models import User, AbstractUser
from django.db import models


class WomenUser(AbstractUser):

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Women(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    del_obj = models.BooleanField(default=False)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Create your models here.
