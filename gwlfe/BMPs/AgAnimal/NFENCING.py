from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN
from gwlfe.AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN_f


def NFENCING(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, n42, n45, n69):
    grsn = AvGRStreamN(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    if n42 > 0:  # based on the code, n42 is always > 0 (may not need to check
        result = (n45 / n42) * n69 * grsn
    else:
        result = 0  # TODO: the code does not have this fall back, would have error if n42 <= 0
    return result


def NFENCING_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, n42, n45, n69):
    if n42 > 0:  # based on the code, n42 is always > 0 (may not need to check
        grsn = AvGRStreamN_f(PctStreams, PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
        return (n45 / n42) * n69 * grsn
    else:
        return 0  # TODO: the code does not have this fall back, would have error if n42 <= 0
