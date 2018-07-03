from numpy import where
from numpy import zeros

from gwlfe.Input.Animals.GrazingAnimal import GrazingAnimal
from gwlfe.Input.Animals.GrazingAnimal import GrazingAnimal_f
from gwlfe.enums import YesOrNo


def NGLoadN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((9,))
    grazing_animal = GrazingAnimal(GrazingAnimal_0)
    for a in range(9):
        if grazing_animal[a] is YesOrNo.NO:
            result[a] = (NumAnimals[a] * AvgAnimalWt[a] / 1000) * AnimalDailyN[a] * 365
    return result


def NGLoadN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    grazing_animal = GrazingAnimal_f(GrazingAnimal_0)
    grazing_mask = where(~grazing_animal)
    return (NumAnimals[grazing_mask] * AvgAnimalWt[grazing_mask] / 1000) * AnimalDailyN[grazing_mask] * 365
