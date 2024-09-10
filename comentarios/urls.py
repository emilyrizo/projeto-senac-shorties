from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.comentarios, name='comentarios'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.exibe, name='mostrar'),
]