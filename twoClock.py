from planetsList import planets, planet_distances_m
from distances import *
from planetaryJourney2 import ship_journey_twoWay
import pandas as pd 

def runTwoClockModel():
    light = 300000000

    #creating empty planets list
    
    #range number chosen to designate how many planets we want to run
    for i in range(2):
        #86400 - one day in secs
        #31536000 - 10 years in secs
        master_array = ship_journey_twoWay(planet_distances_m[i], light, 3153600000 ,.0000000000003)
        #Think of this as creating a huge matrix of all of the data so it is easy to export
        dataframe = pd.DataFrame(master_array)

        #this is simple but awesome, it takes our huge matrix and exports it to a csv datafile.
        dataframe.to_csv(r"C:/Users/17703/Sandbox/PythonProjects/NinaProject/PlanetData/BigDistances/"+planets[i].name+"TwoWay"+"data.csv")


