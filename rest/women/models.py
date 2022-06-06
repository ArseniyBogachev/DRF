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
    women_like = models.ManyToManyField(WomenUser, through='WomenRelation', related_name='books')

    def __str__(self):
        # return f'Id:{self.pk} name:{self.name}'
        return self.name

class WomenRelation(models.Model):
    user = models.ForeignKey(WomenUser, on_delete=models.CASCADE)
    women = models.ForeignKey(Women, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)

    def __str__(self):
        return f'user: {self.user} women: {self.women}'


class BlackListJWT(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(WomenUser, on_delete=models.CASCADE)
    add = models.DateTimeField(auto_now_add=True)


# class RefreshJWT(models.Model):
#     user = models.ForeignKey(WomenUser, on_delete=models.CASCADE)

# Create your models here.
