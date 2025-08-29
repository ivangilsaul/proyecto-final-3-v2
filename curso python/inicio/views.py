from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Avion

def inicio(request):
    
    return render(request, "inicio/inicio.html")

    return HttpResponse(request, "inicio/inicio.html")

def crear_avion(request, marca, modelo, anio, color):

    avion = Avion(marca=marca, modelo=modelo, anio=anio, color=color)
    avion.save()

    return render(request, "inicio/crear_avion.html")

def crear_avionv2(request):
    if request.method == "POST":
        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")
        anio = request.POST.get("anio")
        color = request.POST.get("color")

        avion = Avion(marca=marca, modelo=modelo, anio=anio, color=color)
        avion.save()

        return render(request, "inicio/crear_avion.html")
    return render(request, "inicio/crear_avion.html")