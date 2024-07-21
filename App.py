# autor : LUPON Dylan
# date : 07 / 16 / 2024

import time
import pyautogui
from colorama import Fore, Back, Style
from pyautogui import Point

from InputManager import InputManager as IPM
from Console import Output as OP
from Console import Input as IP

from os import system
class App:

    ################################### VARIABLES

    DEFAULT_CONFIDENCE : float = .7

    ################################### MESSAGE

    def LocationMessage(self): OP.OutInfo(self.locationMessage)

    ################################### INIT

    def __init__(self):
        self.locationMessage : str = ""
        self.commands : dict = None
        self.running : bool = True
        self.userPrefix = "App"
        self.InitVariables()
        self.InitAction()
        self.LocationMessage()

    def Run(self):
        self.Loop()
        self.End()

    def InitVariables(self): pass
        
    def InitAction(self): pass

    ################################### LOOP
    
    def Loop(self):
        lInput : str = None
        while self.running:
            lInput = IP.AskForCommand(self.commands, pUserPrefix = self.userPrefix)
            OP.Clear()
            self.CheckForCommands(lInput)

    ################################### COMMANDS

    def CheckForCommands(self, pCommand : str): pass

    ################################### NAVIGATION

    def Locate(self, pImage : str, pConfidence : float = DEFAULT_CONFIDENCE) -> Point | None:
        lPoint : Point = None
        try: lPoint = pyautogui.locateCenterOnScreen(pImage, confidence = pConfidence)
        except: return None
        return lPoint

    ################################### END

    def Stop(self): self.running = False

    def End(self):
        OP.Out("Done !", Fore.GREEN)
        time.sleep(1)