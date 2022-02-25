def planetTimeToTarget(planetDistanceFromEarth, shipPositionFromEarth, light):
    differenceDistance = planetDistanceFromEarth - shipPositionFromEarth
    timeDelay = differenceDistance / light
    return timeDelay
    

