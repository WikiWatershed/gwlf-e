from numpy import sum

from gwlfe.AFOS.GrazingAnimals.Losses.AvGRLostBarnN import AvGRLostBarnN
from gwlfe.AFOS.GrazingAnimals.Losses.AvGRLostBarnN import AvGRLostBarnN_f
from gwlfe.Memoization import memoize


def AvGRLostBarnNSum(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                     Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    av_gr_lost_barn_n = AvGRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                      PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct,
                                      RunConCoeffN)
    result = sum(av_gr_lost_barn_n)
    return result


@memoize
def AvGRLostBarnNSum_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                       GRBarnNRate,
                       Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    return sum(
        AvGRLostBarnN_f(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                        PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN))
