import argparse
import os
import sys
import config
from src.selenium_runner import run_chatgpt_via_edge

def main():
    parser = argparse.ArgumentParser(description="Robot 2: Subida de Transcripción a ChatGPT")
    parser.add_argument(
        "--transcripcion",
        type=str,
        default=None,
        help="Ruta absoluta del archivo .txt a subir"
    )
    args = parser.parse_args()

    print("\n" + "="*50)
    print("       INICIANDO PROCESO: ROBOT 2 (LOG DE EJECUCIÓN)")
    print("="*50 + "\n")

    ruta_whisper = args.transcripcion
    if not ruta_whisper:
        print("[LOG] No se proporcionó argumento --transcripcion.")
        print(f"[LOG] Usando ruta por defecto definida en Config: \n      -> {config.PATH_WHISPER_DEFAULT}")
        ruta_whisper = config.PATH_WHISPER_DEFAULT
    else:
        print(f"[LOG] Argumento recibido: {ruta_whisper}")

    ruta_whisper = ruta_whisper.strip('"').strip("'")
    if not os.path.exists(ruta_whisper):
        print(f"\n[ERROR FATAL] El archivo no existe en la ruta:\n      {ruta_whisper}")
        print("Revisa que la ruta sea correcta y que el archivo .txt esté ahí.")
        sys.exit(1)

    print("[LOG] Archivo de transcripción validado: OK")

    ruta_instrucciones = config.PATH_INSTRUCCIONES
    print(f"[LOG] Buscando archivo de instrucciones en: \n      -> {ruta_instrucciones}")
    if not os.path.exists(ruta_instrucciones):
        print("\n[ERROR FATAL] No se encuentra el archivo de Reglas/Prompt.")
        sys.exit(1)

    try:
        with open(ruta_instrucciones, "r", encoding="utf-8") as f:
            prompt_texto = f.read()
        print(f"[LOG] Instrucciones cargadas ({len(prompt_texto)} caracteres). OK")
    except Exception as e:
        print(f"[ERROR] Falló la lectura del archivo de instrucciones: {e}")
        sys.exit(1)

    print("\n" + "-"*30)
    print(" INICIANDO NAVEGADOR (EDGE)")
    print("-"*30)

    resultado = run_chatgpt_via_edge(
        prompt_text=prompt_texto,
        file_paths=[ruta_whisper],
        wait_seconds=60
    )

    print("\n" + "="*50)
    if resultado.ok:
        print(" [ÉXITO] El proceso finalizó correctamente.")
        print("         1. Archivo subido.")
        print("         2. Prompt pegado y enviado.")
        print("         3. Revisa la ventana del navegador.")
    else:
        print(f" [FALLO] Ocurrió un error: {resultado.message}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
