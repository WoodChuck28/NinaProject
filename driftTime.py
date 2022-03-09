def calculateDriftTime(time, driftValue1, driftValue2=0, driftValue3=0):
    timeArray = []
    newtime1 = driftValue1 * time
    newtime2 = driftValue2 * time
    newtime3 = driftValue3 * time

    timeArray.append(newtime1)
    timeArray.append(newtime2)
    timeArray.append(newtime3)

    return timeArray
