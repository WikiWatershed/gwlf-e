import numpy as np
from gwlfe.Timer import time_function
from InitNgN import InitNgN


def NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = NGPctManApp[i] * init_ng_n
    return result


def NGAppManN_2():
    pass
