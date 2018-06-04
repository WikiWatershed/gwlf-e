import numpy as np
from gwlfe.Timer import time_function
from GRLostBarnN import GRLostBarnN

def GRLostBarnNSum(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                   Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y] += gr_lost_barn_n[Y][i]
    return result


def GRLostBarnNSum_2():
    pass
