from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLBN import NGLBN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN import GRLBN
from gwlfe.AFOS.GrazingAnimals.Losses.GRSN import GRSN
from gwlfe.Outputs.AvAnimalNSum.AvAnimalNSum import AvAnimalNSum


def NAGBUFFER(n42, n43, n64, NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
              Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp, PctGrazing, GRBarnNRate,
              AWMSGrPct, GrAWMSCoeffN, PctStreams, NGAppNRate, NGPctSoilIncRate, GRAppNRate, GRPctSoilIncRate,
              GrazingNRate):
    nglbn = NGLBN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                  Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    grlbn = GRLBN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    grsn = GRSN(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    av_animal_n_sum = AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate,
                                   Prec, DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate,
                                   NGBarnNRate, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, PctGrazing,
                                   GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate)
    if n42 > 0:
        result = (n43 / n42) * n64 * (av_animal_n_sum - (nglbn + grlbn + grsn))
    else:
        result = 0
    return result


def NAGBUFFER_2():
    pass
