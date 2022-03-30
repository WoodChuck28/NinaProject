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
GJ15Ab = Planet("GJ 15 A b", 733596.5, 7)
AUmicro = Planet("AU Microsopii b", 2024000, 8)
GJ1132 = Planet("GJ 1132", 2593000, 9)
kepler16b = Planet("Kepler-16 b", 12650000, 10)
kepler22b = Planet("Kepler-22 b", 39210000, 11)
WASP12b = Planet("WASP-12 b", 55070330, 12)
kepler7b = Planet("Kepler-7 b", 63240000, 13)
HD17156b = Planet("HD 17156 b", 16130000, 14)
kepler452b = Planet("Kepler-452 b", 113830000, 15)
OGLE2005 = Planet("OGLE-2005-BLG-309L b", 208700000, 16)


# adding planets to big list
planets.append(mars)
planets.append(jupiter)
planets.append(saturn)
planets.append(uranus)
planets.append(neptune)
planets.append(pluto)
planets.append(GJ15Ab)
planets.append(AUmicro)
planets.append(GJ1132)
planets.append(kepler16b)
planets.append(kepler22b)
planets.append(WASP12b)
planets.append(kepler7b)
planets.append(HD17156b)
planets.append(kepler452b)
planets.append(OGLE2005)

# creating array for plantery distances in meters
planet_distances_m = []

# loop through all of the planets and convert from AU to meters.
for entry in planets:
    meters = convertAU(entry.distance)
    planet_distances_m.append(meters)
