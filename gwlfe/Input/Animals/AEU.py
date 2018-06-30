from gwlfe.Input.Animals.TotLAEU import TotLAEU
from gwlfe.Input.LandUse.AreaTotal import AreaTotal
from gwlfe.Input.LandUse.AreaTotal import AreaTotal_f


def AEU(NumAnimals, AvgAnimalWt, NRur, NUrb, Area):
    # Recalculate AEU using the TotAEU from the animal file and the total area of the basin in Acres
    result = 0
    areatotal = AreaTotal(NRur, NUrb, Area)
    totLAEU = TotLAEU(NumAnimals, AvgAnimalWt)
    if totLAEU > 0 and areatotal > 0:
        result += totLAEU / (areatotal * 2.471)
    else:
        result = 0
    return result


def AEU_f(NumAnimals, AvgAnimalWt, Area):
    areatotal = AreaTotal_f(Area)
    totLAEU = TotLAEU(NumAnimals, AvgAnimalWt)
    if totLAEU > 0 and areatotal > 0:
        return totLAEU / (areatotal * 2.471)
    else:
        return 0
