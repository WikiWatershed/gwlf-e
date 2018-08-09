from numpy import maximum
from numpy import minimum
from numpy import reshape
from numpy import resize
from numpy import zeros

from gwlfe.AFOS.GrazingAnimals.Loads.GRInitBarnN import GRInitBarnN
from gwlfe.AFOS.GrazingAnimals.Loads.GRInitBarnN import GRInitBarnN_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_f


def GRLostBarnN(NYrs, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing, GRBarnNRate,
                Prec, DaysMonth, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    result = zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    gr_init_barn_n = GRInitBarnN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                                 PctGrazing)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i]
                            - gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i] * AWMSGrPct * GrAWMSCoeffN
                            + gr_init_barn_n[i] * GRBarnNRate[i] * loss_fact_adj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > gr_init_barn_n[i]:
                result[Y][i] = gr_init_barn_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


@memoize
def GRLostBarnN_f(NYrs, Prec, DaysMonth, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                  PctGrazing, GRBarnNRate, AWMSGrPct, GrAWMSCoeffN, RunContPct, RunConCoeffN):
    loss_fact_adj = LossFactAdj_f(Prec, DaysMonth)
    gr_init_barn_n = GRInitBarnN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)

    years_gr_init_barn_gr_barn_n_rate = resize(gr_init_barn_n * GRBarnNRate,
                                               (NYrs, 12)) * loss_fact_adj  # TODO: what is a better name for this
    result = years_gr_init_barn_gr_barn_n_rate + \
             years_gr_init_barn_gr_barn_n_rate * (AWMSGrPct * GrAWMSCoeffN - RunContPct * RunConCoeffN)
    result = minimum(result, resize(gr_init_barn_n, (NYrs, 12)))
    result = maximum(result, 0)
    return reshape(result, (NYrs, 12))
