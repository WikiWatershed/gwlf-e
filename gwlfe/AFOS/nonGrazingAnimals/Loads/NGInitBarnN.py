from numpy import maximum
from numpy import zeros

from .NGAccManAppN import NGAccManAppN
from .NGAccManAppN import NGAccManAppN_f
from .NGAppManN import NGAppManN
from .NGAppManN import NGAppManN_f
from gwlfe.Memoization import memoize


def NGInitBarnN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    ng_app_man_n = NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    ng_acc_man_app_n = NGAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp)
    for i in range(12):
        result[i] = ng_acc_man_app_n[i] - ng_app_man_n[i]
        if result[i] < 0:
            result[i] = 0
    return result


@memoize
def NGInitBarnN_f(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    ng_app_man_n = NGAppManN_f(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    ng_acc_man_app_n = NGAccManAppN_f(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, NGPctManApp)
    return maximum(ng_acc_man_app_n - ng_app_man_n, 0)[None, :]
