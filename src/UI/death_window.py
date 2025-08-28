import tkinter as tk
import datetime


class DeathWindow():
    def __init__(self):
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
            text=f"{datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")}",
            font=("bold", 20),
            fg="red"
        )
        
        game_over.place(relx=0.5, rely=0.5, anchor="center")
        label_datetime.place(relx=0.5, rely=0.6, anchor="center")  # Cambiado para estar debajo

        window.mainloop()
