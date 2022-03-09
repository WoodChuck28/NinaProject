def calculateDriftTime(time, driftValueOne, driftValueTwo=0, driftValueThree=0):
    timeArray = []
    driftValue1 = driftValueOne + 1.0
    driftValue2 = driftValueTwo + 1.0
    driftValue3 = driftValueThree + 1.0

    newtime1 = driftValue1 * time
    newtime2 = driftValue2 * time
    newtime3 = driftValue3 * time

    timeArray.append(newtime1)
    timeArray.append(newtime2)
    timeArray.append(newtime3)

    return timeArray
