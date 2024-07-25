from django.db import models
class Movie(models.Model):
    movie_icon =  models.FileField(upload_to='movie_icons/')
    movie_title = models.CharField(max_length = 50)
    release_date = models.DateField()
    description = models.TextField()
    actor = models.TextField()
    country = models.CharField(max_length = 50)


    def _str(self):
        return self.movie_title

# Create your models here.
