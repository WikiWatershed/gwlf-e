import numpy as np
from gwlfe.Timer import time_function
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_2
from gwlfe.AFOS.GrazingAnimals.Loads.GRInitBarnN import GRInitBarnN
from gwlfe.AFOS.GrazingAnimals.Loads.GRInitBarnN import GRInitBarnN_2


def GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    gr_init_barn_n = GRInitBarnN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
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


def GRLostBarnN_2(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                  PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    loss_fact_adj = LossFactAdj_2(Prec, DaysMonth)
    gr_init_barn_n = GRInitBarnN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)

    years_gr_init_barn_gr_barn_n_rate = np.resize(gr_init_barn_n * GRBarnNRate,
                                                  (NYrs, 12)) * loss_fact_adj  # TODO: what is a better name for this
    result = years_gr_init_barn_gr_barn_n_rate + \
             years_gr_init_barn_gr_barn_n_rate * (AWMSGrPct * GrAWMSCoeffN - RunContPct * RunConCoeffN)
    result = np.minimum(result, np.resize(gr_init_barn_n, (NYrs, 12)))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))
