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
        "help" : "Show this menu.",
        "setup" : "WIP...",
        "start" : "WIP...",
        "stop" : "I think it stops the program ?"
        }

    ################################### COMMANDS

    def CheckForCommands(self, pCommand : str):
        if (pCommand == "help") : OP.Help(self.commands)
        elif (pCommand == "setup") : self.Setup()
        elif (pCommand == "start") : pass
        elif (pCommand == "stop") : self.Stop()

    ################################### SETUP

    def Setup(self):
        self.SetupMessage()
        self.SetupDrive()

    def SetupMessage(self): OP.Out(self.setupMessage)
        

    def SetupDrive(self):
        OP.OutInstruction("Go to the drive and select the first line to check (a the very left of the line)\nThen get back to the consol and type anithing")
        IP.JustAnswer("No Command Just Wait For Inputs")
        IPM.KeyShortCut("alt", "tab")
        IPM.KeyShortCut("home")
        IPM.KeyShortCut("enter")
        IPM.KeyType("test")


    ################################### START

    def Start(self): pass