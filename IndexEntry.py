from App import *

class IndexEntry(App):
    ################################### VARIABLES

    # MESSAGES
    initMessage : str = "You are currently running the Index Entry"
    setupMessage : str = "WIP..."

    # COMMANDS
    commands : dict = {
        "setup" : "WIP...",
        "start" : "WIP...",
        "stop" : "WIP...",
    }

    ################################### COMMANDS

    def CheckForCommands(pCommand : str):
        if (pCommand == "setup") : IndexEntry.Setup()
        elif (pCommand == "start") : pass
        elif (pCommand == "stop") : pass

    ################################### SETUP

    def Setup():
        IndexEntry.SetupMessage()

    def SetupMessage() : OP.Out(IndexEntry.setupMessage)
        
    ################################### SETUP

    def Start(): pass