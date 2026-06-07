# 🎬 AI Cinema Lab: Bitácora de Producción y FinOps
## Campaña: R&JC Funda Térmica (FundaCerveza)

Este documento centraliza el registro de producción, el inventario de assets y la auditoría financiera (FinOps) de la campaña publicitaria de generación automática por IA para la funda térmica de camuflaje R&JC.

---

## 💰 1. Auditoría Financiera y Reporte de FinOps (GCP)

Durante la corrida de generación con los modelos de video de **Vertex AI (Veo 2.0)**, se realizó un monitoreo constante del gasto y se detectó un rebase en el presupuesto debido a los altos costos de procesamiento de video por segundo. A continuación se detalla la conciliación oficial extraída de la consola de GCP:

### 📊 Estado de Facturación (1 al 6 de junio, 2026)
*   **Cuenta de Facturación:** `coatl-tech-invoices` (ID: `01631D-150EE6-3A2497`)
*   **Proyecto Asociado:** `AI Condesa Workshop 02` (`mx-coatl-aicondesa-workshop02`)
*   **Servicio:** Vertex AI (SKU: `Veo 2 Video Generation`)
*   **Región:** `us-central1`
*   **Costo Bruto de Uso:** $477.00 MXN
*   **Descuentos y Ahorros Aplicados:** -$180.40 MXN
*   **Costo Neto Cobrado:** **$296.60 MXN**

### 🚨 Alerta de Presupuesto
*   **Presupuesto Configurado:** **$10.00 USD / mes** (~$200.00 MXN)
*   **Nombre de Alerta:** `$10 Alerta de presupuesto mensual`
*   **Incidente:** El 6 de junio de 2026 a la 1:19 AM se recibió una alerta crítica de **150% del presupuesto alcanzado**. El costo neto ($296.60 MXN) excedió el límite de alerta establecido.
*   **Mitigación Ejecutada:** Se detuvieron de inmediato las llamadas de generación de video directo en GCP, migrando a flujos locales de post-producción y edición de video con `moviepy` ($0 costo).

---

## 🖼️ 2. Banco de Imágenes Semilla (Seeds)

Para mantener la consistencia visual del producto a lo largo de las distintas escenas animadas por la IA, se utilizaron las siguientes imágenes base cargadas en el bucket `gs://mx-coatl-aicondesa-workshop02-seeds/`:

1.  **`can_sleeve_closeup.png`**: Toma cerrada en plano macro de la funda de silicona roja sobre una mesa de madera de oficina. Utilizado para las escenas de transformación y showcase en escritorio.
2.  **`beach_usage.png`**: Toma de producto contextualizada en exterior (playa). Utilizada para las tomas de estilo de vida al aire libre.
3.  **`seed_asset.png`**: Imagen de referencia del empaque y diseño del producto.

---

## 🧱 3. Inventario de Escenas Generadas (Bloques Modulares)

En el bucket de GCS se generaron **14 archivos mp4 de prueba** correspondientes a 3 tipos de escenas (gancho, ASMR térmico, y estilo de vida). Estos archivos se descargaron localmente en la ruta `/mnt/e/work/rjc-videos/` conservando sus IDs únicos:

| Escena Local / GCS | Tipo de Escena | Descripción Visual / Prompt | Peso |
| :--- | :--- | :--- | :--- |
| **`scene1_transform.mp4`** | Escena 1 (Reveal) | La funda de silicona roja se desliza suavemente sobre una lata de aluminio. | 1.3 MB |
| **`scene1_disguise.mp4`** | Escena 1 (Camuflaje) | Mano deslizando la funda roja para revelar el borde metálico de la cerveza. | 1.4 MB |
| **`scene1_alert.mp4`** | Escena 1 (Gancho) | Variación rápida del reveal con enfoque de cámara instantáneo. | 0.9 MB |
| **`scene1_product.mp4`** | Escena 1 (Producto) | Vista cenital de la lata cubierta en escritorio. | 1.2 MB |
| **`scene2_thermal.mp4`** | Escena 2 (ASMR) | Gotas de condensación helada deslizándose por el silicón (efecto frío). | 2.2 MB |
| **`scene2_showcase.mp4`** | Escena 2 (Producto) | Acercamiento lento (slow push-in) a la funda en el escritorio de oficina. | 1.2 MB |
| **`scene2_lifestyle.mp4`** | Escena 2 (Contexto) | Uso de la funda en una reunión informal de amigos de fondo. | 1.4 MB |
| **`scene2_remediation.mp4`**| Escena 2 (Textura) | Detalle macro del acabado mate del silicón rojo. | 1.1 MB |
| **`scene3_lifestyle.mp4`** | Escena 3 (Cierre) | El producto integrado en uso continuo en un día caluroso. | 1.4 MB |
| **`scene3_sunrise.mp4`** | Escena 3 (Outro) | Toma final con iluminación dorada/tarde de fondo para dar cierre. | 1.0 MB |

---

## 🎬 4. Estructura de los Cortes Finales

Los bloques de construcción anteriores se combinaron en **3 cortes finales** con diferentes duraciones y propósitos publicitarios. 

Estos archivos fueron organizados y copiados en una nueva carpeta limpia en tu disco local para que los puedas compartir fácilmente:
📁 **`/mnt/e/work/rjc-videos-finales/`**

### 🎥 1. `01_silicone_sleeve_pitch_final.mp4` (Comercial Completo - 15s)
*   **Composición:** Escena 1 (Reveal/Transformation) + Escena 2 (ASMR Térmico/Gotas) + Escena 3 (Lifestyle/Cierre).
*   **Propósito:** Video principal para la presentación comercial y campaña completa. Cuenta la historia completa del producto (camuflaje, aislamiento y estilo de vida).

### 🎥 2. `02_the_silent_edge_final.mp4` (Corte Cinemático - 10s)
*   **Composición:** Escena 1 (Reveal Alternativo) + Escena 2 (Detalle ASMR).
*   **Propósito:** Enfoque estético y premium, ideal para campañas inmersivas en Instagram y TikTok sin diálogos directos, apoyándose 100% en la música de fondo.

### 🎥 3. `03_hide_in_plain_sight.mp4` (Corte Rápido de Producto - 10s)
*   **Composición:** `scene1_transform.mp4` + `scene2_showcase.mp4`.
*   **Propósito:** Diseñado específicamente para ganchos publicitarios veloces (el reveal ocurre antes de los 3 segundos en el escritorio de la oficina). Excelente para pautas de retención agresiva.
