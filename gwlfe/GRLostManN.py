import numpy as np
from Timer import time_function
import LossFactAdj
from GRAppManN import GRAppManN

def GRLostManN(NYrs, GRPctManApp,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN, GRAppNRate, Prec, DaysMonth, GRPctSoilIncRate):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj.LossFactAdj(NYrs, Prec, DaysMonth)
    gr_app_man_n = GRAppManN(GRPctManApp,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (gr_app_man_n[i] * GRAppNRate[i] * loss_fact_adj[Y][i] * (1 - GRPctSoilIncRate[i]))
            if result[Y][i] > gr_app_man_n[i]:
                result[Y][i] = gr_app_man_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostManN_2(NYrs, GRAppManN, GRAppNRate, Precipitation, DaysMonth, GRPctSoilIncRate):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    result = (np.tile( GRAppManN,NYrs) * np.tile( GRAppNRate, NYrs) * np.ndarray.flatten(lossFactAdj) * np.tile(( 1 - GRPctSoilIncRate),NYrs ))
    result = np.minimum(result, np.tile( GRAppManN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))