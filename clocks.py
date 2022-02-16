class CesiumClock:
    def __init__(self, driftValue, actualTime = 0, driftTime = 0):
        self.driftValue = driftValue
        self.actualTime = actualTime
        self.driftTime = driftTime

    def editDriftTime(self, currentTime):
        self.actualTime = self.actualTime + currentTime
        self.driftTime = self.actualTime * self.driftValue
        theDrift = self.driftTime
        return theDrift

    def addTime(self, actualTimePassed, driftTimePassed):
        self.actualTime = self.actualTime + actualTimePassed
        self.driftTime = self.driftTime + driftTimePassed
