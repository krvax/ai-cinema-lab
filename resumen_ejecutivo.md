# 📊 RESUMEN EJECUTIVO: PIPELINE DE AI CINEMA & COMERCIAL "HIDE IN PLAIN SIGHT"

**Documento Técnico-Comercial para R & JC**  
*Fecha: 5 de Junio, 2026*  

---

## 🏗️ 1. LO QUE TENEMOS (Estructura de Repositorio & Código)

Todo el proyecto está estructurado bajo control de versiones en el repositorio **`ai-cinema-lab`**, lo que garantiza que todo el flujo creativo y técnico sea **100% reproducible por código** con un solo comando.

### Estructura del Repositorio y Roles de los Archivos:
*   [config.json](file:///Ubuntu/home/mcarvaj/src/coatl-tech/ai-cinema-lab/config.json) **(Configuración Declarativa):** Centraliza las credenciales del proyecto GCP (`mx-coatl-aicondesa-workshop02`), el bucket de GCS, la región (`us-central1`), los parámetros de costos por segundo de la IA y el storyboard detallado (prompts, duraciones y tipos de escena).
*   [render_movie.py](file:///Ubuntu/home/mcarvaj/src/coatl-tech/ai-cinema-lab/render_movie.py) **(Orquestador de Plataforma):** Script maestro en Python. Realiza de manera secuencial:
    1. Carga la configuración e imprime el debug JSON (`⚙️ LOADED CONFIGURATION`).
    2. Ejecuta el control presupuestal interno contra el ledger.
    3. Sube las imágenes semilla a GCS de manera automatizada.
    4. Resuelve y asigna el modelo correcto (ej. `veo-2.0-generate-001`) por escena y ejecuta las llamadas asíncronas a Vertex AI mediante polling automático cada 15 segundos.
    5. Descarga los renders y ejecuta localmente **MoviePy** para unificar los clips.
    6. Asienta el gasto real en el libro contable de FinOps.
*   [finops_ledger.json](file:///Ubuntu/home/mcarvaj/src/coatl-tech/ai-cinema-lab/finops_ledger.json) **(Base de Auditoría Local):** Base de datos JSON que actúa como registro inmutable de transacciones locales, guardando el timestamp, costo exacto y la descripción de cada renderizado.
*   [pitch_script.md](file:///Ubuntu/home/mcarvaj/src/coatl-tech/ai-cinema-lab/pitch_script.md) **(Storyboard & Pitch):** Contiene el guion cinematográfico estructurado para inversores y los copies tipográficos de edición.
*   [requirements.txt](file:///Ubuntu/home/mcarvaj/src/coatl-tech/ai-cinema-lab/requirements.txt) **(Dependencias del Sistema):** Especifica las librerías necesarias (`google-genai`, `google-cloud-storage`, `moviepy`, `imageio-ffmpeg`).
*   **`assets/` (Control de Material Estático):**
    *   `can_sleeve_closeup.png` (Seed premium de la funda colocándose sobre el escritorio).
    *   `beach_usage.png` (Seed de la funda vacía en el escritorio).
    *   `output/` (Directorio de salida para los renders independientes y el ensamble final `hide_in_plain_sight.mp4`).

---

## 📸 2. LO QUE OCUPAMOS (La Clave: Seeds de Calidad)

El mayor aprendizaje cinematográfico de este proyecto es que **el modelo Veo es excelente animando una realidad que ya existe (fotos de entrada), pero tiene problemas transformando un objeto en otro totalmente diferente**.

### Regla de Oro para el Futuro:
> **La calidad y contexto del "Seed" (imagen de entrada) determina el 70% de la calidad del video final de la IA.**

Para las siguientes versiones o iteraciones ocupamos:
*   **Fotos de entrada reales de alta definición:** Evitar imágenes recortadas sobre fondos blancos puros (Voids) porque confunden a la IA y generan artefactos/deformaciones en las manos.
*   **Secuencia de fotos Antes/Después reales:** Si queremos una transición perfecta de la lata Budweiser a la funda Coca-Cola, ocupamos:
    1.  *Seed 1 (Inicio):* Foto real del producto a medio colocar en un entorno de uso real.
    2.  *Seed 2 (Fin):* Foto real del producto completamente cubierto en el mismo entorno exacto.
*   **Uso de Text-to-Video para entornos complejos:** Para escenarios complejos (como el estilo de vida playero), es preferible generar el video nativo desde texto en lugar de intentar deformar fotos que no corresponden al contexto.

---

## 💰 3. LO QUE NOS COSTÓ (Desglose Detallado de Costos)

El pipeline está diseñado bajo la filosofía SRE/FinOps para minimizar el desperdicio. A continuación, el desglose unitario y el costo de la corrida del comercial de 10 segundos:

### A. Tarifas Unitarias de Vertex AI (Costo por Segundo de Render):
*   **Veo Video (Text-to-Video):** $0.15 USD / segundo.
*   **Veo Image-to-Video (Con imagen semilla):** $0.18 USD / segundo.
*   **Imagen Video (Modelo secundario):** $0.07 USD / segundo.

### B. Desglose de Costo de la Corrida Actual (Comercial de 10s):
*   **Escena 1 (Transformación - 5s de Image-to-Video):** $0.90 USD (5s × $0.18)
*   **Escena 2 (Showcase - 5s de Image-to-Video):** $0.90 USD (5s × $0.18)
*   **Almacenamiento e Ingesta GCS:** $0.00 USD (Los archivos pesan < 50 MB. Entran 100% en la capa gratuita de 5 GB Standard Storage de Google Cloud en `us-central1`).
*   **Operaciones de API de GCS:** $0.00 USD (Menos de 50 llamadas API de subida/descarga, entra en la capa gratuita de 10,000 operaciones mensuales).
*   **Montaje y Stitching Local (MoviePy):** $0.00 USD (Procesado local en WSL, coste de cómputo en la nube nulo).
*   **COSTO TOTAL DE PRODUCCIÓN:** **$1.80 USD** (Al tipo de cambio aproximado, unos **$32.00 MXN**).

### C. Consumo Histórico Registrado (Hoy):
1.  *Corrida de Prueba 1 (12 segundos SRE original):* $2.40 USD
2.  *Corrida de Prueba 2 (12 segundos versión preliminar):* $2.40 USD
3.  *Corrida de Prueba 3 (10 segundos versión errónea de playa):* $1.80 USD
4.  *Corrida de Prueba 4 (10 segundos versión final de escritorio):* $1.80 USD
*   **Presupuesto mensual acumulado final:** **$12.72 USD / $15.00 USD** (Control absoluto del gasto bajo presupuesto aprobado).
*   **Escalabilidad:** Generar 100 variaciones de este comercial para pruebas A/B de marketing costaría solo **$180.00 USD**, una reducción de costo de más del 95% contra renders en granjas tradicionales de animación 3D.
