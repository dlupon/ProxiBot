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

    # MESSAGES
    initMessage = ""

    # PROPERTIES
    running : bool = True

    # LOCALISATION
    DEFAULT_CONFIDENCE : float = .7

    # COMMANDS

    commands : dict = None

    ################################### MESSAGE

    def InitMessage(): OP.Out(App.initMessage, Fore.CYAN)

    ################################### INIT

    def Run():
        App.Init()
        App.Loop()
        App.End()

    def Init():
        App.InitAction()
        App.InitMessage()

    def InitAction() : pass

    ################################### LOOP
    
    def Loop():
        lInput : str = None
        while App.running:
            lInput = IP.AskForCommand(App.commands)
            OP.Clear()
            App.CheckForCommands(lInput)

    ################################### COMMANDS

    def CheckForCommands(pCommand : str):
        pass


    ################################### NAVIGATION

    def Locate(pImage : str, pConfidence : float = App.DEFAULT_CONFIDENCE) -> Point | None:
        lPoint : Point = None
        try: lPoint = pyautogui.locateCenterOnScreen(pImage, confidence = pConfidence)
        except: return None
        return lPoint

    ################################### END

    def Stop(): App.running = False

    def End():
        OP.Out("Done !", Fore.GREEN)
        time.sleep(1)