# 🎬 PITCH & SCRIPT: THE SILENT EDGE

**Un corto cinematográfico SRE Cyberpunk**  
*Optimizado para Generación con Google Cloud Vertex AI (Veo / Imagen Video)*  
*Diseñado por Miguel Ángel Carvajal & Antigravity (Google DeepMind)*  

---

## 💡 LOGLINE & CONCEPTO DE NEGOCIO (Investor Pitch)

> *En una Ciudad de México futurista sumergida bajo la lluvia, un Ingeniero de Confiabilidad de Sitio (SRE) libra una batalla silenciosa contra la degradación de un nodo crítico en el borde del continente, antes de que el tráfico digital de millones de personas colapse.*

### La Oportunidad (GenAI + Platform Engineering)
Este proyecto demuestra cómo la automatización de infraestructura SRE y la Inteligencia Artificial Generativa permiten crear **contenido cinematográfico de alta fidelidad con presupuestos ultra-efectivos**. En lugar de requerir un equipo de filmación, sets físicos y semanas de renderizado en granjas tradicionales, utilizamos pipelines de **Vertex AI** controlados por código, con un costo de producción estimado en **menos de $5 USD** para el render final.

---

## 📽️ EL GUION CINEMATOGRÁFICO Y STORYBOARD

El corto tiene una duración total de **12 segundos**, estructurado en tres escenas continuas de 4 segundos cada una.

```
+-----------------------------------------------------------------------+
|                              SCENE FLOW                               |
|                                                                       |
|   [ Scene 1: The Alert ]  ===>  [ Scene 2: The Remediation ] ===>     |
|   (0:00 - 0:04)                 (0:04 - 0:08)                         |
|   "Foco en el Ingeniero"        "Holograma de Red & Assets"           |
|                                                                       |
|                     ===> [ Scene 3: The Sunrise ]                     |
|                          (0:08 - 0:12)                                |
|                          "Estabilización y Skyline CDMX"              |
+-----------------------------------------------------------------------+
```

---

### 🎬 ESCENA 1: THE ALERT (00:00 - 00:04)

*   **Enfoque Visual:** Plano medio corto (Medium Close-Up) con lente anamórfico. Un ingeniero de sistemas (SRE) de perfil, sentado en una silla ergonómica erguida. Viste una chaqueta técnica impermeable oscura. Luces de neón púrpura y azul se reflejan en su rostro húmedo por la llovizna. De fondo, a través de una ventana de cristal con gotas de agua escurriendo, se ven los rascacielos borrosos de la Condesa envueltos en bruma cyberpunk.
*   **Acción:** Sus lentes de realidad aumentada parpadean con un brillo rojo tenue. Su mirada se tensa ligeramente al detectar una alerta.
*   **Audio (Sonido):** Sonido ambiental de lluvia constante chocando contra el cristal. Un zumbido electrónico de baja frecuencia (low-hum) de fondo. Un pitido sintético suave y repetitivo (tono de alerta).
*   **Vertex AI Prompt (Text-to-Video / Image-to-Video):**
    > `"Cinematic medium close-up, cyberpunk SRE engineer wearing glowing AR glasses reflecting subtle red alert data, neon purple and teal light accents, raindrops on window in background, blurred futuristic skyline of Mexico City at night, rainy atmosphere, photorealistic, 8k resolution, anamorphic lens, 24fps."`

---

### 🎬 ESCENA 2: THE REMEDIATION (00:04 - 00:08)

*   **Enfoque Visual:** Plano detalle (Close-Up) de la interfaz holográfica flotando frente al ingeniero. La interfaz es un mapa tridimensional de nodos de red globales con líneas de tráfico que conectan continentes.
*   **Integración del Asset del Usuario:**
    > ⚠️ **[HOOCK DE ASSET]:** En esta escena se proyectará el logotipo o la interfaz propietaria del usuario (imagen de entrada semilla) para hacer un renderizado **Image-to-Video**. El mapa de red colapsado transiciona suavemente a medida que el algoritmo de IA inyecta movimiento al asset base, transformándolo en un nodo de red que se estabiliza.
*   **Acción:** Un nodo parpadea en rojo brillante con la palabra `LATENCY CRITICAL`. Tras un ligero movimiento de dedos del ingeniero en el aire, el nodo se torna verde brillante y la palabra cambia a `STABLE`.
*   **Audio (Sonido):** Un barrido de frecuencias agudas (UI sound effect) when the interaction is made in the air. The ambient music (atmospheric synthwave) rises slightly, changing from tension to resolution.
*   **Vertex AI Prompt (Imagen-to-Video):**
    > `"Close-up of a glowing 3D holographic network interface floating in the air, a critical node transitions from blinking red to solid emerald green with cybernetic glyphs, fingers gently swiping through the digital light, high-tech HUD, volumetric lighting, dark room, highly detailed, octane render, 4k."`

---

### 🎬 ESCENA 3: THE SUNRISE (00:08 - 00:12)

*   **Enfoque Visual:** Plano general (Wide Shot) de la ventana. El ingeniero se quita lentamente los lentes de realidad aumentada y mira a través del cristal. Afuera, la lluvia ha parado y el primer rayo de sol del amanecer corta la niebla, tiñendo el skyline de rascacielos de la Condesa y Reforma con tonos anaranjados y dorados cálidos que contrastan con los anuncios de neón apagándose.
*   **Acción:** El reflejo en el cristal muestra la calma del ingeniero al ver el sistema estabilizado al amanecer. El corto termina con un fade-out a negro.
*   **Audio (Sonido):** La lluvia cesa. Un acorde de sintetizador cálido y expansivo (estilo Vangelis / Blade Runner) entra en crescendo. Sonido lejano de la ciudad despertando.
*   **Vertex AI Prompt (Text-to-Video):**
    > `"Wide cinematic shot of a futuristic control room with a massive glass window, a programmer looking out at a cyberpunk Mexico City skyline during sunrise, warm golden and orange light cutting through morning fog, neon lights turning off, slow camera pull back, peaceful mood, photorealistic, 8k, highly detailed."`

---

## 📊 LEDGER DE COSTOS SRE & FINOPS (Para los Inversores)

La ventaja competitiva de nuestro motor de render frente a la animación tradicional es el costo escalable:

| Elemento | Consumo Estimado | Costo Unitario (GCP Vertex) | Costo Total Estimado |
| :--- | :--- | :--- | :--- |
| **Generación Escena 1** | 4 segundos de video | $0.15 USD / seg (Veo) | **$0.60 USD** |
| **Generación Escena 2 (Img-to-Vid)** | 4 segundos de video | $0.18 USD / seg (Veo) | **$0.72 USD** |
| **Generación Escena 3** | 4 segundos de video | $0.15 USD / seg (Veo) | **$0.60 USD** |
| **Post-Procesamiento (Stitching)** | Local (CPU / moviepy) | $0.00 USD (Compute gratis) | **$0.00 USD** |
| **Búfer de Iteración (10 tomas)** | 30 seg de prueba | Promedio ponderado | **$4.50 USD** |
| **COSTO TOTAL DEL PROYECTO** | **12s Finales + Pruebas** | **Límite FinOps configurado**| **$6.42 USD** |

---

## 🛠️ CÓMO CORRER LA PIPELINE (Instrucciones Técnicas)

1.  **Coloca tu asset semilla:** Guarda tu imagen o asset en la ruta `coatl-tech/ai-cinema-lab/assets/seed_asset.png`.
2.  **Configura las credenciales:** Corre `gcloud auth application-default login` en tu terminal.
3.  **Ejecuta el renderizador:**
    ```bash
    python render_movie.py --config config.json
    ```
