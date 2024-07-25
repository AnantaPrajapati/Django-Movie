from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from service.forms import MovieForm
from service.models import Movie


# @AuthMiddleware
def index(request):
#    data={
#        'title':'House black',
#        'place': 'Dragon stone',
#        'dragons': ['syrax', 'vermithor', 'caraxes', 'meleys'],
#        'NumberofDragons': [1, 3 ,5 , 7],
#        'dragonRider':[
#                {'dragonRider':'daemon', 'dragon':'caraxes'},
#                 {'dragonRider':'Aemond', 'dragon':'Vaghar'},
#                {'dragonRider':'Aegon', 'dragon':'sunfyre'},
#                {'dragonRider':'Rahnerya', 'dragon':'Syrax'}
           
#        ]
#    }
   return render (request,"index.html")

def course(request):
    return HttpResponse("course")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, ("Logged in successfully"))
            return redirect('index')
        else:
            messages.success(request,("Invalid username or password"))
            return redirect('login')
    else:
        return render(request, "registration/login.html")

def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        username = request.POST['username']
        password = request.POST['password']
        Confirmpassword = request.POST['Confirmpassword']
        user = authenticate(request, email=email, username=username, password=password )
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


def AddMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "Movie added successfully!")
            return redirect('AddMovie')
        else:
            print(form.errors)
            messages.error(request, "Error adding movie. Please correct the errors below.")
    else:
        form = MovieForm()
    movies = Movie.objects.all()
    return render(request, 'AddMovie.html', {'form': form, 'movies': movies})


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated successfully!")
            return redirect('AddMovie')
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