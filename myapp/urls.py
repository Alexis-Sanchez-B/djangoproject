#Este archivo se debe crear a mano para sincronizar correctamente urls.py del proyecto principal mysite
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:username>',views.hello),
    path('projects/',views.projects),
    path('tasks/',views.tasks)
]