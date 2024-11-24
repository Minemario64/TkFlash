from customerrors import *
import time

class SpeedrunTimer:

    TimeFormats = ["hrs:mins:secs", "mins:secs", "secs", "hrs:mins"]
    PrintFormats = ["normal", "dynamic"]

    def __init__(self, timeFormat : str = "secs", printFormat : str = "normal"):
        if timeFormat in self.TimeFormats:
            self.timeFormat = timeFormat
        else:
            raise TkFlashError("timer error", "Error : Invalid Time Format")
        if printFormat in self.PrintFormats:
            self.printFormat = printFormat
        else:
            raise TkFlashError("timer error", "Error : Invalid Print Format")

    def start(self):
        self.startTime = time.time()
        self.totalTime = 0

    def pause(self):
        self.pauseTime = time.time()
        self.totalTime = self.pauseTime - self.startTime

    def unpause(self):
        self.startTime = time.time()

    def stop(self):
        self.stopTime = time.time()
        if self.totalTime > 0:
            self.totalTime += self.stopTime - self.startTime
        elif self.totalTime == 0:
            self.totalTime = self.stopTime - self.startTime

    def get_time(self, precision : int = None, prefix : str = "Time Lapsed - ") -> str:
        if precision is None:
            time = self.totalTime
        else:
            time = float(f"{self.totalTime:.{precision}f}")

        if self.printFormat == "normal":
            separates = {"hrs" : " : ", "mins" : " : "}
        elif self.printFormat == "dynamic":
            separates = {"hrs" : " hours, ", "mins" : " minutes, ", "secs" : " seconds"}

        if self.timeFormat == "hrs:mins:secs":
            mins = time // 60
            sec = time % 60
            hours = mins // 60
            mins = mins % 60
            try:
                return f"{prefix}{int(hours)}{separates["hrs"]}{int(mins)}{separates["mins"]}{sec}" + separates["secs"]
            except:
                return f"{prefix}{int(hours)}{separates["hrs"]}{int(mins)}{separates["mins"]}{sec}"
        elif self.timeFormat == "secs":
            try:
                return f"{prefix}{time}" + separates["secs"]
            except:
                return f"{prefix}{time}"
        elif self.timeFormat == "mins:secs":
            mins = time // 60
            sec = time % 60
            try:
                return f"{prefix}{int(mins)}{separates["mins"]}{sec}" + separates["secs"]
            except:
                return f"{prefix}{int(mins)}{separates["mins"]}{sec}"
        elif self.timeFormat == "hrs:mins":
            mins = time // 60
            sec = time % 60
            hours = mins // 60
            mins = mins % 60
            try:
                test = separates["secs"]
                return f"{prefix}{int(hours)}{separates["hrs"]}{mins}" + separates["mins"]
            except:
                return f"{prefix}{int(hours)}{separates["hrs"]}{mins}"