from django.urls import path
from DtechApp import views
urlpatterns = [
    path('', views.Home, name="home"),
]