import numpy as np
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.AFOS.nonGrazingAnimals.Loads.NGInitBarnN import NGInitBarnN


def NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    ng_init_barn_n = NGInitBarnN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i]
                            - ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i] * AWMSNgPct * NgAWMSCoeffN
                            + ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > ng_init_barn_n[i]:
                result[Y][i] = ng_init_barn_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostBarnN_2(NYrs, NGInitBarnN, NGBarnNRate, Precipitation, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct,
                  RunConCoeffN):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    result = (np.tile(NGInitBarnN, NYrs) * np.tile(NGBarnNRate, NYrs) * np.ndarray.flatten(lossFactAdj) * (
            1 - (AWMSNgPct * NgAWMSCoeffN) + (RunContPct * RunConCoeffN)))
    result = np.minimum(result, np.tile(NGInitBarnN, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))


def AvNGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                  Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((12,))
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += ng_lost_barn_n[Y][i] / NYrs
    return result


def AvNGLostBarnN_2():
    pass


def AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    av_ng_lost_barn_n = AvNGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                      NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = sum(av_ng_lost_barn_n)
    return result


def AvNGLostBarnNSum_2():
    pass

def NGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                   DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs,))
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y] += ng_lost_barn_n[Y][i]
    return result


def NGLostBarnNSum_2():
    pass
