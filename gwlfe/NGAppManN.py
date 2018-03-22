import numpy as np
from Timer import time_function
from InitNgN import InitNgN


def NGAppManN(NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = NGPctManApp[i] * init_ng_n
    return result


def NGAppManN_2():
    pass
