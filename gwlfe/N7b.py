import numpy as np
from Timer import time_function
from AvAnimalNSum import AvAnimalNSum
from NAWMSL import NAWMSL
from NAWMSP import NAWMSP
from NRUNCON import NRUNCON
from NFENCING import NFENCING
from NAGBUFFER import NAGBUFFER

def N7b(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,NGPctSoilIncRate,GRAppNRate,GRPctSoilIncRate,GrazingNRate,GRPctManApp, PctGrazing, GRBarnNRate,
        Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct,
        NGBarnNRate, NgAWMSCoeffN, n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69,n43, n64, n7b):
    av_animal_n_sum = AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,GrazingNRate)
    nawmsl = NAWMSL(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                    Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h)
    nawmsp = NAWMSP(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                    Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j)
    nruncon = NRUNCON(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
            Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate, AWMSNgPct,
            NgAWMSCoeffN,n41f,n85l)
    nfencing = NFENCING(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN,n42,n45,n69)
    nagbuffer = NAGBUFFER(n42, n43, n64, n7b, NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
              Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp, PctGrazing, GRBarnNRate,
              AWMSGrPct, GrAWMSCoeffN,PctStreams)

    result = av_animal_n_sum
    result = result - (nawmsl + nawmsp + nruncon + nfencing + nagbuffer)
    return result


def n7b_2():
    pass
