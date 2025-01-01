from django.urls import path
from .views import cargar_preguntas

urlpatterns = [
    path("cargar-preguntas/", cargar_preguntas, name="cargar_preguntas"),
]