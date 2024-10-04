# TranscribeYT.io

Este programa permite descargar y transcribir audio y video de YouTube. También puedes transcribir archivos de audio almacenados localmente. Utiliza `yt-dlp` para descargar el contenido de YouTube y el modelo `Whisper` de OpenAI para realizar la transcripción.

## Características

- Descargar videos de YouTube en calidad 720p o 1080p.
- Descargar solo el audio en formato MP3.
- Transcribir el audio de un video de YouTube directamente.
- Transcribir archivos de audio locales.
- Limpieza opcional del archivo de audio descargado después de la transcripción.

## Requisitos

1. Python 3.6 o superior.
2. Instalar las siguientes bibliotecas:

```bash
pip install yt-dlp whisper openai
```

Además, asegúrate de tener instalado FFmpeg, ya que es necesario para procesar los archivos de audio y video. Puedes instalarlo con:

En sistemas basados en Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Uso

Para ejecutar el programa, simplemente corre el archivo en Python. Verás un menú con las siguientes opciones:

```bash
python transcribe_yt.py
```

## Opciones del menú
- Descargar video de YouTube: Te permite ingresar una URL de YouTube y seleccionar una calidad de video (720p o 1080p) para descargar el video.

- Descargar audio de YouTube: Te permite descargar el audio de un video de YouTube como un archivo MP3.

- Transcribir video de YouTube: Esta opción descarga el audio de un video de YouTube, lo transcribe a texto usando el modelo Whisper, y guarda la transcripción en un archivo .txt.

- Transcribir audio almacenado localmente: Puedes ingresar la ruta de un archivo de audio local en formato MP3, y el programa lo transcribirá y guardará la transcripción en un archivo .txt.

- Salir: Finaliza el programa.

## Ejemplos
### Descargar un video de YouTube
1. Selecciona la opción "1. Descargar video de YouTube".
2. Ingresa la URL del video de YouTube.
3. Selecciona la calidad de video (720p o 1080p).
4. El video se descargará en el directorio actual.
### Descargar y transcribir un video de YouTube
1. Selecciona la opción "3. Transcribir video de YouTube".
2. Ingresa la URL del video.
3. Selecciona el idioma del video (es para español, en para inglés).
5. El programa descargará el audio, realizará la transcripción y guardará el archivo de texto con el mismo nombre del video.
6. Puede elegir si conservar el audio descargado o no.
### Transcribir un archivo de audio local
1. Selecciona la opción "4. Transcribir audio almacenado localmente".
2. Ingresa la ruta del archivo de audio local.
3. Selecciona el idioma del audio.
4. La transcripción se guardará en un archivo de texto.
