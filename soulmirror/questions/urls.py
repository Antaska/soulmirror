from django.urls import path
from .views import cargar_preguntas, pregunta_diaria, estado_general

urlpatterns = [
    path("cargar-preguntas/", cargar_preguntas, name="cargar_preguntas"),
    path("pregunta-diaria/", pregunta_diaria, name="pregunta_diaria"),
    path("estado-general/", estado_general, name="estado_general"),
]