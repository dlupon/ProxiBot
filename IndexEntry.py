from App import *

class IndexEntry(App):
    ################################### VARIABLES

    # MESSAGES
    initMessage : str = "You are currently running the Index Entry"

    # COMMANDS
    commands : dict = {
        "setup" : "...",
        "start" : "...",
        "stop" : "...",
    }

    ################################### COMMANDS

    def CheckForCommands(pCommand : str):
        if (pCommand == "setup") : IndexEntry.Setup()
        elif (pCommand == "start") : pass
        elif (pCommand == "stop") : pass

    def Setup(): pass

    def Start(): pass