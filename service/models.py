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
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.gender

    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created: 
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# Create your models here.
