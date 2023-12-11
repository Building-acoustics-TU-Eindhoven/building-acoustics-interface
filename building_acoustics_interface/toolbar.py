from tkinter import *

class Toolbar:
    def __init__(self, root):
        self.menu = Menu(root)
        root.config(menu=self.menu)

        #File toolbar menu
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Upload file", command=uploadFile)
        self.subMenu.add_command(label="Delete", command=deleteFile)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="exit", command=doNothing)

        #Environments settings toolbar menu
        self.environmentSettings = Menu(self.menu)
        self.menu.add_cascade(label="Environment Settings", menu=self.environmentSettings)
        self.environmentSettings.add_command(label="airdensity", command=changeAirDensity)

        #Material settings toolbar menu
        self.materialSettings = Menu(self.menu)
        self.menu.add_cascade(label="Material Settings", menu=self.materialSettings)
        self.materialSettings.add_command(label="wood", command=changeMaterial)

        #Graph results toolbar menu
        self.graphResults = Menu(self.menu)
        self.menu.add_cascade(label="Graph Results", menu=self.graphResults)
        self.graphResults.add_command(label="Gausian", command=addGaussian)

        #Numeric results toolbar menu
        self.numericResults = Menu(self.menu)
        self.menu.add_cascade(label="Numeric Results", menu=self.numericResults)
        self.numericResults.add_command(label="Reverb", command=addReverb)

        #position Emitters and Receivers toolbar menu
        self.posEmittersAndReceivers = Menu(self.menu)
        self.menu.add_cascade(label="sound Emitters/Receivers", menu=self.posEmittersAndReceivers)
        self.posEmittersAndReceivers.add_command(label="Emitters", command=setPosition)

#added for test purposes
def doNothing():
    print("ok i wont do shit")

def uploadFile():
    print("uploading file...")

def deleteFile():
    print("deleting file....")

def changeAirDensity():
    print("Air density changed....")

def changeMaterial():
    print("changed to wood")

def addGaussian():
    print("Gaussian added")

def addReverb():
    print("added reverb... (beetboxsounds)")

def setPosition():
    print("set the position of receiver")


    










