import numpy as np
from gwlfe.Timer import time_function
from GRStreamN import AvGRStreamN

def GRSN(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    av_gr_stream_n = AvGRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    return av_gr_stream_n


def GRSN_2():
    pass
