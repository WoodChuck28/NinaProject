from planetsList import planets, planet_distances_m
from distances import *
from planetaryJourney2 import ship_journey_twoWay
import pandas as pd 

def runTwoClockModel():
    light = 300000000

    #creating empty planets list
    
    for i in range(len(planets)):
        print(f'Calculating {planets[i]} two way data')
        df = ship_journey_twoWay(planet_distances_m[i], light)
        # Think of this as creating a huge matrix of all of the data so it is easy to export=

        # this is simple but awesome, it takes our huge matrix and exports it to a csv datafile.
        df.to_csv("NinaData/" + planets[i].name + "TwoWay" + "data.csv")

