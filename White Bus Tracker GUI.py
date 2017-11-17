import datetime
from tkinter import *
import winsound
WhiteBusTracker = __import__('White Bus Tracker')


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Village Bus Tracker")
        #  Frames
        self.rootFrame = Frame(self.root, bg="purple4")
        self.buttonFrame = Frame(self.rootFrame, bg="purple4")
        self.messageFrame = Frame(self.rootFrame, bg="purple4")
        self.separator = Frame(self.rootFrame, height=10, bg="purple4")
        #  Buttons
        self.checkBusTimesButton = Button(self.buttonFrame, text="Check Bus Times", bg="slateblue4",
                                          command=self.checkBusTimes, activebackground="mediumpurple4")
        self.trackBus = Button(self.buttonFrame, text="Start Tracking buses", command=self.turnOnTracker,
                               bg="slateblue4", activebackground="mediumpurple4")
        self.stopTracking = Button(self.buttonFrame, text="Stop Tracking", command=self.turnOffTracker, state=DISABLED,
                                   bg="slateblue4", activebackground="mediumpurple4")
        #  Text Box
        self.textBox = Text(self.messageFrame, height=10, width=37, bg="slateblue4")
        #  Packing Frames
        self.rootFrame.pack()
        self.buttonFrame.pack(side="top")
        self.separator.pack(side="top", fill=X, padx=5, pady=5)
        self.messageFrame.pack(side="bottom")
        #  Packing Buttons
        self.checkBusTimesButton.grid(row=0, column=0)
        self.trackBus.grid(row=0, column=1)
        self.stopTracking.grid(row=0, column=2)
        #  Packing Text Box
        self.textBox.pack()
        #  Initialize busWatcher
        self.watcher = WhiteBusTracker.BusWatcher()
        #  Tracker Switch
        self.tracker = False
        self.trackingSystem()
        #  Renders GUI
        self.root.mainloop()

    def checkBusTimes(self):
        try:
            self.watcher.updateTimes()
            times = self.watcher.getLatestBus()
            message = ""
            if(self.watcher.e == 1):
                message = "HOST SERVER HAS REFUSED TO RESPOND!\nTIMES COULD NOT BE UPDATED!\n"
            message = message + "Latest Bus Arrival Time: " + times[0] + "\nOther Bus Arrival Times: \n"
            for i in range(1, len(times)):
                message = message + "\t" + times[i] + "\n"
        except IndexError:
            message = "No buses are running"
        self.textBox.delete(1.0, END)
        self.textBox.insert(END, message)

    def turnOnTracker(self):
        self.tracker = True
        self.trackBus.config(state=DISABLED)
        self.stopTracking.config(state=NORMAL)

    def turnOffTracker(self):
        self.tracker = False
        self.trackBus.config(state=NORMAL)
        self.stopTracking.config(state=DISABLED)

    def trackingSystem(self):
        if(self.tracker == True):
            self.checkBusTimes()
            try:
                timeString = self.watcher.times[0]
                gar, timeString = timeString.split(":")
                minute, gar = timeString.split(" ")
                currentMinute = datetime.datetime.now().minute
                if(currentMinute + 5 > int(minute)):
                    winsound.Beep(1000, 600)
            except IndexError:
                self.textBox.delete(1.0, END)
                self.textBox.insert(END, "NO BUSES ARE RUNNING!\nTRACKING IS CURRENTLY USELESS!")
        self.textBox.after(30000, self.trackingSystem)


if __name__ == "__main__":
    gui = GUI()

