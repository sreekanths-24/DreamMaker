from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User
from .models import *
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You have been logged in as {username}')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login_user')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, f'Account created for {username}')
            return redirect('login_user')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register.html', {'form': form})

def profile(request, id):
    if request.user.is_authenticated:
        ob = User.objects.get(id=id)
        obj = Profile.objects.get(user=id)
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'profile.html', {'user': ob, 'profile': obj, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.success(request, "You must be logged in to view profile.")
        return redirect('index')

# views.py

def add_more_details_to_profile(request, id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated successfully')
            return redirect('profile', id=id)
        else:
            messages.error(request, 'No changes made to your profile details.')
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'add_more_details_to_profile.html', {'form': form, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.error(request, 'You must be logged in to edit profile.')
        return redirect('index')

def edit_account_info(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        form = RegisterUserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account details updated successfully')
            return redirect('profile', id=id)
        else:
            messages.error(request, 'No changes made to your account details.')
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'edit_account_info.html', {'form': form, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.error(request, 'You must be logged in to edit account details.')
        return redirect('index')