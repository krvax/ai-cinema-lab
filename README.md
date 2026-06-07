# 🌌 AI Cinema Lab

*Hecho con amor y estilo por Miguel Ángel Carvajal & Antigravity (Google DeepMind) 🎬🖤*

**AI Cinema Lab** es un estudio de producción de contenido comercial potenciado por IA, con gobernanza de costos integrada (FinOps). Combina generación de video por IA, prompt engineering avanzado y automatización de montaje para crear campañas publicitarias de alta calidad a una fracción del costo de producción tradicional.

---

## 🏗️ Estructura del Proyecto

```text
ai-cinema-lab/
├── README.md                     # Esta documentación general
├── index.html                    # 🎨 Pitch Deck interactivo (SRE Cyberpunk)
├── pitch_script.md               # Guion técnico e investor pitch
├── resumen_ejecutivo.md          # Resumen ejecutivo para inversionistas
├── resumen_ejecutivo.pdf         # PDF generado del resumen
├── config.json                   # Configuración de límites FinOps
├── render_movie.py               # Script maestro de generación y stitching
├── generate_beautiful_pdf.py     # Generador de PDF con diseño premium
├── requirements.txt              # Dependencias Python (Google Cloud SDK, moviepy)
├── .gitignore
├── assets/                       # Assets globales del studio
│   ├── seed_asset.png
│   └── output/                   # Videos renderizados (gitignored)
└── campaigns/                    # 📂 Campañas de clientes
    └── rjc-funda/                # 🍺 Primera campaña: FundaCerveza R&JC
        ├── README.md
        ├── creative-brief.md     # Insight, buyer persona, 3 versiones A/B/C
        ├── pitch-strategy.md     # Estrategia de pitch para CFOs
        ├── produccion.md         # Matriz de experimentación & brand safety
        ├── storyboard.md         # Storyboard visual con shots generados por IA
        ├── gallery.md            # Galería de fotos de producto (proporciones reales)
        ├── storyboard-tactico.html    # Export Stitch: versión táctica
        ├── storyboard-lifestyle.html  # Export Stitch: versión lifestyle
        ├── storyboard-real.html       # Export Stitch: versión real
        └── assets/               # Imágenes de la campaña
            ├── storyboard_shot_1.png
            ├── storyboard_shot_2.png
            ├── storyboard_shot_3.png
            ├── storyboard_shot_4.png
            ├── funda_camuflaje.png
            └── funda_reveal.png
```

---

## 🎨 Pitch Deck Interactivo

El archivo [`index.html`](./index.html) contiene una presentación interactiva con temática **SRE Cyberpunk** diseñada para inversionistas. Incluye:

- **Hero Section** con reproductor de video placeholder y telemetría overlay
- **Widget de FinOps en tiempo real** mostrando el estado del presupuesto (actualmente en alerta: $16.50 consumidos vs $10.00 autorizados)
- **Pipeline de Producción** visual con pasos animados (Brief → Storyboard → Production → Delivery)
- **Galería de Output** con storyboard cards interactivos
- **Métricas de Producción**: 15s de comercial, $12.72 de render cost, 92% de reducción de costos

### Design System
- **Fonts**: Space Grotesk (headlines), Inter (body), JetBrains Mono (labels/telemetry)
- **Palette**: Midnight Black `#131313`, Neon Teal `#00FFCC`, Glass surfaces
- **Effects**: Glassmorphism, neon bloom shadows, mouse-tracking radial gradients, intersection observer animations

---

## 📂 Campañas

### 🍺 [R&JC FundaCerveza](./campaigns/rjc-funda/)
Primera campaña producida por AI Cinema Lab. Funda térmica de silicón para latas de cerveza de 473ml que imita una lata de refresco de cola.

**Entregables:**
- 3 versiones de comercial TikTok/Reels (A/B/C testing)
- 4 ángulos de experimentación psicológica
- Storyboard visual de 4 tomas generado con IA
- Fotos de producto con escala realista (prompt engineering avanzado)
- Exports interactivos de Stitch (3 variantes de storyboard)

---

## 🎬 El Cortometraje: "THE SILENT EDGE"

Un cortometraje de **12 segundos** que sigue a un ingeniero de SRE resolviendo un incidente de latencia crítica al borde de la red (Edge Nodes) en una Ciudad de México futurista durante la noche, terminando con la estabilidad del sistema al amanecer.

*   **Detalle completo:** [Pitch & Script](pitch_script.md)

---

## 💰 Gobernanza SRE & FinOps

Para proteger el presupuesto operativo contra llamadas excesivas o loops de renderizado:

1. **Presupuestos en GCP:** Alerta configurada. Actualmente en **breach** ($16.50 USD consumidos vs $10.00 USD autorizados → ~$296.60 MXN en GCP).
2. **Python Shield:** `render_movie.py` implementa un validador que bloquea ejecución si el gasto supera el límite de `config.json`.
3. **Prototipado $0:** Iteraciones con herramientas gratuitas (Nano Banana para imágenes, Stitch para storyboards) antes de gastar créditos en Veo/Imagen.

---

## 🛠️ Stack Tecnológico

| Herramienta | Rol | Costo |
|---|---|---|
| Google Veo | Generación Text-to-Video / Image-to-Video | $0.15-$0.18/s |
| Google Flow | Pipeline cinematográfico (consistencia visual) | Incluido |
| Google Whisk | Pre-producción (moodboards rápidos) | Incluido |
| Stitch MCP | Diseño de UI / Storyboards interactivos | $0 |
| Nano Banana | Generación de imágenes de producto | $0 |
| MoviePy | Ensamblaje automatizado de video | $0 |
| NotebookLM | Estrategia de marca / Contexto del cliente | $0 |

---

## 🚀 Cómo Ejecutar

```bash
# Ver el Pitch Deck interactivo
python -m http.server 8080
# → Abrir http://localhost:8080

# Generar PDF del resumen ejecutivo
python generate_beautiful_pdf.py

# Renderizar cortometraje (requiere GCP + créditos)
python render_movie.py
```
