from .AvAnimalNSum import AvAnimalNSum
from gwlfe.BMPs.AgAnimal.NAGBUFFER import NAGBUFFER
from gwlfe.BMPs.AgAnimal.NAGBUFFER import NAGBUFFER_f
from gwlfe.BMPs.AgAnimal.NAWMSL import NAWMSL
from gwlfe.BMPs.AgAnimal.NAWMSL import NAWMSL_f
from gwlfe.BMPs.AgAnimal.NAWMSP import NAWMSP
from gwlfe.BMPs.AgAnimal.NAWMSP import NAWMSP_f
from gwlfe.BMPs.AgAnimal.NFENCING import NFENCING
from gwlfe.BMPs.AgAnimal.NFENCING import NFENCING_f
from gwlfe.BMPs.AgAnimal.NRUNCON import NRUNCON
from gwlfe.BMPs.AgAnimal.NRUNCON import NRUNCON_f
from gwlfe.Output.AvAnimalNSum.AvAnimalNSum import AvAnimalNSum_f


def N7b(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
        GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate,
        Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct,
        NGBarnNRate, NgAWMSCoeffN, n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64):
    av_animal_n_sum = AvAnimalNSum(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                   NGAppNRate,
                                   Prec, DaysMonth,
                                   NGPctSoilIncRate, GRPctManApp, GRAppNRate, GRPctSoilIncRate, NGBarnNRate, AWMSNgPct,
                                   NgAWMSCoeffN,
                                   RunContPct, RunConCoeffN, PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN,
                                   PctStreams, GrazingNRate)
    nawmsl = NAWMSL(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                    Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h)
    nawmsp = NAWMSP(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                    Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j)
    nruncon = NRUNCON(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                      GRBarnNRate,
                      Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate,
                      AWMSNgPct, NgAWMSCoeffN, n41f, n85l)
    nfencing = NFENCING(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, n42, n45, n69)
    nagbuffer = NAGBUFFER(n42, n43, n64, NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                          NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, GRPctManApp,
                          PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, NGAppNRate, NGPctSoilIncRate,
                          GRAppNRate, GRPctSoilIncRate, GrazingNRate)
    result = av_animal_n_sum - (nawmsl + nawmsp + nruncon + nfencing + nagbuffer)
    return result


def N7b_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGAppNRate, NGPctSoilIncRate, GRAppNRate,
          GRPctSoilIncRate, GrazingNRate, GRPctManApp, PctGrazing, GRBarnNRate,
          Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h, NGPctManApp, AWMSNgPct,
          NGBarnNRate, NgAWMSCoeffN, n41d, n85j, n41f, n85l, PctStreams, n42, n45, n69, n43, n64):
    av_animal_n_sum = AvAnimalNSum_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                                     NGAppNRate, Prec, DaysMonth, NGPctSoilIncRate, GRPctManApp, GRAppNRate,
                                     GRPctSoilIncRate, NGBarnNRate, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN,
                                     PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, GrazingNRate)
    nawmsl = NAWMSL_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                      GRBarnNRate,
                      Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, n41b, n85h)
    nawmsp = NAWMSP_f(NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate,
                      Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN, n41d, n85j)
    nruncon = NRUNCON_f(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing,
                        GRBarnNRate,
                        Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN, NGPctManApp, NGBarnNRate,
                        AWMSNgPct, NgAWMSCoeffN, n41f, n85l)
    nfencing = NFENCING_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, n42, n45, n69)
    nagbuffer = NAGBUFFER_f(n42, n43, n64, NYrs, NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN,
                            NGBarnNRate, Prec, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN,
                            GRPctManApp,
                            PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, PctStreams, NGAppNRate, NGPctSoilIncRate,
                            GRAppNRate, GRPctSoilIncRate, GrazingNRate)
    result = av_animal_n_sum - (nawmsl + nawmsp + nruncon + nfencing + nagbuffer)
    return result
