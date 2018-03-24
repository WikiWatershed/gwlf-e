import numpy as np
from Timer import time_function
from GRSN import GRSN

def NFENCING(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN,n42,n45,n69):
    grsn = GRSN(PctStreams, PctGrazing, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    if n42 > 0:# based on the code, n42 is always > 0 (may not need to check
        result = (n45 / n42) * n69 * grsn
    else:
        result = 0 #TODO: the code does not have this fall back, would have error if n42 <= 0
    return result


def NFENCING_2():
    pass
