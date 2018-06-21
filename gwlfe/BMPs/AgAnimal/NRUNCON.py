from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN import GRLBN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN import GRLBN_2
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnN import AvNGLostBarnNSum_2


def NRUNCON(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
            Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate, AWMSNgPct,
            NgAWMSCoeffN, n41f, n85l):
    grlbn = GRLBN(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                  Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    nglbn = AvNGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                             Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    result = (n41f / 100) * n85l * (grlbn + nglbn)
    return result


def NRUNCON_2(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
              Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate, AWMSNgPct,
              NgAWMSCoeffN, n41f, n85l):
    grlbn = GRLBN_2(NYrs, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                    Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    nglbn = AvNGLostBarnNSum_2(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                               Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    return (n41f / 100) * n85l * (grlbn + nglbn)
