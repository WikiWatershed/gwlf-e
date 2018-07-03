from numpy import sum

from gwlfe.Memoization import memoize


def TotLAEU(NumAnimals, AvgAnimalWt):
    result = 0
    aeu3 = (NumAnimals[5] * AvgAnimalWt[5]) / 1000
    aeu4 = (NumAnimals[4] * AvgAnimalWt[4]) / 1000
    aeu5 = (NumAnimals[6] * AvgAnimalWt[6]) / 1000
    aeu6 = (NumAnimals[0] * AvgAnimalWt[0]) / 1000
    aeu7 = (NumAnimals[1] * AvgAnimalWt[1]) / 1000
    result += aeu3 + aeu4 + aeu5 + aeu6 + aeu7
    return result


@memoize
def TotLAEU_f(NumAnimals, AvgAnimalWt):
    return sum(NumAnimals[[0, 1, 4, 5, 6]] * AvgAnimalWt[[0, 1, 4, 5, 6]] / 1000)
