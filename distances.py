def calculateDistance(time, speed):
    distance = speed * time
    return distance

def calculateDelay(distance, lightSpeed):
    delayTime = distance / lightSpeed
    return delayTime


def convertAU(auRating):
    kiloDistance = auRating * 150000000000
    return kiloDistance

