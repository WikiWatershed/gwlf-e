import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo
from NGLoadN import NGLoadN
from gwlfe.GrazingAnimal import GrazingAnimal


def InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = 0
    ng_load_n = NGLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            result += ng_load_n[a]
    return result


def InitNgN_2():
    pass
