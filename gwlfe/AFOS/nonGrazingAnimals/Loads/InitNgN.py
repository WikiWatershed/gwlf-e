import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo
from NGLoadN import NGLoadN
from NGLoadN import NGLoadN_2
from gwlfe.GrazingAnimal import GrazingAnimal
from gwlfe.GrazingAnimal import GrazingAnimal_2


def InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = 0
    ng_load_n = NGLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            result += ng_load_n[a]
    return result


def InitNgN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    ng_load_n = NGLoadN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    return np.sum(ng_load_n)
