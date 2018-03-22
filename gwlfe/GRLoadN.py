import numpy as np
from Timer import time_function
from enums import YesOrNo
from Constants import NAnimals


def GRLoadN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((NAnimals,))
    for a in range(9):
        if GrazingAnimal[a] is YesOrNo.NO:
            pass
        elif GrazingAnimal[a] is YesOrNo.YES:
            result[a] = (NumAnimals[a] * AvgAnimalWt[a] / 1000) * AnimalDailyN[a] * 365
    return result


def GRLoadN_2():
    pass
