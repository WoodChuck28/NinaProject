from clocks import CesiumClock
from spaceShip import SpaceShip
from planets import Planet
from distances import *

#creating empty lists to be filled in with our code
actualTimes = []
driftTimes = []
actualDistances = []
driftDistances= []

#creating empty planets list
planets = []

#define planets, distances, and their order from earth
mars = Planet("Mars", 345000000, 1)
jupiter = Planet("Jupiter", 654000000, 2)
neptune = Planet("Neptune", 999000000, 3)

#add planets to planets array
planets.append(mars)
planets.append(jupiter)
planets.append(neptune)

#create spaceship
myShip = SpaceShip(340000)

for entry in planets:
    distance = entry[1]
    time  = myShip.getTimeToTarget(distance)
    actualTimes.append(time)

print(actualTimes)

