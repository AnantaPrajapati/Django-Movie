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
from rest_framework.routers import DefaultRouter
from service.views import MovieViewSet, UserViewSet, LoginView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from service import views



router = DefaultRouter()
router.register(r'MV', MovieViewSet)

router.register(r'UL', UserViewSet)

# router.register('loginview', LoginView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('details/<slug:course>/', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('AddMovie/<int:user_id>',views.AddMovie, name='AddMovie'), 
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path('password/<int:user_id>/', views.password, name='password'),
    path('Profile/', views.profile, name='Profile'),
    #    path('delete/', views.delete, name='delete'),
    path('', include("django.contrib.auth.urls")),
    path('MovieList/', views.MovieList, name='MovieList'),
    path('MovieDetail/<str:pk>', views.MovieDetail, name='MovieDetail'),
    path('MovieCreate/', views.MovieCreate, name='MovieCreate'),
    path('MovieUpdate/<str:pk>', views.MovieUpdate, name='MovieUpdate'),
    path('MovieDelete/<str:pk>', views.MovieDelete, name='MovieDelete'),
    path('UserList/', views.UserList, name='Userlist'),
    path('', include(router.urls)),
    # path('loginView/', views.LoginView, name='LoginView' )
     
]
