import numpy as np
from AvAnimalN import AvAnimalN
from AvAnimalN import AvAnimalN_2


def AvAnimalNSum(NYrs, NGPctManApp, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                 RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    av_animal_n = AvAnimalN(NYrs, NGPctManApp, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                            DaysMonth,
                            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                            NgAWMSCoeffN,
                            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,
                            GrazingNRate)
    result = sum(av_animal_n)
    return result


def AvAnimalNSum_2(NYrs, NGPctManApp, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
                 RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    return np.sum(AvAnimalN_2(NYrs, NGPctManApp, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec,
                            DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate,
                            AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct,
                            GrAWMSCoeffN, PctStreams, GrazingNRate))
