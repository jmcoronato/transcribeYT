# 🎬 TranscribeYT.io

> **¡Transforma cualquier video de YouTube en texto de forma automática con una interfaz gráfica moderna!** 🚀

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green.svg)](https://openai.com/research/whisper)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-red.svg)](https://github.com/yt-dlp/yt-dlp)
[![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-GUI-purple.svg)](https://github.com/israel-dryer/ttkbootstrap)

## 📋 Índice

- [🌟 ¿Qué es TranscribeYT.io?](#-qué-es-transcribeytio)
- [✨ Características Principales](#-características-principales)
- [🚀 Instalación Rápida](#-instalación-rápida)
  - [1. Requisitos del Sistema](#1-requisitos-del-sistema)
  - [2. Instalar Dependencias](#2-instalar-dependencias)
  - [3. Instalar FFmpeg](#3-instalar-ffmpeg)
- [🎯 Guía de Uso](#-guía-de-uso)
  - [Ejecutar la Aplicación](#ejecutar-la-aplicación)
  - [🖥️ Interfaz Gráfica](#️-interfaz-gráfica)
  - [⚙️ Configuración General](#️-configuración-general)
- [📖 Ejemplos Paso a Paso](#-ejemplos-paso-a-paso)
  - [🎥 Ejemplo 1: Descargar un Video de YouTube](#-ejemplo-1-descargar-un-video-de-youtube)
  - [📝 Ejemplo 2: Transcribir un Video de YouTube](#-ejemplo-2-transcribir-un-video-de-youtube)
  - [🎙️ Ejemplo 3: Transcribir Audio Local](#️-ejemplo-3-transcribir-audio-local)
- [🔧 Características Técnicas](#-características-técnicas)
- [🌍 Idiomas Soportados](#-idiomas-soportados)
- [⚡ Casos de Uso](#-casos-de-uso)
  - [👨‍🎓 Para Estudiantes](#-para-estudiantes)
  - [📰 Para Periodistas](#-para-periodistas)
  - [🎬 Para Creadores de Contenido](#-para-creadores-de-contenido)
  - [💼 Para Profesionales](#-para-profesionales)
- [🛠️ Solución de Problemas](#️-solución-de-problemas)
- [🤝 Contribuciones](#-contribuciones)
- [📄 Licencia](#-licencia)
- [🙏 Agradecimientos](#-agradecimientos)

## 🌟 ¿Qué es TranscribeYT.io?

**TranscribeYT.io** es una aplicación con interfaz gráfica moderna y intuitiva que te permite descargar contenido de YouTube y convertir automáticamente el audio a texto utilizando la tecnología de inteligencia artificial más avanzada. Con su diseño elegante y funcional, es perfecta para estudiantes, periodistas, creadores de contenido y cualquier persona que necesite transcripciones precisas de manera sencilla.

### ✨ Características Principales

🖥️ **Interfaz Gráfica Moderna**: Aplicación con diseño intuitivo y tema oscuro elegante  
📑 **Interfaz por Pestañas**: Organiza todas las funciones en tabs fáciles de navegar  
🎥 **Descarga de Videos HD**: Obtén videos de YouTube en calidad 720p o 1080p  
🎵 **Extracción de Audio**: Descarga solo el audio en formato MP3 de alta calidad  
📝 **Transcripción Inteligente**: Convierte audio a texto usando el modelo Whisper de OpenAI  
🌐 **Soporte Multiidioma**: Transcribe en español, inglés y muchos otros idiomas con selector visual  
💾 **Archivos Locales**: Transcribe archivos de audio que ya tengas almacenados con explorador de archivos  
🎬 **Transcripción de Videos**: Procesa directamente archivos MP4 y otros formatos de video locales  
📋 **Funciones del Portapapeles**: Pega URLs directamente desde el portapapeles  
📊 **Barra de Progreso Visual**: Seguimiento en tiempo real del proceso de transcripción  
🧹 **Limpieza Automática**: Opción para eliminar archivos temporales después de la transcripción  
📁 **Rutas Personalizables**: Elige dónde guardar tus descargas y transcripciones con explorador visual

## 🚀 Instalación Rápida

### 1. Requisitos del Sistema

- **Python 3.13 o superior** 🐍
- **FFmpeg** (para procesamiento de audio/video)

### 2. Instalar Dependencias

```bash
# Instalar todas las dependencias desde el archivo requirements.txt
pip install -r requirements.txt

# O instalar bibliotecas individualmente
pip install yt-dlp openai-whisper ttkbootstrap pathlib
```

### 3. Instalar FFmpeg

**En Windows:**

```bash
# Usando chocolatey
choco install ffmpeg
```

- Descarga directa desde: https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip
- Asegurarse de agregar la ubicacion de la carpeta bin de ffmpeg al path del sistema
- Tutorial para instalacion en windows: https://www.youtube.com/watch?v=JR36oH35Fgg

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

### Ejecutar la Aplicación

```bash
python transcribeYT.py
```

### 🖥️ Interfaz Gráfica

Al ejecutar el programa, se abrirá una ventana moderna con cuatro pestañas principales:

**📝 Transcribir YouTube**

- Pega o escribe la URL del video
- Selecciona el idioma del contenido
- Haz clic en "🚀 INICIAR TRANSCRIPCIÓN"

**🎙️ Transcribir Audio Local**

- Busca y selecciona tu archivo de audio
- Elige el idioma correspondiente
- Haz clic en "🎙️ TRANSCRIBIR AUDIO"

**🎬 Transcribir Video MP4**

- Busca y selecciona tu archivo de video (MP4, AVI, MOV, etc.)
- Selecciona el idioma del video
- Haz clic en "🎬 TRANSCRIBIR VIDEO"

**📥 Descargar Contenido**

- Ingresa la URL del video o usa "📋 Pegar desde portapapeles"
- Selecciona la calidad (720p/1080p)
- Elige entre "🎥 DESCARGAR VIDEO" o "🎵 DESCARGAR AUDIO"

### ⚙️ Configuración General

- **Carpeta de destino**: Personaliza dónde se guardan los archivos
- **Barra de progreso**: Seguimiento visual del proceso en tiempo real
- **Indicador de estado**: Información detallada de cada paso del proceso

## 📖 Ejemplos Paso a Paso

### 🎥 Ejemplo 1: Descargar un Video de YouTube

1. **Abrir la pestaña "📥 Descargar Contenido"**
2. **Pegar URL**: Copia la URL del video y pégala en el campo correspondiente
   - Puedes usar el botón "📋 Pegar desde portapapeles"
3. **Configurar calidad**: Selecciona "720p" o "1080p" desde el menú desplegable
4. **Elegir carpeta**: Si quieres cambiar la ubicación, usa "📁 CAMBIAR RUTA"
5. **Descargar**: Haz clic en "🎥 DESCARGAR VIDEO"
6. **Seguimiento**: Observa la barra de progreso y los mensajes de estado

### 📝 Ejemplo 2: Transcribir un Video de YouTube

1. **Abrir la pestaña "📝 Transcribir YouTube"**
2. **Ingresar URL**: Pega la URL del video de YouTube
3. **Seleccionar idioma**: Elige el idioma desde el menú visual (🇪🇸 Español, 🇺🇸 Inglés, etc.)
4. **Iniciar proceso**: Haz clic en "🚀 INICIAR TRANSCRIPCIÓN"
5. **Seguimiento automático**: La aplicación:
   - Descarga el audio automáticamente
   - Procesa con IA Whisper
   - Guarda la transcripción como archivo .txt
6. **Limpieza opcional**: Al final, puedes elegir eliminar el archivo de audio temporal

**Resultado:** Se crean archivos:

- `📄 Nombre_del_Video.txt` (transcripción completa)
- `🎵 Nombre_del_Video.mp3` (opcional, si decides conservarlo)

### 🎙️ Ejemplo 3: Transcribir Audio Local

1. **Abrir la pestaña "🎙️ Transcribir Audio Local"**
2. **Seleccionar archivo**: Haz clic en "📁 BUSCAR ARCHIVO" y navega hasta tu audio
3. **Configurar idioma**: Selecciona el idioma correspondiente
4. **Procesar**: Haz clic en "🎙️ TRANSCRIBIR AUDIO"
5. **Resultado automático**: Se crea `mi_audio.txt` en la misma carpeta del archivo original

### 🎬 Ejemplo 4: Transcribir Video MP4

1. **Abrir la pestaña "🎬 Transcribir Video MP4"**
2. **Seleccionar archivo**: Haz clic en "📁 BUSCAR VIDEO" y navega hasta tu video
   - Soporta formatos: MP4, AVI, MOV, MKV, WMV, FLV
3. **Configurar idioma**: Selecciona el idioma del video desde el menú visual
4. **Procesar**: Haz clic en "🎬 TRANSCRIBIR VIDEO"
5. **Seguimiento automático**: La aplicación:
   - Extrae el audio del video automáticamente
   - Procesa con IA Whisper
   - Guarda la transcripción como archivo .txt
6. **Resultado automático**: Se crea `mi_video.txt` en la misma carpeta del archivo original

**Resultado:** Se crea archivo:

- `📄 mi_video.txt` (transcripción completa del audio del video)

## 🔧 Características Técnicas

| Característica          | Detalle                                                         |
| ----------------------- | --------------------------------------------------------------- |
| **Interfaz**            | GUI moderna con ttkbootstrap                                    |
| **Tema Visual**         | Superhero (tema oscuro elegante)                                |
| **Calidad de Audio**    | MP3 a 192 kbps                                                  |
| **Calidades de Video**  | 720p, 1080p                                                     |
| **Modelo de IA**        | OpenAI Whisper (base)                                           |
| **Idiomas Soportados**  | Español, Inglés, y 90+ idiomas más                              |
| **Formatos de Entrada** | YouTube URLs, MP3/WAV/M4A/AAC/OGG/FLAC, MP4/AVI/MOV/MKV/WMV/FLV |
| **Formato de Salida**   | Texto plano (.txt) con codificación UTF-8                       |
| **Procesamiento**       | Multihilo para operaciones no bloqueantes                       |
| **Compatibilidad**      | Windows, macOS, Linux                                           |

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
- Transcribe videos locales para crear blogs y artículos

### 💼 Para Profesionales

- Transcribe reuniones y webinars
- Convierte presentaciones en documentos
- Analiza contenido de capacitación
- Procesa archivos de video de conferencias y seminarios

## 🛠️ Solución de Problemas

### Error: "FFmpeg no encontrado"

```bash
# Verifica la instalación
ffmpeg -version
```

- Si no está instalado, sigue las instrucciones de instalación de arriba
- [3. Instalar FFmpeg](#3-instalar-ffmpeg)

### Error: "Módulo no encontrado"

```bash
# Reinstala las dependencias
pip install --upgrade -r requirements.txt

# O instala módulos específicos
pip install --upgrade yt-dlp openai-whisper ttkbootstrap
```

### Video no disponible

- Verifica que la URL sea correcta
- Algunos videos pueden tener restricciones regionales
- Asegúrate de que el video sea público

### Error al procesar video local

- Verifica que el archivo no esté corrupto
- Asegúrate de que el formato sea compatible (MP4, AVI, MOV, MKV, WMV, FLV)
- El archivo debe tener pista de audio para poder transcribir

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
- **ttkbootstrap** por la interfaz gráfica moderna

---

<div align="center">

**¿Te gusta TranscribeYT.io? ¡Dale una ⭐ al repositorio!**

_Hecho con ❤️ para la comunidad_

</div>
