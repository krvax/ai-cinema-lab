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
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None

try:
    from google.cloud import storage
except ImportError:
    storage = None

try:
    import imageio_ffmpeg
except ImportError:
    imageio_ffmpeg = None

try:
    from moviepy import VideoFileClip, concatenate_videoclips
except ImportError:
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
    
    # Obtener el ejecutable de ffmpeg (priorizando el embebido en imageio_ffmpeg)
    ffmpeg_exe = "ffmpeg"
    if imageio_ffmpeg is not None:
        try:
            ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        except Exception:
            pass
            
    # Intentamos crear un video real en negro con duración de 4s
    cmd = f'"{ffmpeg_exe}" -y -f lavfi -i color=c=black:s=640x360 -t {scene["duration_seconds"]} -pix_fmt yuv420p "{output_path}" >/dev/null 2>&1'
    status = os.system(cmd)
    
    # Si falló o el archivo no existe/está vacío, usamos un fallback de bytes
    if status != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
        with open(output_path, "wb") as f:
            f.write(b"MOCK VIDEO DATA" * 1000)
            
    print(f"   Saved to: {output_path}")
    return output_path

def ensure_gcs_bucket_exists(project_id, bucket_name, region="us-central1"):
    """
    Verifica si un bucket de GCS existe. Si no, lo crea.
    """
    if storage is None:
        print("❌ Error: SDK de Google Cloud Storage no instalado.")
        sys.exit(1)
        
    storage_client = storage.Client(project=project_id)
    
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except Exception:
        print(f"   [GCS] El bucket '{bucket_name}' no existe. Intentando crearlo...")
        try:
            bucket = storage_client.create_bucket(bucket_name, location=region)
            print(f"   [GCS] Bucket '{bucket_name}' creado con éxito.")
        except Exception as e:
            print(f"   [GCS] Error al crear el bucket: {e}")
            print(f"   Por favor, crea un bucket manualmente e indica su nombre en config.json como 'gcs_bucket_name'.")
            sys.exit(1)
    return bucket

def upload_to_gcs(local_path, project_id, bucket_name, region="us-central1"):
    """
    Sube un archivo local a un bucket de Google Cloud Storage y retorna la URI gs://.
    """
    print(f"   [GCS] Subiendo {local_path} al bucket '{bucket_name}'...")
    bucket = ensure_gcs_bucket_exists(project_id, bucket_name, region)
    
    blob_name = os.path.basename(local_path)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_path)
    
    gcs_uri = f"gs://{bucket_name}/{blob_name}"
    print(f"   [GCS] Archivo subido con éxito: {gcs_uri}")
    return gcs_uri

def render_scene_via_vertex(scene, config, output_dir):
    """
    Realiza la llamada real de API a Vertex AI usando el SDK google-genai para Veo/Imagen.
    """
    output_path = os.path.join(output_dir, scene["output_name"])
    print(f"\n🚀 [GCP VERTEX AI] Iniciando renderizado real para {scene['output_name']}...")
    
    if genai is None or types is None:
        print("❌ Error: SDK 'google-genai' no instalado. Ejecuta: pip install -r requirements.txt")
        sys.exit(1)
        
    project_id = config["gcp_project_id"]
    region = config["gcp_region"]
    bucket_name = config.get("gcs_bucket_name", f"{project_id}-seeds")
    
    # Asegurarnos de que el bucket de GCS exista (necesario para guardar los outputs de Vertex AI)
    ensure_gcs_bucket_exists(project_id, bucket_name, region)
    
    # Inicializar el cliente unificado de GenAI para Vertex AI
    client = genai.Client(vertexai=True, project=project_id, location=region)
    
    # Determinar el ID del modelo a usar
    default_model = "veo-2.0-generate-001"
    model_name = scene.get("model", scene.get("veo_model_id", config.get("veo_model_id", default_model)))
    print(f"\n[MODEL RESOLUTION] Using model: {model_name} for scene {scene['id']}")
    
    # Configurar parámetros de llamada de video
    # Indicamos el output_gcs_uri para que Vertex AI guarde el video en nuestro bucket y podamos verlo en el navegador
    output_gcs_dir = f"gs://{bucket_name}/output/"
    video_config = types.GenerateVideosConfig(
        number_of_videos=1,
        aspect_ratio="16:9",
        duration_seconds=scene["duration_seconds"],
        output_gcs_uri=output_gcs_dir,
    )
    
    image_ref = None
    if scene["type"] == "image-to-video":
        local_image = scene["seed_image"]
        if not os.path.exists(local_image):
            print(f"❌ Error: No se encontró la imagen semilla local en: {local_image}")
            sys.exit(1)
            
        # Subir a GCS para que Vertex AI pueda acceder
        gcs_uri = upload_to_gcs(local_image, project_id, bucket_name, region)
        
        # Asignar la referencia de imagen
        image_ref = types.Image(
            gcs_uri=gcs_uri,
            mime_type="image/png"
        )
        
    print(f"   Enviando solicitud a Veo ({model_name})...")
    print(f"   Prompt: \"{scene['prompt'][:100]}...\"")
    
    try:
        if image_ref:
            operation = client.models.generate_videos(
                model=model_name,
                prompt=scene["prompt"],
                image=image_ref,
                config=video_config
            )
        else:
            operation = client.models.generate_videos(
                model=model_name,
                prompt=scene["prompt"],
                config=video_config
            )
            
        print("   Operación iniciada en Vertex AI. Esperando renderizado (esto toma un par de minutos)...")
        
        # Esperar la respuesta mediante polling
        import time
        while not operation.done:
            print("   Esperando renderizado en Vertex AI (revisando en 15 segundos)...")
            time.sleep(15)
            operation = client.operations.get(operation)
            
        if operation.error:
            if isinstance(operation.error, dict):
                error_msg = operation.error.get('message', 'Sin mensaje')
                error_code = operation.error.get('code', 'Sin código')
            else:
                error_msg = getattr(operation.error, 'message', 'Sin mensaje')
                error_code = getattr(operation.error, 'code', 'Sin código')
            raise Exception(f"La operación falló en Vertex AI con el error: {error_msg} (Código: {error_code})")

        if operation.response and operation.response.generated_videos:
            generated_video = operation.response.generated_videos[0]
            video_obj = generated_video.video
            print(f"   ¡Video renderizado con éxito por Vertex AI!")
            
            if video_obj.video_bytes:
                print(f"   Guardando video desde los bytes de la respuesta...")
                with open(output_path, "wb") as f:
                    f.write(video_obj.video_bytes)
                print(f"   Guardado localmente en: {output_path}")
                return output_path
            elif video_obj.uri:
                print(f"   El video está almacenado en: {video_obj.uri}")
                if video_obj.uri.startswith("gs://"):
                    print(f"   Descargando video desde GCS...")
                    try:
                        gcs_path = video_obj.uri[5:]
                        parts = gcs_path.split("/", 1)
                        res_bucket = parts[0]
                        res_blob = parts[1]
                        
                        storage_client = storage.Client(project=project_id)
                        bucket = storage_client.bucket(res_bucket)
                        blob = bucket.blob(res_blob)
                        blob.download_to_filename(output_path)
                        print(f"   Guardado localmente en: {output_path}")
                        return output_path
                    except Exception as gcs_err:
                        raise Exception(f"Error al descargar desde GCS ({video_obj.uri}): {gcs_err}")
                else:
                    try:
                        import urllib.request
                        print(f"   Descargando video vía HTTP...")
                        urllib.request.urlretrieve(video_obj.uri, output_path)
                        print(f"   Guardado localmente en: {output_path}")
                        return output_path
                    except Exception as http_err:
                        raise Exception(f"Error al descargar desde URL HTTP ({video_obj.uri}): {http_err}")
            else:
                raise Exception("La respuesta de Vertex AI no contiene ni bytes de video ni una URI para descargar.")
        else:
            raise Exception("La operación de Vertex AI completó, pero no devolvió ningún video y no tiene un error especificado.")
        
    except Exception as e:
        print(f"❌ Error en la llamada a Vertex AI: {e}")
        print("   Asegúrate de estar autenticado ('gcloud auth application-default login')")
        print("   y de tener acceso al modelo en tu proyecto.")
        sys.exit(1)

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
    print("\n==================================================")
    print("⚙️  LOADED CONFIGURATION:")
    print(json.dumps(config, indent=2))
    print("==================================================")
    
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
