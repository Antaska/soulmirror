from django.urls import path
from .views import cargar_preguntas, pregunta_diaria

urlpatterns = [
    path("cargar-preguntas/", cargar_preguntas, name="cargar_preguntas"),
    path("pregunta-diaria/", pregunta_diaria, name="pregunta_diaria"),
]