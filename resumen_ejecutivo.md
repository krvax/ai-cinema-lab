# RESUMEN EJECUTIVO

## AI Cinema Lab: Generación Automatizada de Video con IA, Cloud y FinOps

**Fecha:** 5 de junio de 2026

### Resumen

Durante esta iniciativa se desarrolló un pipeline reproducible de generación de video utilizando Inteligencia Artificial sobre Google Cloud Platform. El objetivo fue validar la viabilidad técnica, operativa y financiera de producir contenido audiovisual mediante modelos generativos, integrando controles de costos, automatización y gobierno de plataforma.

El proyecto permitió generar comerciales cortos mediante imágenes semilla, prompts declarativos y renderizado automatizado utilizando Vertex AI Veo, reduciendo significativamente el tiempo y costo requerido para experimentar con conceptos creativos.

---

## ¿Qué construimos?

Se desarrolló una plataforma automatizada compuesta por:

* Vertex AI (Veo) para generación de video.
* Google Cloud Storage para almacenamiento de assets y resultados.
* Un orquestador en Python para ejecutar el flujo completo.
* Controles FinOps para validación de presupuestos.
* Registro de costos y auditoría local.
* Ensamble automático de clips mediante MoviePy.

El pipeline permite ejecutar todo el proceso mediante configuración declarativa y un único comando de ejecución.

---

## Resultados obtenidos

Se generaron múltiples iteraciones de un comercial experimental denominado:

**"Hide in Plain Sight"**

El proyecto cumplió exitosamente con los objetivos técnicos:

* Integración funcional con Vertex AI.
* Generación de video Image-to-Video.
* Gestión automática de assets en GCS.
* Descarga y ensamblado automatizado de resultados.
* Control presupuestal en tiempo real.
* Registro auditable de costos.

Desde la perspectiva creativa, el ejercicio permitió comprender las fortalezas y limitaciones actuales de los modelos generativos de video para publicidad de producto.

---

## Aprendizajes clave

### 1. Las imágenes semilla son determinantes

El principal hallazgo fue que la calidad de los resultados depende en gran medida de las imágenes de entrada.

Las mejores animaciones se obtienen cuando:

* Existe contexto visual real.
* Hay iluminación consistente.
* Se conserva continuidad entre escenas.
* Los objetos están claramente definidos.

### 2. La IA anima mejor que transforma

Los modelos actuales muestran mejores resultados cuando animan una escena existente que cuando intentan convertir un objeto en algo completamente diferente.

Por esta razón, los futuros proyectos deberán apoyarse en secuencias fotográficas cuidadosamente preparadas para maximizar consistencia visual.

### 3. Iterar es económico

La generación de múltiples versiones creativas resulta financieramente viable gracias al bajo costo por render.

Esto abre oportunidades para pruebas A/B, experimentación de marketing y validación temprana de conceptos.

---

## Costos

### Costo unitario aproximado

| Servicio           | Costo               |
| ------------------ | ------------------- |
| Veo Text-to-Video  | USD $0.15 / segundo |
| Veo Image-to-Video | USD $0.18 / segundo |

### Corrida del comercial

| Concepto              | Costo         |
| --------------------- | ------------- |
| Escena 1 (5 segundos) | USD $0.90     |
| Escena 2 (5 segundos) | USD $0.90     |
| Almacenamiento GCS    | USD $0.00     |
| Stitching local       | USD $0.00     |
| **Total**             | **USD $1.80** |

### Consumo acumulado del proyecto

Presupuesto mensual autorizado: **USD $15.00**

Consumo acumulado: **USD $12.72**

Estado: **Dentro de presupuesto.**

---

## Valor estratégico

Más allá del comercial generado, el activo principal es la plataforma creada.

La solución demuestra la posibilidad de combinar:

* Inteligencia Artificial Generativa
* Cloud Computing
* Automatización
* Observabilidad
* FinOps
* Platform Engineering

en un único flujo reproducible.

Este enfoque puede reutilizarse para futuros casos de uso relacionados con marketing, capacitación, contenido digital, prototipado visual y generación automatizada de materiales audiovisuales.

---

## Próximos pasos recomendados

1. Crear un banco de imágenes semilla de calidad profesional.
2. Incorporar branding, música y postproducción automatizada.
3. Generar variantes creativas para pruebas comparativas.
4. Evaluar otros modelos de video conforme evolucionen las capacidades del mercado.
5. Convertir AI Cinema Lab en una plataforma reusable para experimentación audiovisual basada en IA.

---

## Conclusión

El proyecto validó exitosamente la viabilidad técnica y financiera de generar contenido audiovisual mediante IA en Google Cloud.

Aunque el primer comercial sirvió principalmente como aprendizaje creativo, el resultado más importante fue la construcción de una plataforma funcional, reproducible y gobernada por controles FinOps que permite iterar rápidamente sobre nuevas ideas a muy bajo costo.
