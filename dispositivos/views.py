from django.shortcuts import render
from django.http import Http404
from .services import cargar_dispositivos, cargar_zonas, obtener_detalle_zona

def inicio(request):
    zonas = cargar_zonas()
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
        "zonas": zonas,
    }
    return render(request, "dispositivos/inicio.html", contexto)

def catalogo(request):
    dispositivos = cargar_dispositivos()
    activos = sum(1 for item in dispositivos if item.get("estado") == "Activo")
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(request, "dispositivos/catalogo.html", contexto)

def detalle_zona(request, zona_id):
    datos_zona = obtener_detalle_zona(zona_id)
    if not datos_zona:
        raise Http404("Zona no encontrada")
    return render(request, "dispositivos/detalle_zona.html", datos_zona)