# autor : LUPON Dylan
# date ; 07 / 12 / 2024

import time
import random

from InputManager import InputManager as IP

class Program:
    
    ################################### VARIABLES

    running : bool = True

    ################################### Run

    def Run():
        Program.Init()
        Program.Loop()

    def Init():
        pass

    ################################### LOOP
    
    def Loop():
        while Program.running:
            break
        
        print("Done !")
        time.sleep(1)