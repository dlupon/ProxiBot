from App import *

class IndexEntry(App):

    instance = None

    ################################### INITIALIZATION

    def MainLoop():
        if (IndexEntry.instance == None): IndexEntry.instance = IndexEntry()
        IndexEntry.instance.Run()

    def InitVariables(self):
        self.locationMessage : str = "You are currently running the Index Entry"
        self.setupMessage : str = "WIP..."
        self.userPrefix = "IndexEntry > "
        self.commands : dict = {
        "setup" : "WIP...",
        "start" : "WIP...",
        "stop" : "WIP...",
        }

    ################################### COMMANDS

    def CheckForCommands(self, pCommand : str):
        if (pCommand == "setup") : self.Setup()
        elif (pCommand == "start") : pass
        elif (pCommand == "stop") : self.Stop()

    ################################### SETUP

    def Setup(self):
        IndexEntry.SetupMessage()

    def SetupMessage(self): OP.Out(IndexEntry.setupMessage)
        
    ################################### SETUP

    def Start(self): pass