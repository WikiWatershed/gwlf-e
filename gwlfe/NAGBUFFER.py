import numpy as np
from Timer import time_function
from NGLBN import NGLBN
from GRLBN import GRLBN
from GRSN import GRSN


def NAGBUFFER(n42, n43, n64, n7b, NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
              Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp, PctGrazing, GRBarnNRate,
              AWMSGrPct, GrAWMSCoeffN,PctStreams):
    nglbn = NGLBN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                  Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    grlbn = GRLBN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    grsn = GRSN(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    if n42 > 0:
        result = (n43 / n42) * n64 * (n7b - (nglbn + grlbn + grsn))
    else:
        result = 0
    return result


def NAGBUFFER_2():
    pass
