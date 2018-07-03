from numpy import maximum
from numpy import minimum
from numpy import ndarray
from numpy import reshape
from numpy import tile
from numpy import zeros

from gwlfe.AFOS.nonGrazingAnimals.Loads.NGAppManN import NGAppManN
from gwlfe.AFOS.nonGrazingAnimals.Loads.NGAppManN import NGAppManN_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_f


def NGLostManN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
               NGPctSoilIncRate):
    # Non-grazing animal losses
    result = zeros((NYrs, 12))
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


@memoize
def NGLostManN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
                 NGPctSoilIncRate):
    lossFactAdj = LossFactAdj_f(Prec, DaysMonth)
    ng_app_man_n = NGAppManN_f(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    result = tile(ng_app_man_n * NGAppNRate * (1 - NGPctSoilIncRate), NYrs) * ndarray.flatten(lossFactAdj)
    result = minimum(result, tile(ng_app_man_n, NYrs))  # TODO: should eliminate the double tile
    result = maximum(result, 0)
    return reshape(result, (NYrs, 12))
