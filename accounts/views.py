from django.shortcuts import render, HttpResponse


def profile_view(request):
    return render(request, 'accounts/profile.html')
