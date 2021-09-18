from numpy import average
from numpy import zeros

from .GRLostBarnN import GRLostBarnN
from .GRLostBarnN import GRLostBarnN_f
from gwlfe.Memoization import memoize


def AvGRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = zeros((12,))
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += gr_lost_barn_n[Y][i] / NYrs
    return result


@memoize
def AvGRLostBarnN_f(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                    PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    return average(
        GRLostBarnN_f(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                      PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN), axis=0)
