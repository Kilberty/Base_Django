from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150,blank=True,null=True)
    nome = models.CharField(max_length=150,blank=False,null=True,default="")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','nome']