from numpy import zeros

from .InitGrN import InitGrN
from .InitGrN import InitGrN_f
from gwlfe.Memoization import memoize


def GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = PctGrazing[i] * (init_gr_n / 12)
    return result


@memoize
def GrazingN_f(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return (PctGrazing * (InitGrN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN) / 12))[None, :]
