def planetTimeToTarget(planetDistanceFromEarth, shipPositionFromEarth, light):
    differenceDistance = planetDistanceFromEarth - shipPositionFromEarth
    timeDelay = differenceDistance / light
    return timeDelay

def planetTimeToTarget2(planetDistanceFromEarth, driftPositionFromEarth, light):
    differenceDistance = planetDistanceFromEarth - driftPositionFromEarth
    timeDelay = differenceDistance / light
    return timeDelay
    
    

