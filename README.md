# 🌌 AI Cinema Lab — "The Silent Edge"

*Hecho con amor y estilo por Miguel Ángel Carvajal (tu servilleta) & Antigravity (Google DeepMind) 🎬🖤*

Este repositorio contiene la arquitectura de plataforma, el motor de procesamiento de video por IA y la documentación técnica del cortometraje SRE Cyberpunk **"The Silent Edge"**.

El proyecto demuestra cómo desplegar un flujo automatizado de generación de video utilizando las APIs de **Google Cloud Vertex AI** (modelos Veo e Imagen Video), aplicando estrictos controles de gobernanza de costos (**FinOps**) y procesamiento de montaje automatizado.

---

## 🏗️ ESTRUCTURA DEL PROYECTO

```text
ai-cinema-lab/
├── README.md               # Esta documentación general
├── pitch_script.md         # Guion técnico e investor pitch (12 segundos)
├── config.json             # Configuración de límites FinOps y parámetros de la API
├── render_movie.py         # Script maestro de Python para generación y stitching
├── requirements.txt        # Dependencias de Python (Google Cloud SDK, moviepy)
└── assets/                 # Directorio para assets estáticos y semillas
    ├── seed_asset.png      # Tu imagen de entrada para Image-to-Video
    └── output/             # Videos renderizados intermedios y corto final
```

---

## 🎬 EL CORTOMETRAJE: "THE SILENT EDGE"

Un cortometraje de **12 segundos** que sigue a un ingeniero de SRE resolviendo un incidente de latencia crítica al borde de la red (Edge Nodes) en una Ciudad de México futurista durante la noche, terminando con la estabilidad del sistema al amanecer.

*   **Detalle completo del Guion y Storyboard:** Lee el documento **[Pitch & Script](pitch_script.md)**, diseñado para presentación ante inversores y especificación técnica de prompts.

---

## 💰 GOBERNANZA SRE & FINOPS

Para proteger el presupuesto operativo de este hobby/proyecto contra llamadas excesivas o loops de renderizado:
1.  **Presupuestos en GCP:** Configurado un presupuesto de alerta a los **$15.00 USD** mensuales.
2.  **Límite de Ejecución (Python Shield):** El script `render_movie.py` implementa un validador que consulta un archivo local de auditoría y bloquea la ejecución si el gasto estimado acumulado supera el límite configurado en `config.json`.
3.  **Prototipado Eficiente:** Iteraciones rápidas con resoluciones reducidas antes del renderizado final en 8K.
