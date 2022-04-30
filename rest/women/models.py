from django.contrib.auth.models import User
from django.db import models



class Women(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.TextField(blank=True)
    age = models.IntegerField()
    delete = models.BooleanField(default=True)
    display = models.BooleanField(default=False)
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name
# Create your models here.
