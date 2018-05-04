import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo


def NGLoadN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((9,))
    for a in range(9):
        if GrazingAnimal[a] is YesOrNo.NO:
            result[a] = (NumAnimals[a] * AvgAnimalWt[a] / 1000) * AnimalDailyN[a] * 365
    return result


def NGLoadN_2():
    pass
