import os
import whisper
import yt_dlp
import re

# Función para descargar el audio del video de YouTube y devolver el nombre del video sin el código
def download_audio_from_youtube(video_url):
    # Solicitar la ruta de almacenamiento al usuario
    output_path = input("Ingrese la ruta donde desea almacenar el archivo de audio (deje vacío para la carpeta actual): ").strip()
    if not output_path:
        output_path = "."  # Directorio actual
    output_path = os.path.join(output_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,  # Usar la ruta proporcionada por el usuario
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', 'audio_sin_nombre')
        audio_file = f"{video_title}.mp3"

    clean_audio_file = re.sub(r'[\\/*?:"<>|]', "", audio_file)
    full_path = os.path.join(os.path.dirname(output_path), clean_audio_file)
    
    if os.path.exists(audio_file) and audio_file != full_path:
        os.rename(audio_file, full_path)
    
    print(f"El audio ha sido descargado en '{full_path}'.")
    return full_path, video_title

# Función para transcribir el audio a texto usando Whisper
def transcribe_audio(audio_path, language='es'):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language=language)
    return result['text']

# Función básica para descargar video de YouTube con la calidad seleccionada y limpiar el nombre del archivo
def download_video_from_youtube(video_url, quality):
    output_path = input("Ingrese la ruta donde desea almacenar el archivo de video (deje vacío para la carpeta actual): ").strip()
    if not output_path:
        output_path = "."  # Directorio actual
    output_path = os.path.join(output_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': f'bestvideo[height={quality}]+bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', 'video_sin_nombre')
        video_file = f"{video_title}.mp4"

    clean_video_file = re.sub(r'[\\/*?:"<>|]', "", video_file)
    full_path = os.path.join(os.path.dirname(output_path), clean_video_file)
    
    if os.path.exists(video_file) and video_file != full_path:
        os.rename(video_file, full_path)
    
    print(f"El video '{video_title}' ha sido descargado en {quality}p en '{full_path}'.")
    return full_path, video_title

# Funcion Wrapper trancribir video de yt
def transcribe_yt_video():
        # Ruta del video de YouTube
    video_url = input("Ingresa la URL del video de YT a transcribir: ")
    lan = input("Ingresa el idioma del video (Español = es, Ingles = en): ")

    # Descargar el audio
    audio_file, title = download_audio_from_youtube(video_url)
    text_file = title + ".txt"

    # Transcribir el audio a español
    transcription = transcribe_audio(audio_file, language=lan)

    # Guardar la transcripción en un archivo de texto
    with open(text_file, "w", encoding="utf-8") as file:
        file.write(transcription)

    print(f"Tu video '{title}' fue transcribido correctamente y guardado en '{text_file}'")

    limpiar = input("Desea borrar el archivo de audio descargado? (S o N): ").strip().lower()

    # Limpiar el archivo de audio descargado (opcional)
    if(limpiar == 's'):
        if os.path.exists(audio_file):
            os.remove(audio_file)

def transcribe_local_audio():
    path = input("Ingresa la ruta del archivo a transcribir: ") 
    lan = input("Ingresa el idioma del audio (Español = es, Ingles = en): ")
    transcription = transcribe_audio(path, language=lan)
    path_txt = path.replace(".mp3", ".txt")
    with open(path_txt, "w", encoding="utf-8") as file:
        file.write(transcription)
    print(f"Tu audio fue transcribido correctamente y guardado en '{path_txt}'")   

# Funcion del menu
def mostrar_menu():
    print("Bienvenido a TranscribeYT.io")
    print("1. Descargar video de YouTube")
    print("2. Descargar audio de YouTube")
    print("3. Transcribir video de YouTube")
    print("4. Transcribir audio almacenado localmente")
    print("0. Salir")

if __name__ == "__main__":
    first = True
    while True:
        if(first):
            mostrar_menu()
            first = False
        else:
            input("Presiona enter para continuar: ")
            os.system('cls')
            mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            video_url = input("Ingresa la URL del video de YouTube: ")
            chosen_quality = input("Elige una calidad (720 o 1080): ").strip()
            download_video_from_youtube(video_url, chosen_quality)
        elif opcion == '2':
            url = input("Ingresa la URL del video de YouTube: ")
            download_audio_from_youtube(url)
        elif opcion == '3':
            transcribe_yt_video()
        elif opcion == '4':
             transcribe_local_audio()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")