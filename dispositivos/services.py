import json
from django.conf import settings

def _cargar_json(nombre_archivo):
    ruta = settings.BASE_DIR / "data" / nombre_archivo
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError(f"Se esperaba una lista en {nombre_archivo}")
    return datos

def cargar_dispositivos():
    return _cargar_json("dispositivos.json")

def cargar_zonas():
    zonas = _cargar_json("zonas.json")
    dispositivos = cargar_dispositivos()
    
    # Calcular cantidad de dispositivos por cada zona (CA-02)
    for zona in zonas:
        zona["total_dispositivos"] = sum(
            1 for d in dispositivos if d.get("zona_id") == zona.get("id")
        )
    return zonas

def cargar_categorias():
    return _cargar_json("categorias.json")

def obtener_detalle_zona(zona_id):
    zonas = _cargar_json("zonas.json")
    zona = next((z for z in zonas if z.get("id") == zona_id), None)
    if not zona:
        return None

    dispositivos = cargar_dispositivos()
    categorias = {c["id"]: c for c in cargar_categorias()}

    dispositivos_zona = []
    consumo_total = 0.0

    for d in dispositivos:
        if d.get("zona_id") == zona_id:
            cat = categorias.get(d.get("categoria_id"), {"nombre": "Sin categoría", "descripcion": ""})
            dispositivos_zona.append({
                **d,
                "categoria_nombre": cat["nombre"],
                "categoria_descripcion": cat.get("descripcion", "")
            })
            consumo_total += float(d.get("consumo_kwh", 0))

    # Regla CA-05: ALERTA > limite_kwh / NORMAL <= limite_kwh
    estado_limite = "ALERTA" if consumo_total > zona.get("limite_kwh", 0) else "NORMAL"

    return {
        "zona": zona,
        "dispositivos": dispositivos_zona,
        "consumo_total": round(consumo_total, 2),
        "total_dispositivos": len(dispositivos_zona),
        "estado_limite": estado_limite,
    }