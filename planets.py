class Planet:
    def __init__(self, name, distance, order):
        self.name = name
        self.distance = distance
        self.order = order

    def getDistance(self):
        return self.distance

    def getOrder(self):
        return self.order

    def getName(self):
        return self.name