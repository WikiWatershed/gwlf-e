import numpy as np
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostManN import NGLostManN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostManN import GRLostManN
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import NGLostBarnN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostBarnN import GRLostBarnN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLossN import GRLossN
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import GRStreamN

def AnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,GrazingNRate):
    result = np.zeros((NYrs, 12))
    ng_lost_man_n = NGLostManN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                               Prec, DaysMonth,
                               NGPctSoilIncRate)
    gr_lost_man_n = GRLostManN(NYrs, GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate,
                               Prec, DaysMonth, GRPctSoilIncRate)
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_loss_n = GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
            DaysMonth)
    gr_stream_n = GRStreamN(PctStreams,PctGrazing,GrazingAnimal_0,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (ng_lost_man_n[Y][i]
                            + gr_lost_man_n[Y][i]
                            + ng_lost_barn_n[Y][i]
                            + gr_lost_barn_n[Y][i]
                            + gr_loss_n[Y][i]
                            + gr_stream_n[i])
    return result


def AnimalN_2():
    pass
