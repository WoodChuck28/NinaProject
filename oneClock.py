from planets import Planet
from distances import *
from planetaryJourney import ship_journey
from spaceShip import SpaceShip
import pandas as pd 
import csv

light = 300000000

#creating empty lists to be filled in with our code
actualTimes = []
driftTimes = []
actualDistances = []
driftDistances= []

#creating empty planets list
planets = []

#define planets, distances, and their order from earth
mars = Planet("Mars", .5, 1)
jupiter = Planet("Jupiter", 4.2, 2)
saturn = Planet("Saturn", 8.6, 3)
uranus = Planet("Uranus", 18.2, 4)
neptune = Planet("Neptune", 29.0, 5)
pluto = Planet("Pluto", 38.5, 6)

planets.append(mars)
planets.append(jupiter)
planets.append(saturn)
planets.append(uranus)
planets.append(neptune)
planets.append(pluto)

planet_distances_m = []

for entry in planets:
    meters = convertAU(entry.distance)
    planet_distances_m.append(meters)

master_array = ship_journey(planet_distances_m[1], light)

dataframe = pd.DataFrame(master_array)
dataframe.to_csv(r"C:/Users/17703/Sandbox/PythonProjects/NinaProject/data.csv")


