from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('authentication.urls'), name="homeAuth"),
    path("home", views.home, name="home"),
    path("result/", views.result, name="result"),
]
