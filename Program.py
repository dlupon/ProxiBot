# autor : LUPON Dylan
# date ; 07 / 12 / 2024

import time
import random

from InputManager import InputManager as IP

class Program:
    
    ################################### VARIABLES

    running : bool = true

    ################################### Run

    def Run():
        Init()
        Loop()

    def Init():
        pass

    ################################### LOOP
    
    def Loop():
        Init()

        while running:
            break
        
        print("Done !")
        time.sleep(1)