import numpy as np
from gwlfe.Timer import time_function
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.InitGrN import InitGrN
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN_2


def GRAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    grazing_n = GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = (result[i] + (init_gr_n / 12) - (GRPctManApp[i] * init_gr_n) - grazing_n[i])
        if result[i] < 0:
            result[i] = 0
    return result


def GRAccManAppN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_n = GrazingN_2(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    return np.maximum(((1.0 / 12) - GRPctManApp) * init_gr_n - grazing_n, 0)

# @time_function
# def GRAccManAppN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
#     init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
#     grazing_n = GrazingN_2(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
#     result = (np.repeat(init_gr_n / 12, 12)) - (GRPctManApp * np.repeat(init_gr_n, 12)) - grazing_n
#     result = np.maximum(result, 0)
#     return result
