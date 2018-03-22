import numpy as np
from Timer import time_function
from InitNgN import InitNgN


def NGAccManAppN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp):
    result = np.zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        # For Non-Grazing
        result[i] += (init_ng_n / 12) - (NGPctManApp[i] * init_ng_n)
    return result


def NGAccManAppN_2():
    pass
