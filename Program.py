# autor : LUPON Dylan
# date : 07 / 12 / 2024

from App import *
from IndexEntry import IndexEntry as IE

class Program(App):

    instance = None

    ################################### INITIALIZATION

    def MainLoop():
        if (Program.instance == None): Program.instance = Program()
        Program.instance.Run()

    def InitVariables(self):
        if (Program.instance == None): Program.instance = self
        self.locationMessage : str = "You are currently running nothing"
        self.userPrefix = "Program > "
        self.commands = {
        "help" : "Show this menu.",
        "envoieEDC" : "Not available yes...",
        "saisieCompteur" : "Not available yes...",
        "indexEntry" : "Work in progress...",
        "stop" : "I think it stops the program ?"
        }


    def InitAction(self): OP.InitMessage()

    ################################### COMMANDS

    def CheckForCommands(self,pCommand : str):
        if (pCommand == "stop"): self.Stop()
        elif (pCommand == "help"): OP.Help(self.commands)
        elif (pCommand == "indexEntry"): IE.MainLoop()