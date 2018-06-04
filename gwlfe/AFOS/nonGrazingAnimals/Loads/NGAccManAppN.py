import numpy as np
from gwlfe.Timer import time_function
from InitNgN import InitNgN
from InitNgN import InitNgN_2


def NGAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp):
    result = np.zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        # For Non-Grazing
        result[i] += (init_ng_n / 12) - (NGPctManApp[i] * init_ng_n)
        if result[i] < 0:
            result[i] = 0
    return result


def NGAccManAppN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp):
    init_ng_n = InitNgN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    return np.maximum((init_ng_n / 12) - (NGPctManApp * init_ng_n),0)
