def TotPAEU(NumAnimals, AvgAnimalWt):
    result = 0
    aeu1 = ((NumAnimals[2] / 2) * (AvgAnimalWt[2]) / 1000) + ((NumAnimals[3] / 2) * (AvgAnimalWt[3]) / 1000)
    aeu2 = (NumAnimals[7] * AvgAnimalWt[7]) / 1000
    result += aeu1 + aeu2
    return result


def TotPAEU_f(NumAnimals, AvgAnimalWt):
    return (NumAnimals[2] / 2 * AvgAnimalWt[2] + NumAnimals[3] / 2 * AvgAnimalWt[3] + NumAnimals[7] * AvgAnimalWt[
        7]) / 1000
