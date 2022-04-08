from planets import Planet
from distances import *

planets = []

# define planets, distances in AU, and their order from earth
mars = Planet("Mars", .5, 1)
jupiter = Planet("Jupiter", 4.2, 2)
saturn = Planet("Saturn", 8.6, 3)
uranus = Planet("Uranus", 18.2, 4)
neptune = Planet("Neptune", 29.0, 5)
pluto = Planet("Pluto", 39.5, 6)
kepler16 = Planet("Kepler-16 B", 12700000, 7)
kepler22 = Planet("Kepler-22 B", 39200000, 8)
kepler7 = Planet("Kepler-7 B", 63200000, 9)
wasp12 = Planet("Wasp-12 B", 55070330, 10)
kepler452 = Planet("Kepler-452 B", 114000000, 11)
gj15ab = Planet("GJ 15 A b", 733596.5, 12)


# adding planets to big list
#planets.append(mars)
#planets.append(jupiter)
#planets.append(saturn)
#planets.append(uranus)
#planets.append(neptune)
#planets.append(pluto)
planets.append(wasp12)
planets.append(kepler16)
planets.append(kepler22)
planets.append(kepler7)
planets.append(kepler452)
planets.append(gj15ab)

# creating array for plantery distances in meters
planet_distances_m = []

# loop through all of the planets and convert from AU to meters.
for entry in planets:
    meters = convertAU(entry.distance)
    meters = meters * 1000
    planet_distances_m.append(meters)
