from django.shortcuts import render
from .models import Movie, User
from rest_framework import viewsets, generics, status
from .serializer import MovieSerializer, UserSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView 
from django.contrib.auth import authenticate


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete (sef, request, **args):
        Movie.objects.alll().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email= email).first()

        if user is None:
            return Response('user not found')
        
        if not user.check_password(password):
            return Response("Incorrect password")
        
        return Response({'message':'ok'})


# class UserLoginView(APIView):
#     def post(self, request):
#         user = authenticate(username=request.data['username'], password=request.data['password'])
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=401)
        

    # def perform_create(self, serializer):
    #     serializer.save()

    # @action(detail = False, methods = ['get'])
    # def custom_action(self, reqest):
    #     return Response({"message": 'custom action response'})
    


# Create your views here.
