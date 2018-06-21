from AvAnimalN import AvAnimalN
from AvAnimalN import AvAnimalN_2

from numpy import sum as npsum


def AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                 RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    av_animal_n = AvAnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                            DaysMonth,
                            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                            NgAWMSCoeffN,
                            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                            GrazingNRate)
    result = sum(av_animal_n)
    return result


def AvAnimalNSum_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                 RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    return npsum(AvAnimalN_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                            DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate,
                            AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct,
                            GrAWMSCoeffN, PctStreams, GrazingNRate))
