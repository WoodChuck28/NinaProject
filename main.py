from oneClock import runOneClockModel
from twoClock import runTwoClockModel
from threeClock import runThreeClockModel
import os

def main():
    # Creates NinaData folder if it doesn't already exist
    if not os.path.isdir('NinaData'):
        os.mkdir('NinaData')

    runOneClockModel()
    runTwoClockModel()
    runThreeClockModel()

if __name__ == "__main__":
    main()