from numpy import sum
from numpy import zeros

from .AnimalN import AnimalN
from .AnimalN import AnimalN_f
from gwlfe.Memoization import memoize


def AvAnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
              NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
              RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    result = zeros((12,))
    animal_n = AnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                       DaysMonth,
                       NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                       NgAWMSCoeffN,
                       RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                       GrazingNRate)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += animal_n[Y][i] / NYrs
    return result


@memoize
def AvAnimalN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    return sum(AnimalN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                         DaysMonth,
                         NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                         NgAWMSCoeffN,
                         RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                         GrazingNRate), axis=0) / NYrs
