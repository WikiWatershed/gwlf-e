import numpy as np
from gwlfe.Timer import time_function
from N7b import N7b


def N7b_1(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
          GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct,
          GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct, NGBarnNRate, NgAWMSCoeffN, n41d,
          n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64, NPConvert):
    n7b = N7b(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
              GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct,
              GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct, NGBarnNRate, NgAWMSCoeffN,
              n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64)
    result = n7b * NPConvert
    return result


def N7b_1_2():
    pass
