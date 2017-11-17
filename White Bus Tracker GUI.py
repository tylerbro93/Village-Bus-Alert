from tkinter import *


class GUI:
    def __init__(self, root):
        self.root = root
        #  Frames
        self.rootFrame = Frame(self.root, bg="grey2")
        self.buttonFrame = Frame(self.rootFrame, bg="dodgerblue")
        self.messageFrame = Frame(self.rootFrame, bg="grey2")
        #  Buttons
        self.checkBusTimesButton = Button(self.buttonFrame, text="Check Bus Times", bg="grey")
        self.trackBus = Button(self.buttonFrame, text="Start Tracking buses")
        self.stopTracking = Button(self.buttonFrame, text="Stop Tracking")
        #  Packing Frames
        self.rootFrame.pack()
        self.buttonFrame.pack(side="top")
        self.messageFrame.pack(side="bottom")
        #  Packing Buttons
        self.checkBusTimesButton.grid(row=0, column=0)
        self.trackBus.grid(row=0, column=1)
        self.stopTracking.grid(row=1, column=0)



root = Tk()
gui = GUI(root)
root.mainloop()

