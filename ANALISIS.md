# Análisis de Desarrollo y Decisiones Técnicas — EcoEnergy (Fase 1)

## 1. Modelo de Datos y Relaciones
El sistema no utiliza ORM ni base de datos relacional tradicional, sino tres colecciones en formato JSON desacopladas en la carpeta `data/`:
- **Zona (1) a Dispositivo (0..N):** Relación mediante la clave foránea `zona_id`.
- **Categoría (1) a Dispositivo (0..N):** Relación mediante la clave foránea `categoria_id`.

```text
[Zona: id, nombre, limite_kwh] 
       │ 1
       │ 0..N
[Dispositivo: id, nombre, consumo_kwh, zona_id, categoria_id]
       │ 0..N
       │ 1
[Categoría: id, nombre, descripcion]