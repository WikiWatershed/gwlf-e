import numpy as np
from gwlfe.Timer import time_function
from GRLostBarnN import GRLostBarnN


def AvGRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    gr_lost_barn_n = GRLostBarnN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += gr_lost_barn_n[Y][i] / NYrs
    return result


def AvGRLostBarnN_2():
    pass