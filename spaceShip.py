class SpaceShip:
    def __init__(self, speed, posX=0, actualTime=0, driftTime=0):
        self.speed = speed
        self.posX = posX
        self.actualTime = actualTime
        self.driftTime = driftTime

    def add_dist(self, newDistance):
        self.posX = self.posX + newDistance

    def changeTime(self, timePassed):
        self.actualTime = self.actualTime + timePassed

    
