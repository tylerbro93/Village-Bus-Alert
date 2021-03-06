from time import sleep
import msvcrt
from bs4 import BeautifulSoup
from urllib.request import urlopen


class BusWatcher():
    url = "https://services.saucontds.com/public-services/public-key/stopgroups/display?publicKey=380a944f-aca4-5948" \
          "-b754-39f79e538b99&stops=The%20Gamecock%20Village&departures=true&zoom=225&hours=.5&style=redgrey&fields" \
          "=Route;Departure;Depart;Status;&expireHours=0 "
    times = []
    e = 0  # Used for error tracking. If e=0 then no error. If e=1 then error has occurred

    def __init__(self):
        self.updateTimes()

    def updateTimes(self):
        try:
            self.times.clear()
            client = urlopen(self.url, timeout=2000)
            page = client.read()
            soup_page = BeautifulSoup(page, "html.parser")

            try:
                table = soup_page.findAll("td", {"class": "td-bold"})
                for i in range(0, len(table)):
                    if ("AM" in table[i].text or "PM" in table[i].text):
                        self.times.append(table[i].text)
                self.e = 0
            except IndexError:
                print("No times available")
            client.close()
        except TimeoutError:
            print("Connection Fatal")
            self.e = 1
        except WindowsError:
            print("connection terminated by host")
            self.e = 1

    def getTimes(self):
        return self.times

    def getLatestBus(self):
        try:
            times = self.times
            return times
        except IndexError:
            return "No Buses are running"


def __tracker(obj, waitTime):
    keepGoing = True
    tenth_of_a_minute = 0  # used to keep track of how many tenths of a second has passed
    while (keepGoing == True):
        sleep(1)  # waits a tenth of a second
        tenth_of_a_minute = tenth_of_a_minute + 1
        if (msvcrt.kbhit()):
            keepGoing = False
            print("Done")
        elif (tenth_of_a_minute == waitTime):
            tenth_of_a_minute = 0
            obj.updateTimes()
            print("\n" * 80)
            try:
                print("Latest bus arrival time: " + obj.times[0])
                print("\nOther bus arrival times")
                for i in range(1, len(obj.times)):
                    print("\tArrival time: " + obj.times[i])
            except IndexError:
                if(obj.e == 0):
                    print("No bus times found")
                elif(obj.e == 1):
                    print("Could not talk to host server!")
            print("\n\nPress any key in the window's console to return to main menu")


if __name__ == "__main__":
    watcher = BusWatcher()
    keepGoing = True
    print("Type number for the choice you want to run\n")
    while (keepGoing == True):
        choice = input("1. Get times for bus arrival\n2. Track Bus\n3. Quit\nChoice: ")
        if (choice == "1"):
            __tracker(watcher, 60)
        elif (choice == "2"):
            __tracker(watcher, 10)
        else:
            keepGoing = False
