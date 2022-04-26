def calculateExponentialDrift(currentDriftTime, driftValue, timeInterval):
    driftValue = timeInterval + (timeInterval*driftValue)
    #driftTime = currentDriftTime + driftValue
    return driftValue




