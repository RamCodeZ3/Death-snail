import tkinter as tk
import math
from ui.death_window import DeathWindow


class Snail:
    def __init__(self, scene, speed=1.0):
        # Definicion de los atributos del caracol
        self.scene = scene
        self.image = tk.PhotoImage(file="./media/image/Snail.png")
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
        
        if (self.x, self.y) == (cx, cy):
            DeathWindow()
            
        # Mover al caracol
        self.scene.canvas.coords(self.imageRef, self.x, self.y)