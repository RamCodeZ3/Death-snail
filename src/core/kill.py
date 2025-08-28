import os
import time as t
from ui.death_window import DeathWindow


class Kill():
    def __init__(self):
        DeathWindow()
        
        t.sleep(2.5)
        print("Muerto")
