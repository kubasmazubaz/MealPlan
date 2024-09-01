from django.db import models

# Create your models here.

class Login(models.Model):
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return "Hi" + self.login
    
