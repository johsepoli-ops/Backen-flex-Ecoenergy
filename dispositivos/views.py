from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .services import cargar_zonas, obtener_detalle_zona, obtener_resumen_zonas

def inicio(request):
    zonas = cargar_zonas()
    return render(request, "dispositivos/inicio.html", {"zonas": zonas})

def detalle_zona(request, zona_id):
    detalle = obtener_detalle_zona(zona_id)
    if not detalle:
        raise Http404("La zona solicitada no existe.")
    return render(request, "dispositivos/detalle_zona.html", detalle)

def resumen_zonas(request):
    resumen, totales = obtener_resumen_zonas()
    context = {
        "resumen_zonas": resumen,
        "totales": totales,
    }
    return render(request, "dispositivos/resumen_zonas.html", context)