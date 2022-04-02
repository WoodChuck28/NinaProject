def calculateExponentialDrift(currentDriftTime, driftValue, timeInterval):
    driftValue = timeInterval * (1.0 + driftValue)
    #driftTime = currentDriftTime + driftValue
    return driftValue




