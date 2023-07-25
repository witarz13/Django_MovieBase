from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Movie(models.Model):
    title=models.CharField(max_length=220)
    year=models.IntegerField()
    url=models.CharField(max_length=220,null=True)
    info=models.CharField(max_length=2200,null=True)
    rate_system=models.CharField(max_length=2200,null=True)
    def __str__(self):
        return f'{self.title}'
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username must be set')
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserTable(AbstractBaseUser):
    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=24)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    def __str__(self):
        return f'{self.username}'