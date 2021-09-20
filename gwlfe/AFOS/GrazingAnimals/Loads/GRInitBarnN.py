from numpy import zeros

from .GRAppManN import GRAppManN
from .GRAppManN import GRAppManN_f
from gwlfe.AFOS.GrazingAnimals.Loads.GRAccManAppN import GRAccManAppN
from gwlfe.AFOS.GrazingAnimals.Loads.GRAccManAppN import GRAccManAppN_f


def GRInitBarnN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = zeros((12,))
    gr_acc_man_app_n = GRAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing)
    gr_app_man_n = GRAppManN(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = gr_acc_man_app_n[i] - gr_app_man_n[i]
    return result


def GRInitBarnN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    return GRAccManAppN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp,
                          PctGrazing) - GRAppManN_f(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
