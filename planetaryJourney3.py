from numpy import half
from distances import *
from threeClockFunctions import *
from driftTime import *
from spaceShip import SpaceShip
from newDriftTime import calculateExponentialDrift


#Current master function responsible for bulk of the work. 
#The goal is to model a spaceship flying through space, and updating
#values every so often to demonstrate the effect we are looking for.
#It will take a distance and calculate things based on that entered distance
def ship_journey_threeWay( destination_distance, light, timeInterval, driftValue):
    #creating a spaceship with a speed of 350000 m/s
    myShip = SpaceShip(156000)
    #creating empty master array which will ultimately house all of our data
    master_array = []
    #creating an empty position array that will store our positions over time
    ship_positions = []
    drift_positions = []
    #time ticks
    time_values = []
    #drift time values
    drift_time_values1 = []
    
    #array for how long the time to correct will take, should start small
    time_to_correct = []
    time_to_correct2 = []
    #array to demonstrate how far our ship will go while waiting for instructions
    distancesWithoutCorrection = []
    distancesWithoutCorrection2 = []
    #starting time
    time = 1
    driftTime = 1
    
    #calculating roughly how long our trip SHOULD take
    time_to_destination = destination_distance / myShip.speed

    #Loop that will run until we hit the trip time.
    while time < time_to_destination:
        ship_pos = myShip.getNewPosition(time)
        drift_pos = myShip.getNewPosition(driftTime)
        myShip.add_dist(ship_pos)
        myShip.add_drift_dist(drift_pos)
        ship_positions.append(ship_pos)
        drift_positions.append(drift_pos)
        time_values.append(time)
        drift_time_values1.append(driftTime)
        
        halfwayPoint = destination_distance / 2
        
        if ship_pos <= halfwayPoint:
            #difference = (halfwayPoint-myShip.posX)
            correctionTime = myShip.getTimeToCorrectThreeWay(light)
            correctionTime2 = myShip.getTimeToCorrectThreeWay2(light)
            calculatedDrift = calculateExponentialDrift(driftTime, driftValue, timeInterval)
            
        else:
            correctionTime = planetTimeToTarget(destination_distance, ship_pos, light)
            correctionTime2 = planetTimeToTarget2(destination_distance, drift_pos, light)
            calculatedDrift = calculateExponentialDrift(driftTime, driftValue, timeInterval)
            #driftTime = driftTime + calculatedDrift
        time_to_correct.append(correctionTime)
        time_to_correct2.append(correctionTime2)
        driftTime = driftTime + calculatedDrift

        #drift_time_values1.append(driftTime)

        distanceWithoutCorrection = myShip.getDistanceWhileWaiting(correctionTime)
        distanceWithoutCorrection2 = myShip.getDistanceWhileWaiting(correctionTime2)
        distancesWithoutCorrection.append(distanceWithoutCorrection)
        distancesWithoutCorrection2.append(distanceWithoutCorrection2)
        time = time + timeInterval

    #add all of our mini arrays to the one BIG array
    master_array.append(time_values)
    #Time with drift roughly applied
    master_array.append(drift_time_values1)
    #Distance travelled without correction for base time
    master_array.append(distancesWithoutCorrection)
    #Distance travelled without correction for drift time
    master_array.append(distancesWithoutCorrection2)
    #Time to correct using base time
    master_array.append(time_to_correct)
    #Ship position using base time
    master_array.append(ship_positions)

    #return our master array so it can be exported in main code file.
    return master_array



