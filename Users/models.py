from django.db import models
from django.contrib.auth.models import User

class UsersLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()  # Store email

    def __str__(self):
        return self.user.username
