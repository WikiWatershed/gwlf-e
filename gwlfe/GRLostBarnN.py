import numpy as np
from Timer import time_function
import LossFactAdj
import GRInitBarnN

def GRLostBarnN(NYrs, InitGrN, GRPctManApp, PctGrazing, GRBarnNRate, Precipitation, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    gr_init_barn_n = GRInitBarnN.GRInitBarnN(InitGrN, GRPctManApp, PctGrazing)
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


def GRLostBarnN_2(NYrs, GRAppManN, InitGrN, GRPctManApp, GrazingN, GRBarnNRate, Precipitation, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct):
    loss_fact_adj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    gr_init_barn_n = GRInitBarnN.GRInitBarnN(GRAppManN, InitGrN, GRPctManApp, GrazingN)
    result = ( np.tile(gr_init_barn_n, NYrs) * np.tile(GRBarnNRate,NYrs) * np.ndarray.flatten(loss_fact_adj) * (1 - (AWMSGrPct * GrAWMSCoeffN) + (RunContPct * RunContPct)  ) )
    result = np.minimum(result, np.tile(gr_init_barn_n, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))
