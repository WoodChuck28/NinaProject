from distances import *
from planetaryJourney import ship_journey
from spaceShip import SpaceShip
import pandas as pd 
from planetsList import planets, planet_distances_m


def runOneClockModel():
    light = 300000000

    for i in range(len(planets)):
        print(f'Calculating {planets[i]} one way data')
        df = ship_journey(planet_distances_m[i], light)
        # Think of this as creating a huge matrix of all of the data so it is easy to export=

        # this is simple but awesome, it takes our huge matrix and exports it to a csv datafile.
        df.to_csv("NinaData/" + planets[i].name + "OneWay" + "data.csv")


