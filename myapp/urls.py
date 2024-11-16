#Este archivo se debe crear a mano para sincronizar correctamente urls.py del proyecto principal mysite
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('about/',views.about),
    path('perro/',views.perro)
]