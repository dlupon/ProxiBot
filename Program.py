# autor : LUPON Dylan
# date ; 07 / 12 / 2024

import time
import pyautogui
from colorama import Fore, Back, Style
from pyautogui import Point

from InputManager import InputManager as IPM
from Console import Output as OP
from Console import Input as IP

class Program:
    
    ################################### VARIABLES

    running : bool = True

    # LOCALISATION
    CONFIDENCE : float = .7

    ################################### Run

    def Run():
        Program.Init()
        Program.Loop()

    def Init():
        OP.InitMessage()
        IP.AskForCommand(IP.commands)

    ################################### LOOP
    
    def Loop():
        while Program.running:
            break
        
        OP.Out("Done !", Fore.GREEN)
        time.sleep(1)

    ################################### NAVIGATION

    def Locate(pImage : str) -> Point | None:
        lPoint : Point = None
        try: lPoint = pyautogui.locateCenterOnScreen(pImage, confidence = Program.CONFIDENCE)
        except: return None
        return lPoint

    ################################### MESSAGE