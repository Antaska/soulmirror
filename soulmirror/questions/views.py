from django.shortcuts import render
from django.contrib import messages
from .models import Question

# Create your views here.

def cargar_preguntas(request):
    if request.method == "POST" and request.FILES.get("archivo_preguntas"):
        archivo = request.FILES["archivo_preguntas"]
        lineas = archivo.readlines()

        cargadas = 0
        ignoradas = 0

        for linea in lineas:
            try:
                linea = linea.decode("utf-8").strip()

                if not linea or "." not in linea or "[" not in linea or "]" not in linea:
                    ignoradas += 1
                    continue

                partes = linea.split(".",1)
                numero = partes[0].strip()
                contenido = partes[1].strip()
                if "[" not in contenido or "]" not in contenido:
                    ignoradas += 1
                    continue

                tematica = contenido[contenido.find("[") + 1 : contenido.find("]")]
                pregunta = contenido[contenido.find("]") + 1 :].strip()

                if Question.objects.filter(tematica=tematica, pregunta=pregunta).exists():
                    ignoradas += 1
                    continue

                Question.objects.create(tematica=tematica, pregunta=pregunta)
                cargadas += 1
            
            except Exception as e:
                ignoradas += 1
                continue

        messages.success(request, f"{cargadas} preguntas cargadas correctamente.")
        messages.warning(request, f"{ignoradas} líneas ignoradas (duplicadas o mal formateadas).")
    
    return render(request, "cargar_preguntas.html")
