from planets import Planet
from distances import *
from spaceShip import SpaceShip

def ship_journey( destination_distance, light):
    myShip = SpaceShip(350000)
    master_array = []
    ship_positions = []
    time_values = []
    time_to_correct = []
    distancesWithoutCorrection = []
    time = 1
    time_to_destination = destination_distance / myShip.speed
    while time < time_to_destination:
        ship_pos = myShip.getNewPosition(time)
        print(ship_pos)
        myShip.add_dist(ship_pos)
        ship_positions.append(ship_pos)
        time_values.append(time)
        correctionTime = myShip.getTimeToCorrect(ship_pos, light)
        time_to_correct.append(correctionTime)
        distanceWithoutCorrection = myShip.getDistanceWhileWaiting(correctionTime)
        distancesWithoutCorrection.append(distanceWithoutCorrection)
        time = time + 500

    master_array.append(ship_positions)
    master_array.append(time_values)
    master_array.append(time_to_correct)
    master_array.append(distancesWithoutCorrection)

    return master_array



