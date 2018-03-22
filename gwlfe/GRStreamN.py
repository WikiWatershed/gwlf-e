import numpy as np
from Timer import time_function
from GrazingN import GrazingN

def GRStreamN(PctStreams,PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = np.zeros((12,))
    grazing_n = GrazingN(PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for i in range(12):
        result[i] = PctStreams[i] * grazing_n[i]
    return result


def GRStreamN_2():
    pass
