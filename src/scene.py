import tkinter as tk
from tkinter import Canvas
from snail import Snail

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