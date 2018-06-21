from InitGrN import InitGrN
from InitGrN import InitGrN_2
from numpy import zeros


def GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = PctGrazing[i] * (init_gr_n / 12)
    return result


def GrazingN_2(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return (PctGrazing * (InitGrN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN) / 12))[None,:]
