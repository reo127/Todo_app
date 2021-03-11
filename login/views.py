from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from login.models import Contact
from login import models
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from django.contrib import messages


# import re

# from django.conf import settings
# from django.contrib.auth.decorators import login_required


# Create your views here.

def homePage(request):
    return render(request, 'login/home.html')

def about(request):
    return render(request, 'login/about.html')

@csrf_protect
def contact(request):
    if request.method == "POST":
        timestamp = timezone.now()
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']

        Contact.objects.create(name=name, email=email, contact=contact, timestamp=timestamp)

    return render(request, 'login/contact.html')


def HandleSignup(request):
    if request.method == "POST":
        # Geting data From base.html in signup modal form
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # print(username)

        # Creating new user
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'You singup Successfuly, Now place login')
        # messages.success(request, 'Your account is successufly Created')
  
    return HttpResponseRedirect('/')

def HandleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        # authenticateing the user
        user = authenticate(username=loginusername, password=loginpassword)
        # messages.success(request, 'You are successfuly login')

        if user is not None:
            login(request, user)
            messages.success(request, 'You are loggin')


    return HttpResponseRedirect('/')

# @login_required
def logoutHandle(request):
    logout(request)
    messages.error(request, 'You are logout ')
    # messages.success(request, 'User Successfuly Loguot')
    return redirect('http://127.0.0.1:8000/')





