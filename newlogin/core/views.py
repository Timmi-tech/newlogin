from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html', {})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Creditianls invalid')
            return redirect('signin')


   

    return render(request, 'sigin.html', {})

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']


        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password )
                user.save()
                return redirect('signin')
                
        else:
            messages.warning(request, "Password not matching")
            return redirect('signup')
    return render(request, 'signup.html', {})

def logout(request):
    auth.logout(request)
    return redirect('signin')