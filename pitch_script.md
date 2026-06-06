# 🎬 PRODUCT PITCH & COMMERCIAL SCRIPT: HIDE IN PLAIN SIGHT (Kickstarter Edition)

**Un comercial ultra-corto de 10 segundos enfocado 100% en el producto físico**  
*Optimizado para Generación con Google Cloud Vertex AI (Veo 2.0 / Imagen Video)*  
*Diseñado por Miguel Ángel Carvajal & Antigravity (Google DeepMind)*  

---

## 💡 LOGLINE & CONCEPTO DE NEGOCIO (Investor Pitch)

> *Una funda protectora para bebidas que combina discreción y aislamiento térmico. En menos de 10 segundos el espectador entiende: qué hace el producto, cómo se usa y por qué es útil, eliminando cualquier distracción narrativa.*

### El Enfoque Kickstarter (Producto Puro)
El objetivo de este comercial es posicionar al producto como el protagonista absoluto. 

Al usar la misma imagen semilla premium en el escritorio de oficina (`assets/can_sleeve_closeup.png`) para ambas escenas, garantizamos una **consistencia visual perfecta del entorno (100%)**, logrando que la IA solo se preocupe por el movimiento de cámara y la animación física del producto.

---

## 📽️ EL GUION CINEMATOGRÁFICO Y STORYBOARD

El comercial tiene una duración total de **10 segundos**, estructurado en dos escenas de 5 segundos cada una.

```
+-----------------------------------------------------------------------+
|                              SCENE FLOW                               |
|                                                                       |
|             [ Scene 1: The Transformation ] (0:00 - 0:05)             |
|             "Primerísimo plano de la funda colocándose"               |
|                                                                       |
|                                 ===>                                  |
|                                                                       |
|             [ Scene 2: Product Showcase ] (0:05 - 0:10)               |
|             "Cercamiento lento al producto mostrando condensación"     |
+-----------------------------------------------------------------------+
```

---

### 🎬 ESCENA 1: THE TRANSFORMATION (00:00 - 00:05)

*   **Enfoque Visual:** Toma de producto macro y cinematográfica. Una mano desliza suavemente la funda de silicona roja sobre una lata de aluminio, ocultando la marca Budweiser y dejando ver el diseño de refresco. Entorno de oficina real y ordenado de fondo.
*   **Acción:** Demostración directa del uso y ajuste perfecto de la funda.
*   **Cámara:** Lente macro, plano detalle, poca profundidad de campo.
*   **Vertex AI Prompt (Image-to-Video - Veo 2.0):**
    > `"Cinematic macro product shot. A hand smoothly slides the red beverage sleeve over an aluminum can. Focus on the transformation. Premium product commercial. Realistic office environment. Shallow depth of field. Photorealistic."`

---

### 🎬 ESCENA 2: PRODUCT SHOWCASE (00:05 - 00:10)

*   **Enfoque Visual:** La lata de bebida completamente cubierta con la funda roja descansa con firmeza en el escritorio. Pequeñas gotas de condensación fría son visibles formándose lentamente en la superficie roja de la silicona, ilustrando el beneficio térmico secundario. Luces suaves de oficina reflejándose a través del material.
*   **Acción:** Resalte de la textura de la silicona, el acabado mate y el enfriamiento.
*   **Cámara:** Acercamiento cinematográfico lento (slow push-in) hacia el producto terminado.
*   **Edición y Post-Producción:** Agregar texto en tipografía blanca minimalista con un fade in/out suave:
    > **HIDE IN PLAIN SIGHT** o **Discreción nivel experto.** (segundos 6 al 10). *Nota: No generar el texto dentro de Veo.*
*   **Vertex AI Prompt (Image-to-Video - Veo 2.0):**
    > `"The covered beverage can stands on the wooden desk. Small condensation droplets slowly form on the surface of the sleeve. Soft office light reflects across the material. The camera performs a slow cinematic push-in toward the product. Premium product commercial. Photorealistic."`

---

## 📊 LEDGER DE COSTOS & FINOPS

| Elemento | Consumo | Costo Unitario (GCP Vertex) | Costo Total Estimado |
| :--- | :--- | :--- | :--- |
| **Generación Escena 1 (Img-to-Vid - Veo 2.0)** | 5 segundos | $0.18 USD / seg (Veo) | **$0.90 USD** |
| **Generación Escena 2 (Img-to-Vid - Veo 2.0)** | 5 segundos | $0.18 USD / seg (Veo) | **$0.90 USD** |
| **Post-Procesamiento (Stitching)** | Local (CPU / moviepy) | $0.00 USD (Gratuito) | **$0.00 USD** |
| **COSTO TOTAL DEL RENDER** | **10s de Comercial** | **Presupuesto Máximo** | **$1.80 USD** |
