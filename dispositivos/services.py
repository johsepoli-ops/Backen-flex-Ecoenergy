import json
import os
from django.conf import settings

DATA_DIR = os.path.join(settings.BASE_DIR, 'data')

def cargar_json(nombre_archivo):
    ruta = os.path.join(DATA_DIR, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def cargar_zonas():
    return cargar_json('zonas.json')

def cargar_categorias():
    return cargar_json('categorias.json')

def cargar_dispositivos():
    return cargar_json('dispositivos.json')

def obtener_detalle_zona(zona_id):
    zonas = cargar_zonas()
    categorias = cargar_categorias()
    dispositivos = cargar_dispositivos()
    
    zona = next((z for z in zonas if z.get("id") == zona_id), None)
    if not zona:
        return None
        
    categorias_map = {c["id"]: c["nombre"] for c in categorias}
    
    dispositivos_zona = []
    consumo_total = 0.0
    
    for d in dispositivos:
        if d.get("zona_id") == zona_id:
            disp_info = d.copy()
            disp_info["categoria_nombre"] = categorias_map.get(d.get("categoria_id"), "Sin Categoría")
            dispositivos_zona.append(disp_info)
            consumo_total += d.get("consumo_kwh", 0)
            
    estado_limite = "ALERTA" if consumo_total > zona.get("limite_kwh", 0) else "NORMAL"
    
    return {
        "zona": zona,
        "dispositivos": dispositivos_zona,
        "consumo_total": round(consumo_total, 2),
        "total_dispositivos": len(dispositivos_zona),
        "estado_limite": estado_limite
    }

def obtener_resumen_zonas():
    zonas = cargar_zonas()
    dispositivos = cargar_dispositivos()
    
    resumen_zonas = []
    total_consumo_general = 0.0
    
    for zona in zonas:
        dispositivos_zona = [d for d in dispositivos if d.get("zona_id") == zona["id"]]
        cantidad_disp = len(dispositivos_zona)
        consumo_total_zona = sum(d.get("consumo_kwh", 0) for d in dispositivos_zona)
        total_consumo_general += consumo_total_zona
        
        # Regla de negocio 3.3
        if consumo_total_zona <= zona["limite_kwh"]:
            estado = "DENTRO DEL LÍMITE"
            clase_estado = "success"
        else:
            estado = "LÍMITE SUPERADO"
            clase_estado = "danger"
            
        resumen_zonas.append({
            "id": zona["id"],
            "nombre": zona["nombre"],
            "cantidad_dispositivos": cantidad_disp,
            "consumo_total": round(consumo_total_zona, 2),
            "limite_kwh": zona["limite_kwh"],
            "estado": estado,
            "clase_estado": clase_estado
        })
        
    totales_generales = {
        "total_zonas": len(zonas),
        "total_dispositivos": len(dispositivos),
        "total_consumo": round(total_consumo_general, 2)
    }
    
    return resumen_zonas, totales_generales