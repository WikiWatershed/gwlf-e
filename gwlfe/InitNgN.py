import numpy as np
from Timer import time_function
from enums import YesOrNo
from NGLoadN import NGLoadN


def InitNgN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = 0
    ng_load_n = NGLoadN(GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for a in range(9):
        if GrazingAnimal[a] is YesOrNo.NO:
            result += ng_load_n[a]
    return result


def InitNgN_2():
    pass
