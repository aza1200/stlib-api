from django.db import models
from common.models import CommonModel
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=140)
    email=models.EmailField(max_length=140,blank=True)
    belongs = models.ManyToManyField("users.Club")
    avatar = models.URLField(blank=True)
    
    def total_clubs(user):
        return user.belongs.count()
    
    def __str__(self):
        return self.username
    
class Club(CommonModel):
    
    """Club Definition"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name