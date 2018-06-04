import numpy as np

from gwlfe.AFOS.nonGrazingAnimals.Loads.NGAppManN import NGAppManN
from gwlfe.AFOS.nonGrazingAnimals.Loads.NGAppManN import NGAppManN_2
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_2


def NGLostManN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
               NGPctSoilIncRate):
    # Non-grazing animal losses
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
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


def NGLostManN_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate):
    lossFactAdj = LossFactAdj_2(Prec, DaysMonth)
    ng_app_man_n = NGAppManN_2(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    result = np.tile(ng_app_man_n * NGAppNRate * (1 - NGPctSoilIncRate), NYrs) * np.ndarray.flatten(lossFactAdj)
    result = np.minimum(result, np.tile(ng_app_man_n, NYrs))  # TODO: should eliminate the double tile
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))
