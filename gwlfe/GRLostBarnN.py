import numpy as np
from Timer import time_function
import LossFactAdj
import GRInitBarnN


def GRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate, Prec,
                DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj.LossFactAdj(NYrs, Prec, DaysMonth)
    gr_init_barn_n = GRInitBarnN.GRInitBarnN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                             PctGrazing)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i]
                            - gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i] * AWMSGrPct * GrAWMSCoeffN
                            + gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > gr_init_barn_n[i]:
                result[Y][i] = gr_init_barn_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostBarnN_2(NYrs, GRAppManN, InitGrN, GRPctManApp, GrazingN, GRBarnNRate, Precipitation, DaysMonth, AWMSGrPct,
                  GrAWMSCoeffN, RunContPct):
    loss_fact_adj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    gr_init_barn_n = GRInitBarnN.GRInitBarnN(GRAppManN, InitGrN, GRPctManApp, GrazingN)
    result = (np.tile(gr_init_barn_n, NYrs) * np.tile(GRBarnNRate, NYrs) * np.ndarray.flatten(loss_fact_adj) * (
            1 - (AWMSGrPct * GrAWMSCoeffN) + (RunContPct * RunContPct)))
    result = np.minimum(result, np.tile(gr_init_barn_n, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))


def GRLostBarnNSum(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                   Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y] += gr_lost_barn_n[Y][i]
    return result


def GRLostBarnNSum_2():
    pass


def AvGRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((12,))
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += gr_lost_barn_n[Y][i] / NYrs
    return result


def AvGRLostBarnN_2():
    pass


def AvGRLostBarnNSum(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                     Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    av_gr_lost_barn_n = AvGRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                      PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct,
                                      RunConCoeffN)
    result = sum(av_gr_lost_barn_n)
    return result


def AvGRLostBarnNSum_2():
    pass
