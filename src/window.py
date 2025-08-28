import tkinter as tk
import ctypes
from scene import Scene


class Window():
    def __init__(self):
        self.window = self.create_window()
        self.apply_click_through(self.window)
        self.scene = Scene(self.window)

    def update(self):
        self.scene.update()
        self.window.after(5, self.update)

    def create_window(self):
        window = tk.Tk()
        window.wm_attributes("-topmost", True)
        window.attributes("-fullscreen", True) 
        window.overrideredirect(True)
        
        # Transparencia
        window.attributes('-transparentcolor', 'white')
        window.config(bg='white')
        return window

    def apply_click_through(self, window):
        # Constantes API windows
        WS_EX_TRANSPARENT = 0x00000020
        WS_EX_LAYERED = 0x00080000
        GWL_EXSTYLE = -20

        # Obtener el identificador de ventana (HWND)
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        # Obtener los estilos actuales de la ventana
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        # Establecer nuevo estilo
        style = style | WS_EX_TRANSPARENT | WS_EX_LAYERED
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)

    def start(self):
        self.update()
        self.window.mainloop()