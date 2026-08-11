from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website:index')
        messages.error(request,'Username or password is incorrect.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not password or not password2:
            messages.error( request, 'Please fill in all fields.')
            return render(request,'accounts/signup.html')

        if password != password2:
            messages.error( request,'The passwords do not match.')
            return render( request,'accounts/signup.html' )

        
        if User.objects.filter(username=username).exists():
            messages.error( request,'This username is already in use.')
            return render( request,'accounts/signup.html' )
        user = User.objects.create_user( username=username,password=password)
        login(request, user)
        return redirect('website:index')
    return render(request, 'accounts/signup.html')