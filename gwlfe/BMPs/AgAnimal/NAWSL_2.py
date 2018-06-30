from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN_2 import GRLBN_2
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN_2 import GRLBN_2_f


def NAWMSL_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
             Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h):
    grlbn = GRLBN_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                    Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    result = (n41b / 100) * n85h * grlbn
    return result


# def NAWMSL_2_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
#                Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h):
#     return (n41b / 100) * n85h * GRLBN_2_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
#                                            PctGrazing, GRBarnNRate,
#                                            Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
