from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def Index(request):
    return render(request, 'Index.html')


def Login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user =authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('index')
        else:
            return HttpResponse("Invalid Username & Passsword")

    return render(request, 'Login.html')


def Register(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Different Password")
        else:    
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')

    return render(request, 'Register.html')


def Logout(request):
    logout(request)
    return redirect('login')