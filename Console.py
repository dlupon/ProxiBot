# autor : LUPON Dylan
# date : 07 / 13 / 2024

import winsound
import time
import sys 
from os import system
from colorama import Fore, Back, Style

class Output:

    INIT : str = "#################################################################\n#                            PROXIBOT                           #\n#################################################################"
    CREDITS : str = "                                                        by dLupon"
    README : str = "What is ProxiBot :\n\rThe Job i was doing was really repetitive,\n\rso i decided to make a script to do it for me hehe."

    # Properties
    allOutputs : list = []
    lastOutput : str = ""

    # Sounds
    BEEP_ASK : tuple = (500, 500)
    BEEP_GOOD : tuple = (600, 500)
    BEEP_ERROR : tuple = (400, 500)

    # Help
    HELP_COLOR : str = Fore.YELLOW

    ################################### OUT

    def Out(pMessage : str = "", pColor : str = Fore.RESET, pBackColor : str = Back.RESET, pAddToHistory : bool = True):
        lOutput : str = pColor + pBackColor + pMessage + Style.RESET_ALL
        if pAddToHistory: Output.AddToHostory(lOutput)
        print(lOutput)

    def Clear(pDeleteLastOutput = True):
        if pDeleteLastOutput: Output.lastOutput = ""
        system("cls")

    def Jump(pJumpsCount : int = 1):
        for lJump in range(pJumpsCount): Output.Out()

    ################################### HISTORY

    def AddToHostory(pOutput : str):
        Output.lastOutput += pOutput + " \n"
        Output.allOutputs.append(pOutput)

    def ShowLastOutputs():
        Output.Clear(False)
        print(Output.lastOutput[0 : len(Output.lastOutput) - 3])

    def ShowHisroty():
        Output.Clear()
        lLength = len(Output.allOutputs)
        for lOutputIndex in range(lLength):
            print(Output.allOutputs[lOutputIndex])

    ################################### INIT

    def InitMessage():
        Output.Clear()
        Output.Copyright()
        Output.Jump(2)
        Output.Out(Output.README)
        
    def Copyright():
        Output.Out(Output.INIT, Fore.GREEN)
        Output.Out(Output.CREDITS, Fore.GREEN)

    ################################### HELP

    def Help(pCommand : list):
        Output.Jump()
        Output.Out(f"Help :", Output.HELP_COLOR)
        Output.Jump()
        for lCommandName in Input.commands:
            Output.Out(f"{lCommandName} : {pCommand[lCommandName]}", Output.HELP_COLOR)
        Output.Jump()
    
    ################################### SOUND

    def Beep(pBeep : tuple): winsound.Beep(pBeep[0], pBeep[1])


class Input:

    # Aking Properties
    QUESTION_COLOR : str = Fore.CYAN
    ANSWER_COLOR : str = QUESTION_COLOR
    ANSWER_BACKGROUND_COLOR : str = Back.BLUE

    DEFAULT_QUESTION : str = "ENTER CMD"
    DEFAULT_USER_PREFIX : str = "User Input >  "

    ################################### SOUND
    
    def JustAsk(pQuestion : str = DEFAULT_QUESTION):
        Output.Out(pQuestion, Input.QUESTION_COLOR, pAddToHistory = False)

    def JustAnswer(pUserPrefix : str = DEFAULT_USER_PREFIX) -> str:
        pUserPrefix = Input.QUESTION_COLOR + pUserPrefix + Input.ANSWER_BACKGROUND_COLOR + Input.ANSWER_COLOR
        lInput : str = input(pUserPrefix + Style.RESET_ALL)
        return lInput
    
    def Ask(pQuestion : str = DEFAULT_QUESTION, pUserPrefix : str = DEFAULT_USER_PREFIX) -> str:
        Input.JustAsk(pQuestion)
        return Input.JustAnswer(pUserPrefix)

    def AskForCommand(pCommands : dict, pQuestion : str = DEFAULT_QUESTION, pUserPrefix : str = DEFAULT_USER_PREFIX) -> str:
        lInput = None
        Output.Beep(Output.BEEP_ASK)
        while lInput == None:
            lInput = Input.Ask(pQuestion, pUserPrefix)
            if not (lInput in pCommands):
                Output.Beep(Output.BEEP_ERROR)
                Output.ShowLastOutputs()
                lInput = None
        Output.Beep(Output.BEEP_GOOD)
        return lInput
