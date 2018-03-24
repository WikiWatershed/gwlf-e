import numpy as np
from Timer import time_function
from NGLostManN import NGLostManN
from GRLostManN import GRLostManN
from NGLostBarnN import NGLostBarnN
from GRLostBarnN import GRLostBarnN
from GRLossN import GRLossN
from GRStreamN import GRStreamN

def AnimalN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams,GrazingNRate):
    result = np.zeros((NYrs, 12))
    ng_lost_man_n = NGLostManN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                               Prec, DaysMonth,
                               NGPctSoilIncRate)
    gr_lost_man_n = GRLostManN(NYrs, GRPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate,
                               Prec, DaysMonth, GRPctSoilIncRate)
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_loss_n = GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
            DaysMonth)
    gr_stream_n = GRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
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
