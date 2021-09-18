from numpy import repeat
from numpy import reshape
from numpy import where
from numpy import zeros

from .GRStreamN import GRStreamN
from .GRStreamN import GRStreamN_f
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_f


def GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
            DaysMonth):
    result = zeros((NYrs, 12))
    gr_stream_n = GRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_n = GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = ((grazing_n[i] - gr_stream_n[i]) * GrazingNRate[i] * loss_fact_adj[Y][i])
            if result[Y][i] > (grazing_n[i] - gr_stream_n[i]):
                result[Y][i] = (grazing_n[i] - gr_stream_n[i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


@memoize
def GRLossN_f(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
              DaysMonth):
    grazing_n = reshape(
        repeat(GrazingN_f(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN), repeats=NYrs, axis=0),
        (NYrs, 12))
    gr_stream_n = reshape(
        repeat(GRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN),
               repeats=NYrs, axis=0),
        (NYrs, 12))
    loss_face_adj = LossFactAdj_f(Prec, DaysMonth)
    result = grazing_n - gr_stream_n
    adjusted = where(GrazingNRate * loss_face_adj < 1)
    result[adjusted] = result[adjusted] * (GrazingNRate * loss_face_adj)[adjusted]
    return result
