from numpy import maximum
from numpy import minimum
from numpy import ndarray
from numpy import reshape
from numpy import tile
from numpy import zeros

from gwlfe.AFOS.GrazingAnimals.Loads.GRAppManN import GRAppManN
from gwlfe.AFOS.GrazingAnimals.Loads.GRAppManN import GRAppManN_2
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_2


def GRLostManN(NYrs, GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate, Prec, DaysMonth,
               GRPctSoilIncRate):
    result = zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    gr_app_man_n = GRAppManN(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (gr_app_man_n[i] * GRAppNRate[i] * loss_fact_adj[Y][i] * (1 - GRPctSoilIncRate[i]))
            if result[Y][i] > gr_app_man_n[i]:
                result[Y][i] = gr_app_man_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostManN_2(NYrs, GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate, Prec, DaysMonth,
                 GRPctSoilIncRate):
    lossFactAdj = LossFactAdj_2(Prec, DaysMonth)
    gr_app_man_n = GRAppManN_2(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    result = (tile(gr_app_man_n, NYrs) * tile(GRAppNRate, NYrs) * ndarray.flatten(lossFactAdj) * tile(
        (1 - GRPctSoilIncRate), NYrs))
    result = minimum(result, tile(gr_app_man_n, NYrs))
    result = maximum(result, 0)
    return reshape(result, (NYrs, 12))
