from django.contrib import admin
from service.models import Movie

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('movie_icon', 'movie_title', 'release_date', 'actor','description', 'country')

admin.site.register(Movie, ServiceAdmin)
# Register your models here.
