from numpy import maximum
from numpy import zeros

from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN_f
from gwlfe.AFOS.GrazingAnimals.Loads.InitGrN import InitGrN
from gwlfe.AFOS.GrazingAnimals.Loads.InitGrN import InitGrN_f
from gwlfe.Memoization import memoize


def GRAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = zeros((12,))
    grazing_n = GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = (result[i] + (init_gr_n / 12) - (GRPctManApp[i] * init_gr_n) - grazing_n[i])
        if result[i] < 0:
            result[i] = 0
    return result


@memoize
def GRAccManAppN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    init_gr_n = InitGrN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    grazing_n = GrazingN_f(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    return maximum(((1.0 / 12) - GRPctManApp) * init_gr_n - grazing_n, 0)
