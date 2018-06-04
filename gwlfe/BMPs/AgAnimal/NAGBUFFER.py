from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum_2
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN import GRLBN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN import GRLBN_2
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN_2
from gwlfe.Outputs.AvAnimalNSum.AvAnimalNSum import AvAnimalNSum
from gwlfe.Outputs.AvAnimalNSum.AvAnimalNSum import AvAnimalNSum_2


def NAGBUFFER(n42, n43, n64, NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
              Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp, PctGrazing, GRBarnNRate,
              AWMSGrPct, GrAWMSCoeffN, PctStreams, NGAppNRate, NGPctSoilIncRate, GRAppNRate, GRPctSoilIncRate,
              GrazingNRate):
    nglbn = AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                     Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    grlbn = GRLBN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    grsn = AvGRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    av_animal_n_sum = AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                                   Prec, DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate,
                                   NGBarnNRate, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing,
                                   GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate)
    if n42 > 0:
        result = (n43 / n42) * n64 * (av_animal_n_sum - (nglbn + grlbn + grsn))
    else:
        result = 0
    return result


def NAGBUFFER_2(n42, n43, n64, NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
              Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp, PctGrazing, GRBarnNRate,
              AWMSGrPct, GrAWMSCoeffN, PctStreams, NGAppNRate, NGPctSoilIncRate, GRAppNRate, GRPctSoilIncRate,
              GrazingNRate):
    if n42 > 0:
        nglbn = AvNGLostBarnNSum_2(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                                 Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
        grlbn = GRLBN_2(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                      Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
        grsn = AvGRStreamN_2(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
        av_animal_n_sum = AvAnimalNSum_2(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                                       Prec, DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate,
                                       NGBarnNRate, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing,
                                       GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate)

        return (n43 / n42) * n64 * (av_animal_n_sum - (nglbn + grlbn + grsn))
    else:
        return 0
