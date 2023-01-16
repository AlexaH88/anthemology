from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from songs.models import Song


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            messages.success(request, "Sign up successful!")
            return redirect('songs:user_songs')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if request.user.is_superuser:
                    messages.success(request, "Login successful!")
                    return redirect('accounts:admin')
                else:
                    messages.success(request, "Login successful!")
                    return redirect('songs:user_songs')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logout successful!")
        return redirect('songs:song_list')


@login_required(login_url="/accounts/login/")
def admin_view(request):
    songs = Song.objects.all().order_by('title')
    return render(request, 'accounts/admin.html', {'songs': songs})
