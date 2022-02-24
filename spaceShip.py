from numpy import double


class SpaceShip:
    def __init__(self, speed, posX=0, actualTime=0, driftTime=0):
        self.speed = speed
        self.posX = posX
        self.actualTime = actualTime
        self.driftTime = driftTime

    def getTimeToCorrectTwoWay(self, distance, light):
        timeToTarget = distance / light
        doubleDistance = timeToTarget * 2
        return doubleDistance
    
    def getTimeToCorrectOneWay(self, distance, light):
        timeToTarget = distance / light
        return timeToTarget

    def add_dist(self, newDistance):
        self.posX = self.posX + newDistance

    def changeTime(self, timePassed):
        self.actualTime = self.actualTime + timePassed

    def getSpeed(self):
        return self.speed

    def getNewPosition(self, timePassed):
        distanceCovered = self.speed * timePassed
        return distanceCovered

    def getDistanceWhileWaiting(self, timeToCorrect):
        distanceWithoutCorrection = self.speed * timeToCorrect
        return distanceWithoutCorrection

    
