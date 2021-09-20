from numpy import sum
from numpy import zeros

from .GRLostBarnN import GRLostBarnN


def GRLBN_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
            Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = zeros((NYrs))
    gr_lost_barn_n = sum(
        GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                    GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN), axis=1)
    for y in range(NYrs):
        result[y] = gr_lost_barn_n[y]
    return result


def GRLBN_2_f():
    pass
