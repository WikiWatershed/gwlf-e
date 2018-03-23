import numpy as np
from Timer import time_function
from GRStreamN import GRStreamN
from GrazingN import GrazingN
from LossFactAdj import LossFactAdj


def GRLossN(NYrs, PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, GrazingNRate, Prec,
            DaysMonth):
    result = np.zeros((NYrs, 12))
    gr_stream_n = GRStreamN(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_n = GrazingN(PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = ((grazing_n[i] - gr_stream_n[i]) * GrazingNRate[i] * loss_fact_adj[Y][i])
            if result[Y][i] > (grazing_n[i] - gr_stream_n[i]):
                result[Y][i] = (grazing_n[i] - gr_stream_n[i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLossN_2(NYrs, GrazingN, GRStreamN, GrazingNRate, LossFactAdj):
    result = (np.tile(((GrazingN - GRStreamN) * GrazingNRate), NYrs) * np.ndarray.flatten(LossFactAdj))
    result = np.minimum(result, np.tile((GrazingN - GRStreamN), NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))
