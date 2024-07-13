#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.app.info import APP_NAME
from src.etc.imports import ctk, platform
from src.etc.variables import logo_file

# Controls the dimensions of the application.
APP_WIDTH = 450
APP_HEIGHT = 300

# Create main window
APP = ctk.CTk()
APP.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
APP.title(APP_NAME)
APP.iconbitmap(logo_file)
APP.wm_attributes("-topmost", True)

# Set minimum and maximum APP dimensions
APP.minsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura mínima em pixels
APP.maxsize(width=APP_WIDTH, height=APP_HEIGHT)  # Altura máxima em pixels

# Get screen dimensions
SCREEN_WIDTH = APP.winfo_screenwidth()
SCREEN_HEIGHT = APP.winfo_screenheight()

# Calculate central window position
posicao_x = (SCREEN_WIDTH - APP_WIDTH) // 2
posicao_y = (SCREEN_HEIGHT - APP_HEIGHT) // 2

# Set window geometry (centered on screen)
APP.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{posicao_x}+{posicao_y}")

# Configuração inicial do customtkinter
ctk.set_appearance_mode("dark")  # Modo "dark"
ctk.set_default_color_theme("blue")  # Tema azul

# Sets the application icon "only if the platform is Windows", because on Linux the icon may not be displayed in the
# window header.
if platform == 'win32':
    try:
        APP.iconbitmap(r"src\image\logo.ico")
    except FileNotFoundError:
        APP.iconbitmap(r"_internal\resources\image\logo.ico")
