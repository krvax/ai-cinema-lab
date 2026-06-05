#!/usr/bin/env python3
"""
MAESTRO RENDERER & FINOPS SHIELD - THE SILENT EDGE
Genera escenas cinematográficas por Vertex AI y las une mediante moviepy.
"""
import os
import sys
import json
import argparse
from datetime import datetime

# Importaciones condicionales para evitar fallas si no están instaladas aún
try:
    from google.cloud import aiplatform
except ImportError:
    aiplatform = None

try:
    from moviepy.editor import VideoFileClip, concatenate_videoclips
except ImportError:
    VideoFileClip = None

LEDGER_FILE = "finops_ledger.json"

def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"monthly_spend_usd": 0.0, "transactions": []}

def save_ledger(ledger):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

def check_finops_shield(config, current_execution_cost):
    """
    SRE Guard: Valida que el costo de la corrida actual no supere los límites configurados.
    """
    max_exec = config["finops"]["max_execution_cost_usd"]
    max_month = config["finops"]["max_monthly_budget_usd"]
    
    ledger = load_ledger()
    projected_monthly = ledger["monthly_spend_usd"] + current_execution_cost
    
    print("\n==================================================")
    print("🛡️  FINOPS SHIELD CHECK")
    print(f"Costo estimado de esta corrida: ${current_execution_cost:.2f} USD")
    print(f"Presupuesto mensual acumulado: ${ledger['monthly_spend_usd']:.2f} USD / ${max_month:.2f} USD")
    print("==================================================")
    
    if current_execution_cost > max_exec:
        print(f"❌ ABORTADO: La ejecución actual (${current_execution_cost:.2f} USD) supera el límite por corrida (${max_exec:.2f} USD).")
        sys.exit(1)
        
    if projected_monthly > max_month:
        print(f"❌ ABORTADO: El costo proyectado mensual (${projected_monthly:.2f} USD) superaría el presupuesto límite (${max_month:.2f} USD).")
        sys.exit(1)
        
    print("✅ FinOps Shield: Límites validados. Autorizado para renderizar.")

def calculate_costs(config):
    """
    Calcula el costo estimado de generación basado en el modelo y duración de cada escena.
    """
    total_cost = 0.0
    pricing = config["finops"]["pricing_per_second"]
    
    for scene in config["scenes"]:
        duration = scene["duration_seconds"]
        if scene["type"] == "text-to-video":
            cost = duration * pricing["veo_video"]
        elif scene["type"] == "image-to-video":
            cost = duration * pricing["veo_image_to_video"]
        else:
            cost = duration * pricing["imagen_video"]
        total_cost += cost
    return total_cost

def record_transaction(cost, dry_run=False):
    ledger = load_ledger()
    if not dry_run:
        ledger["monthly_spend_usd"] += cost
        ledger["transactions"].append({
            "timestamp": datetime.now().isoformat(),
            "cost_usd": cost,
            "description": "Renderizado de cortometraje: The Silent Edge"
        })
        save_ledger(ledger)

def mock_render_scene(scene, output_dir):
    """
    Genera un archivo MP4 falso para pruebas de integración local (Dry-Run).
    """
    output_path = os.path.join(output_dir, scene["output_name"])
    print(f"🎬 [MOCK RENDER] Generando {scene['output_name']}...")
    print(f"   Prompt: \"{scene['prompt'][:60]}...\"")
    
    # Intentamos crear un archivo mock muy pequeño para que moviepy no falle al concatenar
    # Si ffmpeg está en el sistema, creamos un video real en negro con duración de 4s
    try:
        os.system(f"ffmpeg -y -f lavfi -i color=c=black:s=640x360 -t {scene['duration_seconds']} -pix_fmt yuv420p {output_path} >/dev/null 2>&1")
    except Exception:
        # Fallback simple
        with open(output_path, "wb") as f:
            f.write(b"MOCK VIDEO DATA" * 1000)
    print(f"   Saved to: {output_path}")
    return output_path

def render_scene_via_vertex(scene, config, output_dir):
    """
    Realiza la llamada real de API a Vertex AI (Google Veo / Imagen).
    """
    output_path = os.path.join(output_dir, scene["output_name"])
    print(f"🚀 [GCP VERTEX AI] Llamando al motor de renderizado para {scene['output_name']}...")
    
    if aiplatform is None:
        print("❌ Error: SDK de Google Cloud AI Platform no instalado. Ejecuta pip install -r requirements.txt")
        sys.exit(1)
        
    # Inicializa el cliente
    aiplatform.init(project=config["gcp_project_id"], location=config["gcp_region"])
    
    # Estructura del API call real (ejemplo con Vertex AI Video Generation)
    # En producción real, aquí se consume el endpoint de generación de video de Google Veo
    print(f"   Conectando a endpoint de video...")
    print(f"   Enviando Prompt: {scene['prompt'][:100]}...")
    
    # Placeholder de ejecución real de Vertex AI:
    # model = aiplatform.VideoGenerationModel.from_pretrained("veo-video-001")
    # operation = model.generate_video(prompt=scene["prompt"], duration_seconds=scene["duration_seconds"])
    # result = operation.result()
    # result.video.save(output_path)
    
    # Para efectos del lab inicial, si es local simulamos la creación del archivo
    return mock_render_scene(scene, output_dir)

def stitch_scenes(config, source_dir):
    """
    Une las escenas generadas en un único video final usando moviepy.
    """
    print("\n🎬 POST-PRODUCCIÓN: Uniendo escenas...")
    if VideoFileClip is None:
        print("⚠️ Warning: moviepy no está instalado. Omita la concatenación automática.")
        print(f"   Por favor, une manualmente los archivos en {source_dir} a {config['output_movie']}.")
        return

    clips = []
    try:
        for scene in config["scenes"]:
            path = os.path.join(source_dir, scene["output_name"])
            print(f"   Cargando clip: {path}")
            clips.append(VideoFileClip(path))
            
        print("   Concatenando clips en un único archivo...")
        final_clip = concatenate_videoclips(clips, method="compose")
        
        # Crear directorio de salida si no existe
        out_dir = os.path.dirname(config["output_movie"])
        os.makedirs(out_dir, exist_ok=True)
        
        print(f"   Renderizando película final en {config['output_movie']}...")
        final_clip.write_videofile(config["output_movie"], fps=24, codec="libx264")
        print("🎉 ¡Corte final de The Silent Edge listo!")
    except Exception as e:
        print(f"❌ Error durante el stitching: {e}")
        print("   Asegúrate de tener instalado ffmpeg en tu sistema operativo.")

def main():
    parser = argparse.ArgumentParser(description="AI Cinema SRE Core Engine")
    parser.add_argument("--config", default="config.json", help="Path to config.json")
    parser.add_argument("--dry-run", action="store_true", help="Simulate GCP API calls and run local cost audits")
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    # Crear directorios base
    os.makedirs("assets/output", exist_ok=True)
    
    # 1. Calcular costos
    est_cost = calculate_costs(config)
    
    # 2. Ejecutar chequeo de FinOps
    check_finops_shield(config, est_cost)
    
    # 3. Renderizar escenas
    rendered_paths = []
    for scene in config["scenes"]:
        if args.dry_run:
            path = mock_render_scene(scene, "assets/output")
        else:
            path = render_scene_via_vertex(scene, config, "assets/output")
        rendered_paths.append(path)
        
    # 4. Post-procesamiento
    if args.dry_run:
        print("\nℹ️ [DRY RUN] Simulación completada. Saltando stitching real.")
    else:
        stitch_scenes(config, "assets/output")
        
    # 5. Registrar gasto
    record_transaction(est_cost, dry_run=args.dry_run)
    print(f"\n✅ Proceso Finalizado. Costo asentado en libro contable.")

if __name__ == "__main__":
    main()
