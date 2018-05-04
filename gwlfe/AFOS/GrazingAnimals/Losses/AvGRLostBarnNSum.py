from gwlfe.AFOS.GrazingAnimals.Losses.AvGRLostBarnN import AvGRLostBarnN


def AvGRLostBarnNSum(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                     Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    av_gr_lost_barn_n = AvGRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                      PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct,
                                      RunConCoeffN)
    result = sum(av_gr_lost_barn_n)
    return result


def AvGRLostBarnNSum_2():
    pass
