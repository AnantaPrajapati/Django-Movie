"""
URL configuration for stproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('details/<slug:course>/', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('AddMovie/',views.AddMovie, name='AddMovie'), 
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path('password/<int:user_id>/', views.password, name='password'),
    path('Profile/', views.profile, name='Profile'),
    #    path('delete/', views.delete, name='delete'),
    path('', include("django.contrib.auth.urls")),
     
]
