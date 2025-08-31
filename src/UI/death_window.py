import tkinter as tk
import datetime
import os
from threading import Timer
from playsound import playsound

PATH = os.path.abspath("media/audio/horror.mp3")

class DeathWindow:

    def __init__(self):
        # Al instanciar la clase se ejecutan las dos funciones
        Timer(5, self.kill).start()
        Timer(0.5, self.sound).start()
        self.death_window()
        

    def death_window(self):
        window = tk.Tk()
        window.config(bg="black")
        window.overrideredirect(True)
        window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")

        game_over = tk.Label(
            window,
            bg="black",
            text="GAME OVER",
            font=("bold", 48),
            fg="red"
        )
        
        label_datetime = tk.Label(
            window,
            bg="black",
            text=f"{datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')}",
            font=("bold", 20),
            fg="red"
        )
        
        game_over.place(relx=0.5, rely=0.5, anchor="center")
        label_datetime.place(relx=0.5, rely=0.6, anchor="center")

        window.mainloop()
    
    def kill(self):
        print("Muerto")
    
    def sound(self):
        playsound(PATH)


if __name__ == '__main__':
    DeathWindow()
