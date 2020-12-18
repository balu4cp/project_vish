from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(AbstractUser):
#     code = models.CharField(max_length=20, null=True, blank=True)
from django.contrib.auth.models import User
class Code(models.Model):
   
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,related_name="+")
    code = models.TextField(unique=True)

class Friend(models.Model):
   
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,related_name="+")
    friend = models.OneToOneField(to=User, on_delete=models.CASCADE,null=True,blank=True,related_name="+")

