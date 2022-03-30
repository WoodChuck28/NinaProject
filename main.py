from oneClock import runOneClockModel
from planetaryJourney import ship_journey
from planetaryJourney2 import ship_journey_twoWay
from planetaryJourney3 import ship_journey_threeWay
from twoClock import runTwoClockModel
from threeClock import runThreeClockModel
import os
from planetsList import planets, planet_distances_m


def main():
    light = 300000000
    # Creates NinaData folder if it doesn't already exist
    if not os.path.isdir('NinaData'):
        os.mkdir('NinaData')

    # runOneClockModel()
    # runTwoClockModel()
    # runThreeClockModel()

    for i in range(len(planets)):
        print(f'##################################################################################################')
        print(f'Calculating {planets[i]} one clock data')
        oneClock = ship_journey(planet_distances_m[i], light)

        print(f'Calculating {planets[i]} two clock data')
        twoClock = ship_journey_twoWay(planet_distances_m[i], light)

        print(f'Calculating {planets[i]} three clock data')
        threeClock = ship_journey_threeWay(planet_distances_m[i], light)
        print(f'--------------------------------------------------------')
        oneClock['Difference'] = oneClock['Distances With Drift'] - oneClock['Distances Without Correction']
        oneClock = oneClock.abs()
        print(f'Largest one way difference: {oneClock["Difference"].max()}')

        twoClock['Difference'] = twoClock['Distances With Drift'] - twoClock['Distances Without Correction']
        twoClock = twoClock.abs()
        print(f'Largest two way difference: {twoClock["Difference"].max()}')

        threeClock['Difference'] = threeClock['Distances With Drift'] - threeClock['Distances Without Correction']
        threeClock = threeClock.abs()
        print(f'Largest three way difference: {threeClock["Difference"].max()}')
        print(f'--------------------------------------------------------')
        print(f'Saving data...')
        oneClock.to_csv("NinaData/" + planets[i].name + "OneClock" + "data.csv")
        twoClock.to_csv("NinaData/" + planets[i].name + "TwoClock" + "data.csv")
        threeClock.to_csv("NinaData/" + planets[i].name + "ThreeClock" + "data.csv")
        print('Saved!')
        print(f'##################################################################################################\n')


if __name__ == "__main__":
    main()