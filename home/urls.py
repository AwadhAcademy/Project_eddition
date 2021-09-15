from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about_us', views.about,name="about"),
    path('sign_in', views.sign_in,name="sign_in"),
    path('user_planer', views.user_planer,name="user_planer"),
    path('project', views.project,name="project"),
]
