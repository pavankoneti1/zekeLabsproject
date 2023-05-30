from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import models, forms, authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
# Create your views here.

class HomePage(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        return render(request, 'home.html')

class UserCreateViewSet(viewsets.ModelViewSet):
    """
    API end point for create, signup, fetch and delete user
    """

    queryset = models.User.objects.all()

    def list(self, request, *args, **kwargs):
        form = forms.UserCreationForm
        return render(request, 'UserCreationForm.html', {'form':form, 'button_name':'Sign Up'})

    def create(self, request, *args, **kwargs):
        # to create the users
        form = forms.UserCreationForm(request.POST) # create user if
        if form.is_valid():
            form.save()
            message = 'user successfully created login'
            return redirect('/api/login')
        message = form.errors
        return Response({"message":message})

    @method_decorator(login_required)
    def update(self, request, *args, **kwargs):
        # to update user credentials
        form = forms.UserChangeForm()
        return render(request, 'UserCreationForm.html', {'form':form, 'button_name':'update'})

class UserLoginViewSet(viewsets.ModelViewSet):
    """
    API for login and logout the user
    """
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        form = forms.AuthenticationForm()
        return render(request, 'UserCreationForm.html', {'form':form, 'button_name':'Login', 'create':True})

    def create(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return Response({"message":"user successfully logged in"})

    @action(detail=False, methods=['post', 'get', 'put', 'patch'])
    def user_logout(self, request):
        logout(request)
        return Response({"message":'user successfully logged out'})