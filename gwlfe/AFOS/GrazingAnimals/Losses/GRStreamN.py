from numpy import sum
from numpy import zeros

from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN_f
from gwlfe.Memoization import memoize


def GRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    grazing_n = GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = PctStreams[i] * grazing_n[i]
    return result


@memoize
def GRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return PctStreams * GrazingN_f(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)


@memoize
def AvGRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = 0
    gr_stream_n = GRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result += gr_stream_n[i]
    return result


@memoize
def AvGRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return sum(GRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN))
