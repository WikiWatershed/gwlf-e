import numpy as np
from gwlfe.Timer import time_function
from gwlfe.AFOS.GrazingAnimals.Loads.GRAccManAppN import GRAccManAppN
from gwlfe.AFOS.GrazingAnimals.Loads.GRAccManAppN import GRAccManAppN_2
from GRAppManN import GRAppManN
from GRAppManN import GRAppManN_2


def GRInitBarnN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    gr_acc_man_app_n = GRAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)
    gr_app_man_n = GRAppManN(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = gr_acc_man_app_n[i] - gr_app_man_n[i]
    return result


def GRInitBarnN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    return GRAccManAppN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                          PctGrazing) - GRAppManN_2(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
