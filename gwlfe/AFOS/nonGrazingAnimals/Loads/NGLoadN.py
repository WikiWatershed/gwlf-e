import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo
from gwlfe.GrazingAnimal import GrazingAnimal


def NGLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((9,))
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            result[a] = (NumAnimals[a] * AvgAnimalWt[a] / 1000) * AnimalDailyN[a] * 365
    return result


def NGLoadN_2():
    pass
