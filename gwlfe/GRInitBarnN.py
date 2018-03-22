import numpy as np
from Timer import time_function
from GRAccManAppN import GRAccManAppN
from GRAccManAppN import GRAccManAppN_2
from GRAppManN import GRAppManN
from GRAppManN import GRAppManN_2


def GRInitBarnN(InitGrN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    gr_acc_man_app_n = GRAccManAppN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)
    gr_app_man_n = GRAppManN(GRPctManApp,InitGrN)
    for i in range(12):
        result[i] = gr_acc_man_app_n[i] - gr_app_man_n[i]
    return result


def GRInitBarnN_2(InitGrN, GRPctManApp, GrazingN):
    result = GRAccManAppN_2(InitGrN, GRPctManApp, GrazingN) - GRAppManN_2(GRPctManApp,InitGrN)
    return result
