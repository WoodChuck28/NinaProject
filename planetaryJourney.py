from distances import *
from spaceShip import SpaceShip

#Current master function responsible for bulk of the work. 
#The goal is to model a spaceship flying through space, and updating
#values every so often to demonstrate the effect we are looking for.
#It will take a distance and calculate things based on that entered distance
def ship_journey( destination_distance, light):
    #creating a spaceship with a speed of 350000 m/s
    myShip = SpaceShip(350000)
    #creating empty master array which will ultimately house all of our data
    master_array = []
    #creating an empty position array that will store our positions over time
    ship_positions = []
    #time ticks
    time_values = []
    #array for how long the time to correct will take, should start small
    time_to_correct = []
    #array to demonstrate how far our ship will go while waiting for instructions
    distancesWithoutCorrection = []
    #starting time
    time = 1
    #calculating roughly how long our trip SHOULD take
    time_to_destination = destination_distance / myShip.speed

    #Loop that will run until we hit the trip time.
    while time < time_to_destination:
        ship_pos = myShip.getNewPosition(time)
        myShip.add_dist(ship_pos)
        ship_positions.append(ship_pos)
        time_values.append(time)
        correctionTime = myShip.getTimeToCorrect(ship_pos, light)
        time_to_correct.append(correctionTime)
        distanceWithoutCorrection = myShip.getDistanceWhileWaiting(correctionTime)
        distancesWithoutCorrection.append(distanceWithoutCorrection)
        time = time + 500

    #add all of our mini arrays to the one BIG array
    master_array.append(ship_positions)
    master_array.append(time_values)
    master_array.append(time_to_correct)
    master_array.append(distancesWithoutCorrection)

    #return our master array so it can be exported in main code file.
    return master_array



