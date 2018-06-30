from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnNSum import NGLostBarnNSum


def NAWMSP_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
             Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j):
    ng_lost_barn_n_sum = NGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                        NGBarnNRate, Prec,
                                        DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = (n41d / 100) * n85j * ng_lost_barn_n_sum
    return result


# def NAWMSP_2_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
#                Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j):
#     return (n41d / 100) * n85j * AvNGLostBarnNSum_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt,
#                                                     AnimalDailyN, NGBarnNRate,
#                                                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
