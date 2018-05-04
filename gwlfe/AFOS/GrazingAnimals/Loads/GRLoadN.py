import numpy as np
from gwlfe.Timer import time_function
from gwlfe.enums import YesOrNo
from gwlfe.MultiUse_Fxns.Constants import NAnimals
from gwlfe.GrazingAnimal import GrazingAnimal
from gwlfe.GrazingAnimal import GrazingAnimal_2

def GRLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((NAnimals,))
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            pass
        elif grazing_animal[a] is YesOrNo.YES:
            result[a] = (NumAnimals[a] * AvgAnimalWt[a] / 1000) * AnimalDailyN[a] * 365
    return result

def GRLoadN_2(GrazingAnimal_0,NumAnimals,AvgAnimalWt,AnimalDailyN):
    grazing_animals = GrazingAnimal_2(GrazingAnimal_0)
    return (NumAnimals[grazing_animals] * AvgAnimalWt[grazing_animals] / 1000) * AnimalDailyN[grazing_animals] * 365
