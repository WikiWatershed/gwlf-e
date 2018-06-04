import numpy as np

from GRStreamN import GRStreamN
from GRStreamN import GRStreamN_2
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN_2
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj
from gwlfe.MultiUse_Fxns.LossFactAdj import LossFactAdj_2


def GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
            DaysMonth):
    result = np.zeros((NYrs, 12))
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


def GRLossN_2(NYrs, PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
              DaysMonth):
    grazing_n = np.reshape(
        np.repeat(GrazingN_2(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN), repeats=NYrs, axis=0),
        (NYrs, 12))
    gr_stream_n = np.reshape(
        np.repeat(GRStreamN_2(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN),
                  repeats=NYrs, axis=0),
        (NYrs, 12))
    loss_face_adj = LossFactAdj_2(Prec, DaysMonth)
    result = grazing_n - gr_stream_n
    adjusted = np.where(GrazingNRate * loss_face_adj < 1)
    result[adjusted] = result[adjusted] * (GrazingNRate * loss_face_adj)[adjusted]
    return result
