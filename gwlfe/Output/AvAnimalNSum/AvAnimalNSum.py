from numpy import sum as npsum

from .AvAnimalN import AvAnimalN
from .AvAnimalN import AvAnimalN_f
from gwlfe.Memoization import memoize


def AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                 RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    av_animal_n = AvAnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                            DaysMonth,
                            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                            NgAWMSCoeffN,
                            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                            GrazingNRate)
    result = sum(av_animal_n)  # TODO: should this be numpysum?
    return result


@memoize
def AvAnimalNSum_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                   DaysMonth,
                   NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                   RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                   GrazingNRate):
    return npsum(
        AvAnimalN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                    DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate,
                    AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct,
                    GrAWMSCoeffN, PctStreams, GrazingNRate))
