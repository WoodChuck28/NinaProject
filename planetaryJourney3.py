from numpy import half
from distances import *
from threeClockFunctions import *
from driftTime import *
from spaceShip import SpaceShip
import pandas as pd

#Current master function responsible for bulk of the work. 
#The goal is to model a spaceship flying through space, and updating
#values every so often to demonstrate the effect we are looking for.
#It will take a distance and calculate things based on that entered distance
def ship_journey_threeWay( destination_distance, light) -> pd.DataFrame:
    #creating a spaceship with a speed of 350000 m/s
    myShip = SpaceShip(350000)
    #creating empty master array which will ultimately house all of our data
    master_array = []
    #creating an empty position array that will store our positions over time
    ship_positions = []
    #time ticks
    time_values = []
    #drift time values
    drift_time_values1 = []
    
    #array for how long the time to correct will take, should start small
    time_to_correct = []
    #array to demonstrate how far our ship will go while waiting for instructions
    distancesWithoutCorrection = []

    distancesWithoutCorrection2 = []
    #starting time
    time = 1
    #driftValues here
    driftTimeValue1 = .000001
    #calculating roughly how long our trip SHOULD take
    time_to_destination = destination_distance / myShip.speed

    #Loop that will run until we hit the trip time.
    while time < time_to_destination:
        ship_pos = myShip.getNewPosition(time)
        myShip.add_dist(ship_pos)
        ship_positions.append(ship_pos)
        time_values.append(time)
        

        halfwayPoint = destination_distance / 2
        if ship_pos <= halfwayPoint:
            #difference = (halfwayPoint-myShip.posX)
            correctionTime = myShip.getTimeToCorrectThreeWay(light)
            driftTime = calculateDriftTime(correctionTime, driftTimeValue1)
        else:
            correctionTime = planetTimeToTarget(destination_distance, ship_pos, light)
            driftTime = calculateDriftTime(correctionTime, driftTimeValue1)
        time_to_correct.append(correctionTime)
        drift_time_values1.append(driftTime)

        distanceWithoutCorrection = myShip.getDistanceWhileWaiting(correctionTime)
        distanceWithoutCorrection2 = myShip.getDistanceWhileWaiting(driftTime)
        distancesWithoutCorrection.append(distanceWithoutCorrection)
        distancesWithoutCorrection2.append(distanceWithoutCorrection2)
        time = time + 86400

    #add all of our mini arrays to the one BIG array
    df = pd.DataFrame()

    df['Ship Positions'] = ship_positions
    # master_array.append(ship_positions)

    df['Time Values'] = time_values
    # master_array.append(time_values)

    df['Time to Correct'] = time_to_correct
    # master_array.append(time_to_correct)

    df['Drift Time Values'] = drift_time_values1
    # master_array.append(drift_time_values1)

    df['Distances Without Correction'] = distancesWithoutCorrection
    # master_array.append(distancesWithoutCorrection)

    df['Distances Without Correction 2'] = distancesWithoutCorrection2
    # master_array.append(distancesWithoutCorrection2)

    #return our master array so it can be exported in main code file.
    return df



