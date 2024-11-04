from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def mymusic(request):
    return render(request, 'mymusic.html')
