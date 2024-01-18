from django.contrib.auth import authenticate, login as sys_login
from django.shortcuts import render, redirect
from .models import User


def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                sys_login(request, user)
                print("logged in")
                return redirect('/')
            else:
                print("invalid email or password")
    else:
        print("form is not posted yet")
    return render(request, 'account/login.html')



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        
        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)
            print('User Created: ', user)
            return redirect('/login')
        else:
            print("something went wrong!!")

    else:
        print("form is not posted yet")
    return render(request, 'account/signup.html')