import numpy as np

from NGAccManAppN import NGAccManAppN
from NGAccManAppN import NGAccManAppN_2
from NGAppManN import NGAppManN
from NGAppManN import NGAppManN_2


def NGInitBarnN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    ng_app_man_n = NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    ng_acc_man_app_n = NGAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp)
    for i in range(12):
        result[i] = ng_acc_man_app_n[i] - ng_app_man_n[i]
        if result[i] < 0:
            result[i] = 0
    return result


def NGInitBarnN_2(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    ng_app_man_n = NGAppManN_2(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    ng_acc_man_app_n = NGAccManAppN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp)
    return np.maximum(ng_acc_man_app_n - ng_app_man_n, 0)[None,:]
