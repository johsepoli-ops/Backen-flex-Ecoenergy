# Registro de Uso de Inteligencia Artificial — Fase 1 (EcoEnergy)

## 1. Herramienta utilizada
- **IA:** Gemini (Google)

## 2. Prompts principales y finalidad
- **Configuración y entorno:** Consultas para resolver errores de rutas, ejecución en terminal (`PowerShell`), ejecución de migraciones y arranque de `runserver`.
- **Capa de Servicios (`services.py`):** Apoyo en la estructura de lectura de archivos JSON (`pathlib`, `json.load`) para desacoplar los datos de la vista.
- **Vistas y plantillas:** Ajustes en `dispositivos/views.py` para calcular totales/activos y renderizar plantillas dinámicas.
- **Estilos:** Integración y configuración de `django-bootstrap5` en `settings.py` y `base.html`.

## 3. Partes adaptadas e integradas por el estudiante
- Estructuración manual de las carpetas y archivos (`data/dispositivos.json`, `templates/`, `services.py`).
- Corrección de rutas en `dispositivos/urls.py` para evitar errores de atributos inexistentes.
- Verificación de la herencia de plantillas (`{% extends "base.html" %}`).
- Pruebas manuales en navegador y depuración de errores (`FileNotFoundError`, `AttributeError`).

## 4. Pruebas y validaciones realizadas
- Comprobación del servidor Django en ejecución continua (`http://127.0.0.1:8000/`).
- Verificación de renderizado de la ruta raíz (`/`) y del catálogo de dispositivos (`/dispositivos/`).
- Comprobación del cálculo dinámico de dispositivos totales y activos.

## Fase 2: Resumen de Consumo por Zona
- **Herramienta:** Gemini
- **Prompts utilizados:**
  - Consulta para implementar la regla de negocio de estados `DENTRO DEL LÍMITE` y `LÍMITE SUPERADO` con separación MVT.
  - Asistencia en la resolución del cierre del servidor de desarrollo con autoreload en Python.
- **Cambios propios y verificación:**
  - Se probó la vista `/resumen-zonas/` en el navegador verificando los tres totales generales y la tabla de resumen.
  - Se confirmó el cumplimiento de la regla 3.3 con zonas con consumo sobre y bajo el límite.