from django.urls import path
from .views import home, welcome, login, profile, mymusic
from django.contrib.auth import views as auth_views

app_name = 'music'

urlpatterns = [
    path('', home, name='home'),
    path('welcome', welcome, name='welcome'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('mymusic', mymusic, name='mymusic'),

]
