from numpy import sum

from .NGLostBarnN import NGLostBarnN


def NGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                   DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    # result = zeros((NYrs,))
    result = sum(
        NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                    DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN), axis=1)
    return result


def NGLostBarnNSum_f():
    pass
