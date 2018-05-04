import numpy as np
from gwlfe.Timer import time_function
from NGLostBarnN import AvNGLostBarnNSum

def NGLBN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    av_ng_lost_barn_n_sum = AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = av_ng_lost_barn_n_sum
    return result


def NGLBN_2():
    pass
