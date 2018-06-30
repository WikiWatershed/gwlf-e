from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum_f


def NAWMSP(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
           Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j):
    nglbn = AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                             Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = (n41d / 100) * n85j * nglbn
    return result


def NAWMSP_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
             Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j):
    return (n41d / 100) * n85j * AvNGLostBarnNSum_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt,
                                                    AnimalDailyN, NGBarnNRate,
                                                    Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
