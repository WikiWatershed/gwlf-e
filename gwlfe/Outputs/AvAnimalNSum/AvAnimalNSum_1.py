import numpy as np
from gwlfe.Timer import time_function
from N7b import N7b
from N7b import N7b_2
from gwlfe.Memoization import memoize


def AvAnimalNSum_1(NYrs, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
                   GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate,
                   Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp,
                   AWMSNgPct, NGBarnNRate, NgAWMSCoeffN, n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64):
    n7b = N7b(NYrs, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
              GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct,
              GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct, NGBarnNRate, NgAWMSCoeffN,
              n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64)
    result = n7b
    return result

@memoize
def AvAnimalNSum_1_2(NYrs, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
                   GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate,
                   Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp,
                   AWMSNgPct, NGBarnNRate, NgAWMSCoeffN, n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64):
    return N7b_2(NYrs, Grazinganimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
        GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct,
        GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct, NGBarnNRate, NgAWMSCoeffN,
        n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64)
