from InitNgN import InitNgN


def NGAppManN(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = zeros((12,))
    init_ng_n = InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = NGPctManApp[i] * init_ng_n
    return result


def NGAppManN_2(NGPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    return NGPctManApp * InitNgN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
