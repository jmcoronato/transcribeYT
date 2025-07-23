# 🎬 TranscribeYT.io

> **¡Transforma cualquier video de YouTube en texto de forma automática!** 🚀

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green.svg)](https://openai.com/research/whisper)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-red.svg)](https://github.com/yt-dlp/yt-dlp)

## 🌟 ¿Qué es TranscribeYT.io?

**TranscribeYT.io** es una herramienta poderosa y fácil de usar que te permite descargar contenido de YouTube y convertir automáticamente el audio a texto utilizando la tecnología de inteligencia artificial más avanzada. ¡Perfecto para estudiantes, periodistas, creadores de contenido y cualquier persona que necesite transcripciones precisas!

### ✨ Características Principales

🎥 **Descarga de Videos HD**: Obtén videos de YouTube en calidad 720p o 1080p  
🎵 **Extracción de Audio**: Descarga solo el audio en formato MP3 de alta calidad  
📝 **Transcripción Inteligente**: Convierte audio a texto usando el modelo Whisper de OpenAI  
🌐 **Soporte Multiidioma**: Transcribe en español, inglés y muchos otros idiomas  
💾 **Archivos Locales**: Transcribe archivos de audio que ya tengas almacenados  
🧹 **Limpieza Automática**: Opción para eliminar archivos temporales después de la transcripción  
📁 **Rutas Personalizables**: Elige dónde guardar tus descargas y transcripciones

## 🚀 Instalación Rápida

### 1. Requisitos del Sistema

- **Python 3.6 o superior** 🐍
- **FFmpeg** (para procesamiento de audio/video)

### 2. Instalar Dependencias

```bash
# Instalar bibliotecas de Python
pip install yt-dlp whisper openai
```

### 3. Instalar FFmpeg

**En Windows:**

```bash
# Usando chocolatey
choco install ffmpeg

# O descarga desde: https://ffmpeg.org/download.html
```

**En Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**En macOS:**

```bash
# Usando homebrew
brew install ffmpeg
```

## 🎯 Guía de Uso

### Ejecutar el Programa

```bash
python transcribeYT.py
```

### 📋 Menú de Opciones

Cuando ejecutes el programa, verás un menú interactivo con las siguientes opciones:

```
🎬 Bienvenido a TranscribeYT.io
1. 📥 Descargar video de YouTube
2. 🎵 Descargar audio de YouTube
3. 📝 Transcribir video de YouTube
4. 🎙️ Transcribir audio almacenado localmente
0. 👋 Salir
```

## 📖 Ejemplos Detallados

### 🎥 Ejemplo 1: Descargar un Video de YouTube

```
1. Selecciona: "1. Descargar video de YouTube"
2. Ingresa la URL: https://www.youtube.com/watch?v=ejemplo
3. Elige la ruta de descarga: C:\MisVideos\ (o deja vacío para carpeta actual)
4. Selecciona calidad: 720 o 1080
5. ¡Listo! Tu video se descarga automáticamente
```

### 📝 Ejemplo 2: Transcribir un Video de YouTube

```
1. Selecciona: "3. Transcribir video de YouTube"
2. Ingresa la URL: https://www.youtube.com/watch?v=ejemplo
3. Selecciona idioma: "es" para español, "en" para inglés
4. Elige si conservar el archivo de audio: S o N
5. ¡Obtienes tu transcripción en formato .txt!
```

**Resultado:** Se crean dos archivos:

- `📁 Nombre_del_Video.mp3` (si elegiste conservarlo)
- `📄 Nombre_del_Video.txt` (transcripción completa)

### 🎙️ Ejemplo 3: Transcribir Audio Local

```
1. Selecciona: "4. Transcribir audio almacenado localmente"
2. Ingresa la ruta: C:\MiAudio\podcast.mp3
3. Selecciona idioma: "es" para español
4. ¡La transcripción se guarda como podcast.txt!
```

## 🔧 Características Técnicas

| Característica          | Detalle                                   |
| ----------------------- | ----------------------------------------- |
| **Calidad de Audio**    | MP3 a 192 kbps                            |
| **Calidades de Video**  | 720p, 1080p                               |
| **Modelo de IA**        | OpenAI Whisper (base)                     |
| **Idiomas Soportados**  | Español, Inglés, y 90+ idiomas más        |
| **Formatos de Entrada** | Cualquier formato soportado por yt-dlp    |
| **Formato de Salida**   | Texto plano (.txt) con codificación UTF-8 |

## 🌍 Idiomas Soportados

TranscribeYT.io utiliza el modelo Whisper de OpenAI, que soporta más de 90 idiomas:

- 🇪🇸 **Español** (`es`)
- 🇺🇸 **Inglés** (`en`)
- 🇫🇷 **Francés** (`fr`)
- 🇩🇪 **Alemán** (`de`)
- 🇮🇹 **Italiano** (`it`)
- 🇵🇹 **Portugués** (`pt`)
- 🇷🇺 **Ruso** (`ru`)
- 🇯🇵 **Japonés** (`ja`)
- 🇰🇷 **Coreano** (`ko`)
- 🇨🇳 **Chino** (`zh`)
- Y muchos más...
- Mas informacion en: https://openai.com/es-419/index/whisper/

## ⚡ Casos de Uso

### 👨‍🎓 Para Estudiantes

- Transcribe conferencias de YouTube para tomar notas
- Convierte tutoriales en texto para estudio offline
- Analiza contenido educativo de forma más eficiente

### 📰 Para Periodistas

- Transcribe entrevistas y declaraciones
- Convierte podcasts en artículos escritos
- Analiza discursos y conferencias de prensa

### 🎬 Para Creadores de Contenido

- Genera subtítulos para tus videos
- Crea contenido escrito a partir de tus videos
- Analiza el contenido de la competencia

### 💼 Para Profesionales

- Transcribe reuniones y webinars
- Convierte presentaciones en documentos
- Analiza contenido de capacitación

## 🛠️ Solución de Problemas

### Error: "FFmpeg no encontrado"

```bash
# Verifica la instalación
ffmpeg -version

# Si no está instalado, sigue las instrucciones de instalación arriba
```

### Error: "Módulo no encontrado"

```bash
# Reinstala las dependencias
pip install --upgrade yt-dlp whisper openai
```

### Video no disponible

- Verifica que la URL sea correcta
- Algunos videos pueden tener restricciones regionales
- Asegúrate de que el video sea público

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar TranscribeYT.io:

1. 🍴 Haz un fork del proyecto
2. 🌿 Crea una rama para tu feature
3. 💻 Implementa tus cambios
4. 📤 Envía un pull request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- **OpenAI** por el modelo Whisper
- **yt-dlp** por la biblioteca de descarga
- **FFmpeg** por el procesamiento multimedia

---

<div align="center">

**¿Te gusta TranscribeYT.io? ¡Dale una ⭐ al repositorio!**

_Hecho con ❤️ para la comunidad_

</div>
