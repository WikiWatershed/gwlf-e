from numpy import repeat
from numpy import reshape
from numpy import zeros

from gwlfe.AFOS.GrazingAnimals.Losses.GRLossN import GRLossN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLossN import GRLossN_f
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostBarnN import GRLostBarnN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostBarnN import GRLostBarnN_f
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostManN import GRLostManN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostManN import GRLostManN_f
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import GRStreamN
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import GRStreamN_f
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import NGLostBarnN
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import NGLostBarnN_f
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostManN import NGLostManN
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostManN import NGLostManN_f
from gwlfe.Memoization import memoize


def AnimalN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
            NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
            RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    result = zeros((NYrs, 12))
    ng_lost_man_n = NGLostManN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                               Prec, DaysMonth,
                               NGPctSoilIncRate)
    gr_lost_man_n = GRLostManN(NYrs, GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate,
                               Prec, DaysMonth, GRPctSoilIncRate)
    ng_lost_barn_n = NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_lost_barn_n = GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                                 GRBarnNRate, Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_loss_n = GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                        GrazingNRate, Prec,
                        DaysMonth)
    gr_stream_n = GRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (ng_lost_man_n[Y][i]
                            + gr_lost_man_n[Y][i]
                            + ng_lost_barn_n[Y][i]
                            + gr_lost_barn_n[Y][i]
                            + gr_loss_n[Y][i]
                            + gr_stream_n[i])
    return result


@memoize
def AnimalN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
              NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
              RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate):
    ng_lost_man_n = NGLostManN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                                 Prec, DaysMonth, NGPctSoilIncRate)
    gr_lost_man_n = GRLostManN_f(NYrs, GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRAppNRate,
                                 Prec, DaysMonth, GRPctSoilIncRate)
    ng_lost_barn_n = NGLostBarnN_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                   NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    gr_lost_barn_n = GRLostBarnN_f(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                   GRPctManApp, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct,
                                   RunConCoeffN)
    gr_loss_n = GRLossN_f(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                          GrazingNRate, Prec,
                          DaysMonth)
    gr_stream_n = reshape(
        repeat(GRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN),
               repeats=NYrs, axis=0), (NYrs, 12))
    return ng_lost_man_n + gr_lost_man_n + ng_lost_barn_n + gr_lost_barn_n + gr_loss_n + gr_stream_n
