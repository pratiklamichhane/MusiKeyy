from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout as auth_logout
from .forms import SignUpForm, ProfileForm
from .models import UserProfile 
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user  # Link the profile to the user
            profile.save()  # Save the profile data
            login(request, user)
            return redirect('index')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    
    return render(request, 'accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')


def loginstatus(request):
    return render(request, 'base_app/base.html', {'user': request.user})

@login_required
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'base_app/base.html', {'user_profile': user_profile})


def logout(request):
    auth_logout(request)
    return redirect('index')