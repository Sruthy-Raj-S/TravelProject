

from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Emailid = request.POST['Email id']
        password = request.POST['password']
        Confirmpassword = request.POST['Confirm password']

        if password == Confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=Emailid).exists():
                messages.info(request, "Mail id already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=Firstname, last_name=Lastname,
                                                password=password, email=Emailid)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')

    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')