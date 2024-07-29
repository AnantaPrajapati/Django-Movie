from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from service.forms import MovieForm
from service.models import Movie, Profile
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework import status
# from rest_framework.authentication.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from service.serializer import MovieSerializer, UserSerializer
from django.http import JsonResponse




# @AuthMiddleware
def index(request):
    # import pdb
    # pdb.set_trace()
    movies = Movie.objects.all().select_related('user')
    return render(request, 'index.html', {'movies': movies})


def course(request):
    return HttpResponse("course")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully")

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            print("Access Token:", access_token)

            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    else:
        return render(request, "registration/login.html")
def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        username = request.POST['username']
        password = request.POST['password']
        Confirmpassword = request.POST['Confirmpassword']
        city = request.POST['city']
        gender = request.POST['gender']
        user = authenticate(request, email=email, username=username, password=password)
        if password == Confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_profile = Profile(user=user, gender=gender, city=city)
                user_profile.save()
                messages.success(request, "Registration successful")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, "registration/register.html")
    
def custom_logout(request):
    logout(request)
    messages.success(request,("successfully logged out"))
    return redirect('login')

def details(request, course):
    return HttpResponse(course)


def AddMovie(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = user
            movie.save()
            messages.success(request, "Movie added successfully!")
            return redirect('AddMovie', user_id=user.id)
        else:
            print(form.errors)
            messages.error(request, "Error adding movie. Please correct the errors below.")
    else:
        form = MovieForm()
    movies = Movie.objects.filter(user=user)
    return render(request, 'AddMovie.html', {'form': form, 'movies': movies, 'user_id': user.id})


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated successfully!")
            return redirect('index')
        else:
            print(form.errors)  
    else:
        form = MovieForm(instance=movie)

    return render(request, 'edit.html', {'form': form, 'movie': movie})



def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        movie.delete()
        messages.success(request, "Movie deleted successfully!")
        return redirect('index')  
    return render(request, 'AddMovie.html', {'movie': movie})

def delete_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        user.delete()
        messages.success(request, "Your profile has been deleted successfully!")
        return redirect('index')  
    return render(request, 'Profile.html', {'user': user})



def password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        old_password = request.POST['oldpassword']
        new_password = request.POST['newpassword']

        if user.check_password(old_password):
            if new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user) 
                messages.success(request, "Password changed successfully!")
                return redirect('Profile') 
            else:
                messages.error(request, "New password cannot be empty.")
        else:
            messages.error(request, "Old password is incorrect.")
    
    return render(request, 'password.html', {'user': user})

def profile(request):
    # profile = get_object_or_404(User, user_id)

    return render(request, 'Profile.html')



@api_view(['GET'])
def MovieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def MovieDetail(request, pk):

    movies = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movies, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def MovieCreate(request):
    # import pdb
    # pdb.set_trace()
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def MovieUpdate(request, pk):
    # import pdb
    # pdb.set_trace()
    movie = Movie.objects.get(id = pk)
    serializer = MovieSerializer(instance= movie, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def MovieDelete(request, pk):
    # import pdb
    # pdb.set_trace()
    movie = Movie.objects.get(id = pk)
    movie.delete()
 
    return Response("movie deleted successfully !!!")


@api_view(['GET'])
def UserList(request):
    user = User.objects.all()
    serializer = UserSerializer(User, many = True)

    return Response(serializer.data)
