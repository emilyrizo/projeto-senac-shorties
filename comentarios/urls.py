from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('feedbacks', views.comentarios, name='comentarios'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.exibe, name='mostrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    # path('localizar/',views.localizar,name='localizar'),
    # path('localizarmais/',views.localizarmais,name='localizarmais'),
]