from distances import *
from planetaryJourney import ship_journey
from spaceShip import SpaceShip
import pandas as pd 
from planetsList import planets, planet_distances_m

def runOneClockModel():
    light = 300000000

    for i in range(5):
        master_array = ship_journey(planet_distances_m[i], light, 31536000000 ,.0000000000003)
        #Think of this as creating a huge matrix of all of the data so it is easy to export
        dataframe = pd.DataFrame(master_array)

        #this is simple but awesome, it takes our huge matrix and exports it to a csv datafile.
        dataframe.to_csv(r"C:/Users/17703/Sandbox/PythonProjects/NinaProject/PlanetData/BigDistances/"+planets[i].name+"OneWay"+"data.csv")


