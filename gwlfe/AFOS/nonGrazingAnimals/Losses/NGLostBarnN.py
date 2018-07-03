from numpy import maximum
from numpy import repeat
from numpy import reshape
from numpy import sum
from numpy import where
from numpy import zeros

from gwlfe.AFOS.nonGrazingAnimals.Loads.NGInitBarnN import NGInitBarnN
from gwlfe.AFOS.nonGrazingAnimals.Loads.NGInitBarnN import NGInitBarnN_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_f


def NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = zeros((NYrs, 12))
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


@memoize
def NGLostBarnN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                  DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    loss_fact_adj = LossFactAdj_f(Prec, DaysMonth)
    ng_init_barn_n = reshape(
        repeat(NGInitBarnN_f(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN), repeats=NYrs,
               axis=0), (NYrs, 12))

    temp = NGBarnNRate * loss_fact_adj * (1 - AWMSNgPct * NgAWMSCoeffN + RunContPct * RunConCoeffN)
    # result would be less than the subexpression if the number that is subtracted is bigger than the one added
    adjusted = where(temp < 1)
    result = ng_init_barn_n
    result[adjusted] = ng_init_barn_n[adjusted] * temp[adjusted]
    return maximum(result, 0)


# TODO: this needs to be split into its own function
@memoize
def AvNGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                  Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = zeros((12,))
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += ng_lost_barn_n[Y][i] / NYrs
    return result


@memoize
def AvNGLostBarnN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                    Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    return sum(NGLostBarnN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                             Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN), axis=0) / NYrs


def AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    av_ng_lost_barn_n = AvNGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                      NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = sum(av_ng_lost_barn_n)
    return result


@memoize
def AvNGLostBarnNSum_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                       Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    return sum(AvNGLostBarnN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                               NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN))
