from django.shortcuts import render, HttpResponse


def accounts_test(request):
    return HttpResponse("Accounts Working!")
