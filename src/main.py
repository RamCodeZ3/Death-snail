import tkinter as tk
from tkinter import Canvas
import ctypes
import os
import math


class Snail:
    def __init__(self, scene, speed=1.0):
        # Definicion de los atributos del caracol
        self.scene = scene
        self.image = tk.PhotoImage(file="./image/Snail.png")
        self.imageRef = self.scene.canvas.create_image(0, 0, image=self.image, anchor="center")
        self.x = 0.0
        self.y = 0.0
        self.speed = speed

    def update(self): #Funcion que se encarga del movimiento del caracol
        # Posición del cursor en pantalla
        sx, sy = self.scene.canvas.winfo_pointerxy()
        # Convertir a coordenadas del canvas
        cx = sx - self.scene.canvas.winfo_rootx()
        cy = sy - self.scene.canvas.winfo_rooty()

        # Calcular vector hacia el cursor
        dx = cx - self.x
        dy = cy - self.y
        dist = math.sqrt(dx*dx + dy*dy)

        if dist > self.speed:  # si está lejos, avanzar poco a poco
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed
        else:  # si ya está cerca, ponerlo encima
            self.x, self.y = cx, cy

        # Mover al caracol
        self.scene.canvas.coords(self.imageRef, self.x, self.y)


class Scene:
    def __init__(self, window: tk.Tk):
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()
        self.canvas = Canvas(
            window,
            width=self.screen_width,
            height=self.screen_height,
            highlightthickness=0,
            bg='white'
        )
        self.canvas.pack()

        # Crear el caracol en la escena
        self.snail = Snail(self)

    def update(self):
        self.snail.update()


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


if __name__ == '__main__':
    window = Window()
    window.start()