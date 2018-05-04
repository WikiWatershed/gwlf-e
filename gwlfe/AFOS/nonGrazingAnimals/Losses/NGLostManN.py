import numpy as np
import gwlfe.MultiUse_Fxns.LossFactAdj
from gwlfe.AFOS.nonGrazingAnimals.Loads.NGAppManN import NGAppManN


def NGLostManN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
               NGPctSoilIncRate):
    # Non-grazing animal losses
    result = np.zeros((NYrs, 12))
    loss_fact_adj = gwlfe.MultiUse_Fxns.LossFactAdj.LossFactAdj(NYrs, Prec, DaysMonth)
    ng_app_man_n = NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (ng_app_man_n[i] * NGAppNRate[i] * loss_fact_adj[Y][i]
                            * (1 - NGPctSoilIncRate[i]))
            if result[Y][i] > ng_app_man_n[i]:
                result[Y][i] = ng_app_man_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostManN_2(NYrs, NGAppManN, NGAppNRate, Prec, DaysMonth, NGPctSoilIncRate):
    lossFactAdj = gwlfe.MultiUse_Fxns.LossFactAdj.LossFactAdj(NYrs, Prec, DaysMonth)
    result = np.tile(NGAppManN * NGAppNRate * (1 - NGPctSoilIncRate), NYrs) * np.ndarray.flatten(lossFactAdj)
    result = np.minimum(result, np.tile(NGAppManN, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))
