from .AvGRLostBarnNSum import AvGRLostBarnNSum
from .AvGRLostBarnNSum import AvGRLostBarnNSum_f
from gwlfe.Memoization import memoize


def GRLBN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
          Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    av_gr_lost_barn_n_sum = AvGRLostBarnNSum(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                             PctGrazing, GRBarnNRate,
                                             Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    result = av_gr_lost_barn_n_sum
    return result


@memoize
def GRLBN_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
            Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    return AvGRLostBarnNSum_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                              GRBarnNRate,
                              Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
