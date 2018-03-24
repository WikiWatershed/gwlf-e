import numpy as np
from Timer import time_function
from AvAnimalN import AvAnimalN


def AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,GrazingNRate):
    av_animal_n = AvAnimalN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,GrazingNRate)
    result = sum(av_animal_n)
    return result


def AvAnimalNSum_2():
    pass
