from tkinter import *
WhiteBusTracker = __import__('White Bus Tracker')


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Village Bus Tracker")
        #  Frames
        self.rootFrame = Frame(self.root, bg="dodgerblue")
        self.buttonFrame = Frame(self.rootFrame, bg="dodgerblue")
        self.messageFrame = Frame(self.rootFrame, bg="dodgerblue")
        #  Buttons
        self.checkBusTimesButton = Button(self.buttonFrame, text="Check Bus Times", bg="grey",
                                          command=self.checkBusTimes)
        self.trackBus = Button(self.buttonFrame, text="Start Tracking buses")
        self.stopTracking = Button(self.buttonFrame, text="Stop Tracking")
        #  Text Box
        self.textBox = Text(self.messageFrame, height=10, width=37)
        #  Packing Frames
        self.rootFrame.pack()
        self.buttonFrame.pack(side="top")
        self.messageFrame.pack(side="bottom")
        #  Packing Buttons
        self.checkBusTimesButton.grid(row=0, column=0)
        self.trackBus.grid(row=0, column=1)
        self.stopTracking.grid(row=0, column=2)
        #  Packing Text Box
        self.textBox.pack()
        #  Initialize busWatcher
        self.watcher = WhiteBusTracker.BusWatcher()

    def checkBusTimes(self):
        try:
            self.watcher.updateTimes()
            times = self.watcher.getLatestBus()
            message = "Latest Bus Arrival Time: " + times[0] + "\nOther Bus Arrival Times: \n"
            for i in range(1, len(times)):
                message = message + "\t" + times[i] + "\n"
        except IndexError:
            message = "No buses are running"
        self.textBox.delete(1.0, END)
        self.textBox.insert(END, message)



root = Tk()
gui = GUI(root)
root.mainloop()
