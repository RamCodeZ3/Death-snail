import tkinter as tk


class DeathWindow():
    def __init__(self):
        window = tk.Tk()
        window.config(bg="black")
        window.overrideredirect(True)

        window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")

        label = tk.Label(
            window,
            bg="black",
            text="GAME OVER",
            font=("bold", 48),
            fg="red")
        
        label.place(relx=0.5, rely=0.5, anchor="center")

        window.mainloop()