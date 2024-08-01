from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie_icon =  models.FileField(upload_to='movie_icons/')
    movie_title = models.CharField(max_length = 50)
    release_date = models.DateField()
    description = models.TextField()
    actor = models.TextField()
    director = models.TextField(null=True)
    country = models.CharField(max_length = 50)

    def __str__(self):
        return self.movie_title
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=9, null=True, blank=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


# class otp(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     otp = models.CharField(max_length =6)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"OTP for {self.user.email} is {self.otp}"

# Create your models here.
