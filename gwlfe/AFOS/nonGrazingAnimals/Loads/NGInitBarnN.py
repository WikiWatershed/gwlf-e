import numpy as np
from gwlfe.Timer import time_function
from NGAppManN import NGAppManN
from NGAccManAppN import NGAccManAppN


def NGInitBarnN(NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    ng_app_man_n = NGAppManN(NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    ng_acc_man_app_n = NGAccManAppN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp)
    for i in range(12):
        result[i] = ng_acc_man_app_n[i] - ng_app_man_n[i]
        if result[i] < 0:
            result[i] = 0
    return result


def NGInitBarnN_2():
    pass
