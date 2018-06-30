from gwlfe.Input.Animals.AEU import AEU
from gwlfe.Input.Animals.AEU import AEU_f
from gwlfe.Input.LandUse.Urb.PcntUrbanArea import PcntUrbanArea
from gwlfe.Input.LandUse.Urb.PcntUrbanArea import PcntUrbanArea_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.AvCN import AvCN
from gwlfe.MultiUse_Fxns.Runoff.AvCN import AvCN_f


@memoize
def SedAFactor(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF, AvSlope,
               SedAAdjust):
    pcnturbanarea = PcntUrbanArea(NRur, NUrb, Area)
    aeu = AEU(NumAnimals, AvgAnimalWt, NRur, NUrb, Area)
    avcn = AvCN(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area)
    # Recalculate Sed A Factor using updated AEU value based on animal data
    result = ((0.00467 * pcnturbanarea) +
              (0.000863 * aeu) +
              (0.000001 * avcn) +
              (0.000425 * AvKF) +
              (0.000001 * AvSlope) - 0.000036) * SedAAdjust

    if result < 0.00001:
        result = 0.00001
    return result


def SedAFactor_f(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF, AvSlope,
                 SedAAdjust):
    pcnturbanarea = PcntUrbanArea_f(NRur, NUrb, Area)
    aeu = AEU_f(NumAnimals, AvgAnimalWt, Area)
    avcn = AvCN_f(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area)
    # Recalculate Sed A Factor using updated AEU value based on animal data
    result = ((0.00467 * pcnturbanarea) +
              (0.000863 * aeu) +
              (0.000001 * avcn) +
              (0.000425 * AvKF) +
              (0.000001 * AvSlope) - 0.000036) * SedAAdjust

    if result < 0.00001:
        result = 0.00001
    return result
