from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from user.form import UserRegisterForm, UserLoginForm

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'login.html', {'form': form})
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})






