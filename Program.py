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

    ################################### INIT

    def Run():
        Program.Init()
        Program.Loop()
        Program.End()

    def Init():
        OP.InitMessage()

    ################################### LOOP
    
    def Loop():
        lInput : str = None
        while Program.running:
            lInput = IP.AskForCommand(IP.commands)
            OP.Clear()
            Program.CheckForCommands(lInput)

    ################################### COMMANDS

    def CheckForCommands(pCommand : str):
        if (pCommand == "exit"): Program.running = False
        elif (pCommand == "help"): OP.Help()


    ################################### NAVIGATION

    def Locate(pImage : str) -> Point | None:
        lPoint : Point = None
        try: lPoint = pyautogui.locateCenterOnScreen(pImage, confidence = Program.CONFIDENCE)
        except: return None
        return lPoint

    ################################### END

    def End():
        OP.Out("Done !", Fore.GREEN)
        time.sleep(1)