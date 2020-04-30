from django.db import models
from django.utils.timezone import timezone

class User(models.Model):
    user_name = models.CharField(max_length=200, default='')
    password = models.TextField()

    class Meta:
        ordering = ['user_name']
    
    def __str__(self):
        return self.user_name


class Profile (models.Model):
    city = models.CharField(max_length=150)
    number = models.CharField(max_length=200)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.email

