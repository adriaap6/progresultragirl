from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path("", views.homeAuth, name="homeAuth"),
    path("signup", views.signup, name="signup"),
    path("homeAuth", views.homeAuth, name="homeAuth"),
    path("daftar", views.signup, name="daftar"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("activate/<str:uid64>/<str:token>", views.activate, name="activate"),
    path('verify/<str:uidb64>/<str:token>/', views.verify, name='verify'),
]   
