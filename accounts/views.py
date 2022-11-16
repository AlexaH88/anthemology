from django.shortcuts import render


def signup(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def profile_view(request):
    return render(request, 'accounts/profile.html')


def logout(request):
    return render(request, 'accounts/logout.html')
