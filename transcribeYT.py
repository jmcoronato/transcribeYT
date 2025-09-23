import os
import whisper
import yt_dlp
import re
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from pathlib import Path
import ttkbootstrap as ttk_bs
from ttkbootstrap.constants import *
from datetime import datetime

class TranscribeYTGUI:
    def __init__(self):
        # Crear ventana principal con tema moderno
        self.root = ttk_bs.Window(themename="superhero")
        self.root.title("🎬 TranscribeYT.io")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        self.root.minsize(900, 750)
        
        # Configurar estilo personalizado
        self.setup_custom_styles()
        
        # Variables
        self.video_url = tk.StringVar()
        self.language = tk.StringVar(value="es")
        self.quality = tk.StringVar(value="720")
        self.output_path = tk.StringVar(value=os.getcwd())
        self.audio_file_path = tk.StringVar()
        self.video_file_path = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Listo para comenzar")
        
        self.setup_ui()
        
    def setup_custom_styles(self):
        """Configurar estilos personalizados para una interfaz más moderna"""
        style = ttk_bs.Style()
        
        # Configurar estilos para botones especiales
        style.configure(
            "Modern.TButton",
            font=("Arial", 10, "bold"),
            borderwidth=2,
            relief="raised",
            padding=8
        )
        
        # Estilo para botones de acción principal
        style.configure(
            "Action.TButton", 
            font=("Arial", 12, "bold"),
            padding=12
        )
        
        # Estilo para frames con gradiente visual
        style.configure(
            "Card.TLabelframe",
            borderwidth=2,
            relief="solid"
        )
        
        # Estilo personalizado para la barra de progreso
        style.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='#2b2b2b',
            borderwidth=1,
            lightcolor='#4a90e2',
            darkcolor='#357abd'
        )
        
    def setup_ui(self):
        # Configurar el grid del root para mejor control
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Frame principal con scrollbar para contenido que no cabe
        main_canvas = tk.Canvas(self.root)
        scrollbar = ttk_bs.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk_bs.Frame(main_canvas)
        
        # Función para centrar el contenido en el canvas
        def configure_scroll_region(event=None):
            main_canvas.configure(scrollregion=main_canvas.bbox("all"))
            # Centrar el contenido horizontalmente
            canvas_width = main_canvas.winfo_width()
            frame_width = scrollable_frame.winfo_reqwidth()
            if canvas_width > frame_width:
                x_offset = (canvas_width - frame_width) // 2
                main_canvas.create_window((x_offset, 0), window=scrollable_frame, anchor="nw")
            else:
                main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        scrollable_frame.bind("<Configure>", configure_scroll_region)
        main_canvas.bind("<Configure>", configure_scroll_region)
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame principal centrado usando grid
        main_frame = ttk_bs.Frame(scrollable_frame, padding=20)
        main_frame.pack(fill=BOTH, expand=True)
        
        # Configurar grid para centrado
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        
        # Frame interno centrado con grid
        inner_container = ttk_bs.Frame(main_frame)
        inner_container.grid(row=0, column=1, sticky="", pady=20)
        
        # Título con estilo mejorado y centrado
        title_label = ttk_bs.Label(
            inner_container, 
            text="🎬 TranscribeYT.io", 
            font=("Arial", 24, "bold"),
            bootstyle="warning"
        )
        title_label.pack(pady=(0, 8))
        
        # Subtitle con estilo mejorado y centrado
        subtitle_label = ttk_bs.Label(
            inner_container, 
            text="✨ Transforma videos de YouTube en texto automáticamente ✨",
            font=("Arial", 11, "italic"),
            bootstyle="info"
        )
        subtitle_label.pack(pady=(0, 15))
        
        # Notebook para las diferentes funcionalidades con ancho fijo
        notebook = ttk_bs.Notebook(inner_container, bootstyle="warning", width=700)
        notebook.pack(pady=(0, 15))
        
        # Tab 1: Transcribir video de YouTube
        self.create_transcribe_yt_tab(notebook)
        
        # Tab 2: Transcribir audio local
        self.create_transcribe_local_tab(notebook)
        
        # Tab 3: Transcribir video local (MP4)
        self.create_transcribe_video_tab(notebook)
        
        # Tab 4: Descargar contenido
        self.create_download_tab(notebook)
        
        # Frame para configuración y progreso con ancho fijo
        bottom_container = ttk_bs.Frame(inner_container)
        bottom_container.pack(fill=X, pady=(10, 0), expand=False)
        
        # Configuración general
        self.create_settings_frame(bottom_container)
        
        # Barra de progreso y estado
        self.create_progress_frame(bottom_container)
        
        # Footer con marca registrada
        self.create_footer_frame(inner_container)
        
        # Configurar canvas y scrollbar
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
    def create_transcribe_yt_tab(self, notebook):
        frame = ttk_bs.Frame(notebook, padding=20)
        notebook.add(frame, text="📝 Transcribir YouTube")
        
        # URL del video con estilo mejorado
        url_frame = ttk_bs.LabelFrame(frame, text="🔗 URL del Video", padding=18, bootstyle="primary")
        url_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(url_frame, text="Ingresa la URL del video de YouTube:").pack(anchor=W, pady=(0, 5))
        url_entry = ttk_bs.Entry(url_frame, textvariable=self.video_url, font=("Arial", 11))
        url_entry.pack(fill=X, pady=(0, 10))
        
        # Botón para pegar desde portapapeles con estilo mejorado
        paste_btn = ttk_bs.Button(
            url_frame, 
            text="📋 Pegar desde portapapeles", 
            command=self.paste_from_clipboard,
            bootstyle="warning",
            width=25
        )
        paste_btn.pack(anchor=W, pady=(5, 0))
        
        # Configuración de idioma con estilo mejorado
        lang_frame = ttk_bs.LabelFrame(frame, text="🌐 Configuración de Idioma", padding=18, bootstyle="success")
        lang_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(lang_frame, text="Selecciona el idioma del video:").pack(anchor=W, pady=(0, 5))
        
        lang_options = [
            ("🇪🇸 Español", "es"),
            ("🇺🇸 Inglés", "en"),
            ("🇫🇷 Francés", "fr"),
            ("🇩🇪 Alemán", "de"),
            ("🇮🇹 Italiano", "it"),
            ("🇵🇹 Portugués", "pt"),
            ("🇯🇵 Japonés", "ja"),
            ("🇰🇷 Coreano", "ko"),
            ("🇨🇳 Chino", "zh"),
            ("🇷🇺 Ruso", "ru")
        ]
        
        lang_combo = ttk_bs.Combobox(
            lang_frame, 
            textvariable=self.language,
            values=[f"{name}" for name, code in lang_options],
            state="readonly",
            font=("Arial", 11)
        )
        lang_combo.pack(fill=X)
        lang_combo.set("🇪🇸 Español")
        
        # Container para centrar el botón
        button_container = ttk_bs.Frame(frame)
        button_container.pack(pady=25, fill=X)
        
        # Botón principal con estilo mejorado y centrado
        transcribe_btn = ttk_bs.Button(
            button_container,
            text="🚀 INICIAR TRANSCRIPCIÓN",
            command=self.start_transcribe_youtube,
            bootstyle="success-outline",
            width=35
        )
        transcribe_btn.pack(anchor="center")
        
    def create_transcribe_local_tab(self, notebook):
        frame = ttk_bs.Frame(notebook, padding=20)
        notebook.add(frame, text="🎙️ Transcribir Audio Local")
        
        # Selección de archivo con estilo mejorado
        file_frame = ttk_bs.LabelFrame(frame, text="🎵 Archivo de Audio", padding=18, bootstyle="primary")
        file_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(file_frame, text="Selecciona el archivo de audio:").pack(anchor=W, pady=(0, 5))
        
        file_select_frame = ttk_bs.Frame(file_frame)
        file_select_frame.pack(fill=X, pady=(0, 10))
        
        file_entry = ttk_bs.Entry(file_select_frame, textvariable=self.audio_file_path, font=("Arial", 11))
        file_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        
        browse_btn = ttk_bs.Button(
            file_select_frame,
            text="📁 BUSCAR ARCHIVO",
            command=self.browse_audio_file,
            bootstyle="primary",
            width=20
        )
        browse_btn.pack(side=RIGHT)
        
        # Configuración de idioma para audio local con estilo mejorado
        lang_frame = ttk_bs.LabelFrame(frame, text="🌐 Configuración de Idioma", padding=18, bootstyle="success")
        lang_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(lang_frame, text="Selecciona el idioma del audio:").pack(anchor=W, pady=(0, 5))
        
        lang_combo_local = ttk_bs.Combobox(
            lang_frame, 
            textvariable=self.language,
            values=["🇪🇸 Español", "🇺🇸 Inglés", "🇫🇷 Francés", "🇩🇪 Alemán", "🇮🇹 Italiano", 
                   "🇵🇹 Portugués", "🇯🇵 Japonés", "🇰🇷 Coreano", "🇨🇳 Chino", "🇷🇺 Ruso"],
            state="readonly",
            font=("Arial", 11)
        )
        lang_combo_local.pack(fill=X)
        lang_combo_local.set("🇪🇸 Español")
        
        # Container para centrar el botón
        button_container = ttk_bs.Frame(frame)
        button_container.pack(pady=25, fill=X)
        
        # Botón principal con estilo mejorado y centrado
        transcribe_local_btn = ttk_bs.Button(
            button_container,
            text="🎙️ TRANSCRIBIR AUDIO",
            command=self.start_transcribe_local,
            bootstyle="info-outline",
            width=35
        )
        transcribe_local_btn.pack(anchor="center")
        
    def create_transcribe_video_tab(self, notebook):
        frame = ttk_bs.Frame(notebook, padding=20)
        notebook.add(frame, text="🎬 Transcribir Video MP4")
        
        # Selección de archivo con estilo mejorado
        file_frame = ttk_bs.LabelFrame(frame, text="🎥 Archivo de Video", padding=18, bootstyle="primary")
        file_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(file_frame, text="Selecciona el archivo de video MP4:").pack(anchor=W, pady=(0, 5))
        
        file_select_frame = ttk_bs.Frame(file_frame)
        file_select_frame.pack(fill=X, pady=(0, 10))
        
        file_entry = ttk_bs.Entry(file_select_frame, textvariable=self.video_file_path, font=("Arial", 11))
        file_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        
        browse_btn = ttk_bs.Button(
            file_select_frame,
            text="📁 BUSCAR VIDEO",
            command=self.browse_video_file,
            bootstyle="primary",
            width=20
        )
        browse_btn.pack(side=RIGHT)
        
        # Configuración de idioma para video local con estilo mejorado
        lang_frame = ttk_bs.LabelFrame(frame, text="🌐 Configuración de Idioma", padding=18, bootstyle="success")
        lang_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(lang_frame, text="Selecciona el idioma del video:").pack(anchor=W, pady=(0, 5))
        
        lang_combo_video = ttk_bs.Combobox(
            lang_frame, 
            textvariable=self.language,
            values=["🇪🇸 Español", "🇺🇸 Inglés", "🇫🇷 Francés", "🇩🇪 Alemán", "🇮🇹 Italiano", 
                   "🇵🇹 Portugués", "🇯🇵 Japonés", "🇰🇷 Coreano", "🇨🇳 Chino", "🇷🇺 Ruso"],
            state="readonly",
            font=("Arial", 11)
        )
        lang_combo_video.pack(fill=X)
        lang_combo_video.set("🇪🇸 Español")
        
        # Container para centrar el botón
        button_container = ttk_bs.Frame(frame)
        button_container.pack(pady=25, fill=X)
        
        # Botón principal con estilo mejorado y centrado
        transcribe_video_btn = ttk_bs.Button(
            button_container,
            text="🎬 TRANSCRIBIR VIDEO",
            command=self.start_transcribe_video,
            bootstyle="danger-outline",
            width=35
        )
        transcribe_video_btn.pack(anchor="center")
        
    def create_download_tab(self, notebook):
        frame = ttk_bs.Frame(notebook, padding=20)
        notebook.add(frame, text="📥 Descargar Contenido")
        
        # URL del video con estilo mejorado
        url_frame = ttk_bs.LabelFrame(frame, text="🔗 URL del Video", padding=18, bootstyle="primary")
        url_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(url_frame, text="Ingresa la URL del video de YouTube:").pack(anchor=W, pady=(0, 5))
        url_entry_download = ttk_bs.Entry(url_frame, textvariable=self.video_url, font=("Arial", 11))
        url_entry_download.pack(fill=X, pady=(0, 10))
        
        # Botón para pegar desde portapapeles con estilo mejorado
        paste_btn_download = ttk_bs.Button(
            url_frame, 
            text="📋 Pegar desde portapapeles", 
            command=self.paste_from_clipboard,
            bootstyle="warning",
            width=25
        )
        paste_btn_download.pack(anchor=W, pady=(5, 0))
        
        # Configuración de calidad con estilo mejorado
        quality_frame = ttk_bs.LabelFrame(frame, text="⚙️ Configuración de Descarga", padding=18, bootstyle="warning")
        quality_frame.pack(fill=X, pady=(0, 20))
        
        ttk_bs.Label(quality_frame, text="Selecciona la calidad del video:").pack(anchor=W, pady=(0, 5))
        
        quality_combo = ttk_bs.Combobox(
            quality_frame,
            textvariable=self.quality,
            values=["720p", "1080p"],
            state="readonly",
            font=("Arial", 11)
        )
        quality_combo.pack(fill=X, pady=(0, 15))
        quality_combo.set("720p")
        
        # Container para centrar los botones de descarga
        buttons_container = ttk_bs.Frame(frame)
        buttons_container.pack(fill=X, pady=20)
        
        # Frame interno para los botones centrados
        buttons_frame = ttk_bs.Frame(buttons_container)
        buttons_frame.pack(anchor="center")
        
        download_video_btn = ttk_bs.Button(
            buttons_frame,
            text="🎥 DESCARGAR VIDEO",
            command=self.start_download_video,
            bootstyle="danger-outline",
            width=25
        )
        download_video_btn.pack(side=LEFT, padx=(0, 15))
        
        download_audio_btn = ttk_bs.Button(
            buttons_frame,
            text="🎵 DESCARGAR AUDIO",
            command=self.start_download_audio,
            bootstyle="warning-outline",
            width=25
        )
        download_audio_btn.pack(side=LEFT)
        
    def create_settings_frame(self, parent):
        settings_frame = ttk_bs.LabelFrame(parent, text="⚙️ Configuración General", padding=15, bootstyle="info")
        settings_frame.pack(fill=X, pady=(0, 10))
        
        # Contenedor principal
        main_container = ttk_bs.Frame(settings_frame)
        main_container.pack(fill=X, expand=True)
        
        # Ruta de salida con mejor espaciado
        ttk_bs.Label(main_container, text="Carpeta de destino:", font=("Arial", 10, "bold")).pack(anchor=W, pady=(0, 5))
        
        path_frame = ttk_bs.Frame(main_container)
        path_frame.pack(fill=X, pady=(0, 5))
        
        path_entry = ttk_bs.Entry(
            path_frame, 
            textvariable=self.output_path, 
            font=("Arial", 10),
            state="readonly"
        )
        path_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 8))
        
        browse_path_btn = ttk_bs.Button(
            path_frame,
            text="📁 Cambiar",
            command=self.browse_output_path,
            bootstyle="secondary",
            width=15
        )
        browse_path_btn.pack(side=RIGHT)
        
    def create_progress_frame(self, parent):
        progress_frame = ttk_bs.LabelFrame(parent, text="📊 Progreso", padding=15, bootstyle="success")
        progress_frame.pack(fill=X, pady=(10, 10))
        
        # Contenedor para el progreso
        progress_container = ttk_bs.Frame(progress_frame)
        progress_container.pack(fill=X, expand=True)
        
        # Etiqueta de estado con mejor formato
        status_label = ttk_bs.Label(
            progress_container, 
            textvariable=self.status_var, 
            font=("Arial", 10, "bold"),
            bootstyle="info"
        )
        status_label.pack(anchor=W, pady=(0, 8))
        
        # Barra de progreso con tamaño adaptativo
        self.progress_bar = ttk_bs.Progressbar(
            progress_container,
            variable=self.progress_var,
            mode='determinate',
            bootstyle="warning-striped",
            length=400
        )
        self.progress_bar.pack(fill=X, pady=(0, 5))
        
    def create_footer_frame(self, parent):
        """Crear footer con marca registrada"""
        footer_frame = ttk_bs.Frame(parent)
        footer_frame.pack(fill=X, pady=(20, 10), expand=False)
        
        # Separador visual
        separator = ttk_bs.Separator(footer_frame, orient="horizontal")
        separator.pack(fill=X, pady=(0, 10))
        
        # Marca registrada con mejor visibilidad
        copyright_label = ttk_bs.Label(
            footer_frame,
            text=f"© {datetime.now().year} Juan Coronato - Todos los derechos reservados",
            font=("Arial", 10, "italic"),
            bootstyle="secondary"
        )
        copyright_label.pack(anchor="center", pady=(0, 5))
        
    # Funciones auxiliares de la interfaz
    def paste_from_clipboard(self):
        try:
            clipboard_content = self.root.clipboard_get()
            self.video_url.set(clipboard_content)
        except:
            messagebox.showwarning("Advertencia", "No se pudo obtener contenido del portapapeles")
            
    def browse_audio_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de audio",
            filetypes=[
                ("Archivos de audio", "*.mp3 *.wav *.m4a *.aac *.ogg *.flac"),
                ("Todos los archivos", "*.*")
            ]
        )
        if file_path:
            self.audio_file_path.set(file_path)
            
    def browse_video_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de video",
            filetypes=[
                ("Archivos de video", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv"),
                ("Todos los archivos", "*.*")
            ]
        )
        if file_path:
            self.video_file_path.set(file_path)
            
    def browse_output_path(self):
        folder_path = filedialog.askdirectory(title="Seleccionar carpeta de destino")
        if folder_path:
            self.output_path.set(folder_path)
            
    def get_language_code(self, language_display):
        lang_map = {
            "🇪🇸 Español": "es",
            "🇺🇸 Inglés": "en", 
            "🇫🇷 Francés": "fr",
            "🇩🇪 Alemán": "de",
            "🇮🇹 Italiano": "it",
            "🇵🇹 Portugués": "pt",
            "🇯🇵 Japonés": "ja",
            "🇰🇷 Coreano": "ko",
            "🇨🇳 Chino": "zh",
            "🇷🇺 Ruso": "ru"
        }
        return lang_map.get(language_display, "es")
        
    # Funciones adaptadas del código original
    def clean_filename(self, filename):
        return re.sub(r'[\\/*?:"<>|]', "", filename)
        
    def download_audio_from_youtube(self, video_url, output_path):
        self.update_status("Obteniendo información del video...")
        self.progress_var.set(10)
        
        # Obtener información del video
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'audio_sin_nombre')
            clean_title = self.clean_filename(video_title)
        
        self.update_status("Descargando audio...")
        self.progress_var.set(30)
        
        # Configurar descarga
        clean_output_path = os.path.join(output_path, f"{clean_title}.%(ext)s")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': clean_output_path,
            'quiet': True,
        }
        
        # Descargar
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        self.progress_var.set(70)
        
        clean_audio_file = f"{clean_title}.mp3"
        clean_full_path = os.path.join(output_path, clean_audio_file)
        
        return clean_full_path, clean_title
        
    def download_video_from_youtube(self, video_url, quality, output_path):
        self.update_status("Obteniendo información del video...")
        self.progress_var.set(10)
        
        # Obtener información del video
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'video_sin_nombre')
            clean_title = self.clean_filename(video_title)
        
        self.update_status("Descargando video...")
        self.progress_var.set(30)
        
        # Configurar descarga
        clean_output_path = os.path.join(output_path, f"{clean_title}.%(ext)s")
        
        ydl_opts = {
            'format': f'bestvideo[height={quality}]+bestaudio/best',
            'outtmpl': clean_output_path,
            'quiet': True,
        }
        
        # Descargar
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        self.progress_var.set(90)
        
        clean_video_file = f"{clean_title}.mp4"
        clean_full_path = os.path.join(output_path, clean_video_file)
        
        return clean_full_path, clean_title
        
    def transcribe_audio(self, audio_path, language='es'):
        self.update_status("Cargando modelo de IA...")
        self.progress_var.set(20)
        
        model = whisper.load_model("base")
        
        self.update_status("Transcribiendo audio...")
        self.progress_var.set(50)
        
        result = model.transcribe(audio_path, language=language)
        return result['text']
        
    def update_status(self, message):
        self.status_var.set(message)
        self.root.update_idletasks()
        
    # Funciones de inicio de procesos (ejecutadas en hilos separados)
    def start_transcribe_youtube(self):
        if not self.video_url.get().strip():
            messagebox.showerror("Error", "Por favor ingresa una URL válida")
            return
            
        # Ejecutar en hilo separado para no bloquear la interfaz
        threading.Thread(target=self.transcribe_youtube_worker, daemon=True).start()
        
    def transcribe_youtube_worker(self):
        try:
            self.progress_var.set(0)
            url = self.video_url.get().strip()
            lang_code = self.get_language_code(self.language.get())
            output_path = self.output_path.get()
            
            # Descargar audio
            audio_file, title = self.download_audio_from_youtube(url, output_path)
            
            # Transcribir
            transcription = self.transcribe_audio(audio_file, language=lang_code)
            
            # Guardar transcripción
            self.update_status("Guardando transcripción...")
            self.progress_var.set(90)
            
            text_file = os.path.join(output_path, f"{title}.txt")
            with open(text_file, "w", encoding="utf-8") as file:
                file.write(transcription)
            
            self.progress_var.set(100)
            self.update_status("¡Transcripción completada!")
            
            # Preguntar si eliminar audio
            result = messagebox.askyesno(
                "Transcripción completada", 
                f"¡Transcripción guardada exitosamente!\n\n"
                f"Archivo: {text_file}\n\n"
                f"¿Deseas eliminar el archivo de audio descargado?"
            )
            
            if result and os.path.exists(audio_file):
                os.remove(audio_file)
                self.update_status("Audio eliminado. ¡Proceso completado!")
            else:
                self.update_status("¡Proceso completado!")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la transcripción: {str(e)}")
            self.update_status("Error en la transcripción")
            self.progress_var.set(0)
            
    def start_transcribe_local(self):
        if not self.audio_file_path.get().strip():
            messagebox.showerror("Error", "Por favor selecciona un archivo de audio")
            return
            
        threading.Thread(target=self.transcribe_local_worker, daemon=True).start()
        
    def transcribe_local_worker(self):
        try:
            self.progress_var.set(0)
            audio_path = self.audio_file_path.get()
            lang_code = self.get_language_code(self.language.get())
            
            if not os.path.exists(audio_path):
                messagebox.showerror("Error", "El archivo seleccionado no existe")
                return
            
            # Transcribir
            transcription = self.transcribe_audio(audio_path, language=lang_code)
            
            # Guardar transcripción
            self.update_status("Guardando transcripción...")
            self.progress_var.set(90)
            
            output_path = os.path.splitext(audio_path)[0] + ".txt"
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(transcription)
            
            self.progress_var.set(100)
            self.update_status("¡Transcripción completada!")
            
            messagebox.showinfo(
                "Transcripción completada",
                f"¡Transcripción guardada exitosamente!\n\nArchivo: {output_path}"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la transcripción: {str(e)}")
            self.update_status("Error en la transcripción")
            self.progress_var.set(0)
            
    def start_transcribe_video(self):
        if not self.video_file_path.get().strip():
            messagebox.showerror("Error", "Por favor selecciona un archivo de video")
            return
            
        threading.Thread(target=self.transcribe_video_worker, daemon=True).start()
        
    def transcribe_video_worker(self):
        try:
            self.progress_var.set(0)
            video_path = self.video_file_path.get()
            lang_code = self.get_language_code(self.language.get())
            
            if not os.path.exists(video_path):
                messagebox.showerror("Error", "El archivo seleccionado no existe")
                return
            
            # Extraer audio del video
            self.update_status("Extrayendo audio del video...")
            self.progress_var.set(20)
            
            # Crear nombre temporal para el audio extraído
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            temp_audio_path = os.path.join(os.path.dirname(video_path), f"{video_name}_temp_audio.mp3")
            
            # Usar FFmpeg para extraer audio (a través de whisper que ya lo maneja internamente)
            # Whisper puede procesar directamente archivos de video
            transcription = self.transcribe_audio(video_path, language=lang_code)
            
            # Guardar transcripción
            self.update_status("Guardando transcripción...")
            self.progress_var.set(90)
            
            output_path = os.path.splitext(video_path)[0] + ".txt"
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(transcription)
            
            self.progress_var.set(100)
            self.update_status("¡Transcripción completada!")
            
            messagebox.showinfo(
                "Transcripción completada",
                f"¡Transcripción guardada exitosamente!\n\nArchivo: {output_path}"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la transcripción: {str(e)}")
            self.update_status("Error en la transcripción")
            self.progress_var.set(0)
            
    def start_download_video(self):
        if not self.video_url.get().strip():
            messagebox.showerror("Error", "Por favor ingresa una URL válida")
            return
            
        threading.Thread(target=self.download_video_worker, daemon=True).start()
        
    def download_video_worker(self):
        try:
            self.progress_var.set(0)
            url = self.video_url.get().strip()
            quality = self.quality.get().replace('p', '')
            output_path = self.output_path.get()
            
            video_file, title = self.download_video_from_youtube(url, quality, output_path)
            
            self.progress_var.set(100)
            self.update_status("¡Descarga completada!")
            
            messagebox.showinfo(
                "Descarga completada",
                f"¡Video descargado exitosamente!\n\nArchivo: {video_file}"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la descarga: {str(e)}")
            self.update_status("Error en la descarga")
            self.progress_var.set(0)
            
    def start_download_audio(self):
        if not self.video_url.get().strip():
            messagebox.showerror("Error", "Por favor ingresa una URL válida")
            return
            
        threading.Thread(target=self.download_audio_worker, daemon=True).start()
        
    def download_audio_worker(self):
        try:
            self.progress_var.set(0)
            url = self.video_url.get().strip()
            output_path = self.output_path.get()
            
            audio_file, title = self.download_audio_from_youtube(url, output_path)
            
            self.progress_var.set(100)
            self.update_status("¡Descarga completada!")
            
            messagebox.showinfo(
                "Descarga completada",
                f"¡Audio descargado exitosamente!\n\nArchivo: {audio_file}"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la descarga: {str(e)}")
            self.update_status("Error en la descarga")
            self.progress_var.set(0)
            
    def run(self):
        # Centrar ventana y asegurar tamaño mínimo
        self.root.update_idletasks()
        
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calcular dimensiones apropiadas (80% de la pantalla como máximo)
        max_width = int(screen_width * 0.8)
        max_height = int(screen_height * 0.85)
        
        # Usar el tamaño configurado o el máximo si es menor
        width = min(900, max_width)
        height = min(750, max_height)
        
        # Centrar ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Asegurar que la ventana no salga de los límites
        x = max(0, x)
        y = max(0, y)
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Configurar redimensionamiento
        self.root.minsize(850, 700)
        self.root.maxsize(screen_width, screen_height)
        
        self.root.mainloop()

if __name__ == "__main__":
    app = TranscribeYTGUI()
    app.run() 