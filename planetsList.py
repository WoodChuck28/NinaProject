from planets import Planet
from distances import *

planets = []

# define planets, distances in AU, and their order from earth
mars = Planet("Mars", .5, 1)
jupiter = Planet("Jupiter", 4.2, 2)
saturn = Planet("Saturn", 8.6, 3)
uranus = Planet("Uranus", 18.2, 4)
neptune = Planet("Neptune", 29.0, 5)
pluto = Planet("Pluto", 38.5, 6)

# adding planets to big list
planets.append(mars)
planets.append(jupiter)
planets.append(saturn)
planets.append(uranus)
planets.append(neptune)
planets.append(pluto)

# creating array for plantery distances in meters
planet_distances_m = []

# loop through all of the planets and convert from AU to meters.
for entry in planets:
    meters = convertAU(entry.distance)
    planet_distances_m.append(meters)
