import numpy as np
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN

def GRStreamN(PctStreams,PctGrazing,GrazingAnimal_0,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = np.zeros((12,))
    grazing_n = GrazingN(PctGrazing,GrazingAnimal_0,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for i in range(12):
        result[i] = PctStreams[i] * grazing_n[i]
    return result


def GRStreamN_2():
    pass

def AvGRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = 0
    gr_stream_n = GRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for i in range(12):
        result += gr_stream_n[i]
    return result


def AvGRStreamN_2():
    pass
