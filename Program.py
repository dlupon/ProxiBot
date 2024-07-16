# autor : LUPON Dylan
# date : 07 / 12 / 2024

from App import *
from IndexEntry import IndexEntry as IE

class Program(App):
    ################################### VARIABLES

    # MESSAGES
    initMessage : str = "You are currently running nothing"

    # COMMANDS
    commands : dict = {
        "help" : "Show this menu.",
        "envoieEDC" : "Not available yes...",
        "saisieCompteur" : "Not available yes...",
        "indexEntry" : "Work in progress...",
        "stop" : "I think it stops the program ?"
    }

    ################################### MESSAGES

    def InitAction(): OP.InitMessage()

    ################################### COMMANDS

    def CheckForCommands(pCommand : str):
        if (pCommand == "exit"): App.Stop()
        elif (pCommand == "help"): OP.Help(App.commands)
        elif (pCommand == "indexEntry"): IE.Run()