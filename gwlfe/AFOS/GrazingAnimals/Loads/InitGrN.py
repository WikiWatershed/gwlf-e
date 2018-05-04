import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo
from GRLoadN import GRLoadN

@time_function
def InitGrN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = 0
    gr_load_n = GRLoadN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for a in range(9):
        if GrazingAnimal[a] is YesOrNo.NO:
            pass
        elif GrazingAnimal[a] is YesOrNo.YES:
            result += gr_load_n[a]
    return result

@time_function
def InitGrN_2(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    gr_load_n = GRLoadN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    return np.sum(gr_load_n[gr_load_n == YesOrNo.Yes])
