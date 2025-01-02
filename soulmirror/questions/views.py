from django.shortcuts import render
from django.contrib import messages
from django.utils.timezone import now
from .models import Question
import random
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

def pregunta_diaria(request):
    ultima_pregunta = Question.objects.filter(respondida__isnull=False).order_by('-respondida').first()
    ultima_tematica = ultima_pregunta.tematica if ultima_pregunta else None

    preguntas_disponibles = Question.objects.filter(
        respondida__isnull=True
    ).exclude(tematica=ultima_tematica)

    if preguntas_disponibles.exists():
        pregunta = random.choice(preguntas_disponibles)
        Question.objects.filter(id=pregunta.id).update(respondida=now())
        pregunta.refresh_from_db()
        return render(request, "pregunta_diaria.html",{"pregunta":pregunta})
    else:
        return render(request, "no_preguntas.html")
    
def estado_general(request):
    tematica_filtro = request.GET.get("tematica", None)
    estado_filtro = request.GET.get("estado", None)

    preguntas = Question.objects.all()

    if tematica_filtro:
        preguntas = preguntas.filter(tematica__icontains=tematica_filtro)
    
    if estado_filtro == "respondida":
        preguntas = preguntas.filter(respondida__isnull=False)
    elif estado_filtro == "no_respondida":
        preguntas = preguntas.filter(responida__isnull=True)

    return render(request, "estado_general.html", {"preguntas":preguntas})