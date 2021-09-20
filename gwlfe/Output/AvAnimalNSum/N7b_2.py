from numpy import zeros

from .N7b import N7b
from gwlfe.AFOS.GrazingAnimals.Losses.GRLBN_2 import GRLBN_2
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN
from gwlfe.AFOS.nonGrazingAnimals.Losses.NGLostBarnNSum import NGLostBarnNSum
from gwlfe.BMPs.AgAnimal.NAWMSL_2 import NAWMSL_2
from gwlfe.BMPs.AgAnimal.NAWMSP_2 import NAWMSP_2
from gwlfe.BMPs.AgAnimal.NFENCING import NFENCING
from gwlfe.BMPs.AgAnimal.NRUNCON_2 import NRUNCON_2


def N7b_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, Prec, DaysMonth,
          NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN,
          RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate, n41b,
          n85h, n41d, n85j, n41f, n85l, n42, n45, n69, n43, n64):
    result = zeros((NYrs))
    n7b = N7b(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
              GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate, Prec, DaysMonth, AWMSGrPct,
              GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct, NGBarnNRate, NgAWMSCoeffN,
              n41d,
              n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64)
    nawmsl = NAWMSL_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                      GRBarnNRate,
                      Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h)
    nawmsp = NAWMSP_2(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                      Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j)
    nruncon = NRUNCON_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                        GRBarnNRate,
                        Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate,
                        AWMSNgPct,
                        NgAWMSCoeffN, n41f, n85l)
    nfencing = NFENCING(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, n42, n45, n69)
    nglbn = NGLostBarnNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                           Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN)
    grlbn = GRLBN_2(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                    Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN)
    grsn = AvGRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    n7b_carryover = n7b
    for y in range(NYrs):
        nagbuffer_2 = (n43 / n42) * n64 * (n7b_carryover - (nglbn[y] + grlbn[y] + grsn))
        result[y] = n7b_carryover - (nawmsl[y] + nawmsp[y] + nruncon[y] + nfencing + nagbuffer_2)
        n7b_carryover = result[y]
    return result


def N7b_2_f():
    pass
