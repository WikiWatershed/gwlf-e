from numpy import zeros

from .InitNgN import InitNgN
from .InitNgN import InitNgN_f
from gwlfe.Memoization import memoize


def NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = NGPctManApp[i] * init_ng_n
    return result


@memoize
def NGAppManN_f(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return NGPctManApp * InitNgN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
