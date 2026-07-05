from django.urls import path
from .views import register, user_login, user_logout, user_home
from . import views

urlpatterns = [
    path('',views.user_home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]