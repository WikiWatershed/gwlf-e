import numpy as np
from Timer import time_function
from enums import YesOrNo
from GRLoadN import GRLoadN

def InitGrN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = 0
    gr_load_n = GRLoadN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for a in range(9):
        if GrazingAnimal[a] is YesOrNo.NO:
            pass
        elif GrazingAnimal[a] is YesOrNo.YES:
            result += gr_load_n[a]
    return result


def InitGrN_2():
    pass
