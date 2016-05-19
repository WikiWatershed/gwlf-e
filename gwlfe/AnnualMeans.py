# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from AnnualMeans.bas
"""

import logging


log = logging.getLogger(__name__)


def CalculateAnnualMeanLoads(z, Y):
    log.debug('CalculateAnnualMeanLoads')

    # UPDATE SEPTIC SYSTEM AVERAGES
    z.AvSeptNitr += z.SepticNitr[Y] / z.NYrs
    z.AvSeptPhos += z.SepticPhos[Y] / z.NYrs

    # Add the Stream Bank Erosion to sediment yield
    for i in range(12):
        z.SedYield[Y][i] += z.StreamBankEros[Y][i] / 1000

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # CALCULATE ANNUAL MEANS FOR STREAM BANK AND TILE DRAINAGE VALUES
    for i in range(12):
        z.AvStreamBankEros[i] += z.StreamBankEros[Y][i] / z.NYrs
        z.AvStreamBankN[i] += z.StreamBankN[Y][i] / z.NYrs
        z.AvStreamBankP[i] += z.StreamBankP[Y][i] / z.NYrs

        # If the Monthly Erosion is < the Sediment Yield
        # recalculate using Sediment Delivery Ratio
        if z.SedDelivRatio > 0 and z.Erosion[Y][i] < z.SedYield[Y][i]:
            z.Erosion[Y][i] = z.SedYield[Y][i] / z.SedDelivRatio

        z.AvPtSrcFlow[i] += z.PtSrcFlow[Y][i] / z.NYrs
        z.AvTileDrain[i] += z.TileDrain[Y][i] / z.NYrs
        z.AvWithdrawal[i] += z.Withdrawal[Y][i] / z.NYrs
        z.AvTileDrainN[i] += z.TileDrainN[Y][i] / z.NYrs
        z.AvTileDrainP[i] += z.TileDrainP[Y][i] / z.NYrs
        z.AvTileDrainSed[i] += z.TileDrainSed[Y][i] / z.NYrs

    # Recalculate the total annual erosion
    z.ErosSum = 0
    for i in range(12):
        z.ErosSum += z.Erosion[Y][i]

    # COMPUTE ANNUAL MEANS
    for i in range(12):
        z.AvPrecipitation[i] += z.Precipitation[Y][i] / z.NYrs
        z.AvEvapoTrans[i] += z.Evapotrans[Y][i] / z.NYrs
        z.AvGroundWater[i] += z.GroundWatLE[Y][i] / z.NYrs

        if z.AvGroundWater[i] < 0:
            z.AvGroundWater[i] = 0

        z.AvRunoff[i] += z.Runoff[Y][i] / z.NYrs
        z.AvErosion[i] += z.Erosion[Y][i] / z.NYrs
        z.AvSedYield[i] += z.SedYield[Y][i] / z.NYrs

        z.AvDisNitr[i] += z.DisNitr[Y][i] / z.NYrs
        z.AvTotNitr[i] += z.TotNitr[Y][i] / z.NYrs
        z.AvDisPhos[i] += z.DisPhos[Y][i] / z.NYrs
        z.AvTotPhos[i] += z.TotPhos[Y][i] / z.NYrs
        z.AvGroundNitr[i] += z.GroundNitr[Y][i] / z.NYrs
        z.AvGroundPhos[i] += z.GroundPhos[Y][i] / z.NYrs
        z.AvAnimalN[i] += z.AnimalN[Y][i] / z.NYrs
        z.AvAnimalP[i] += z.AnimalP[Y][i] / z.NYrs

        z.AvGRLostBarnN[i] += z.GRLostBarnN[Y][i] / z.NYrs
        z.AvGRLostBarnP[i] += z.GRLostBarnP[Y][i] / z.NYrs
        z.AvGRLostBarnFC[i] += z.GRLostBarnFC[Y][i] / z.NYrs

        z.AvNGLostBarnN[i] += z.NGLostBarnN[Y][i] / z.NYrs
        z.AvNGLostBarnP[i] += z.NGLostBarnP[Y][i] / z.NYrs
        z.AvNGLostBarnFC[i] += z.NGLostBarnFC[Y][i] / z.NYrs

        z.AvNGLostManP[i] += z.NGLostManP[Y][i] / z.NYrs

        # Average pathogen totals
        z.AvAnimalFC[i] += z.AnimalFC[Y][i] / z.NYrs
        z.AvWWOrgs[i] += z.WWOrgs[Y][i] / z.NYrs
        z.AvSSOrgs[i] += z.SSOrgs[Y][i] / z.NYrs
        z.AvUrbOrgs[i] += z.UrbOrgs[Y][i] / z.NYrs
        z.AvWildOrgs[i] += z.WildOrgs[Y][i] / z.NYrs
        z.AvTotalOrgs[i] += z.TotalOrgs[Y][i] / z.NYrs

    # Average loads for each landuse
    for l in range(z.NRur):
        z.AvLuRunoff[l] += z.LuRunoff[Y][l] / z.NYrs
        z.AvLuErosion[l] += z.LuErosion[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += z.LuTotNitr[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += z.LuTotPhos[Y][l] / z.NYrs

    for l in range(z.NRur, z.NLU):
        z.AvLuRunoff[l] += z.LuRunoff[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += z.LuTotNitr[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += z.LuTotPhos[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs

    z.AvStreamBankErosSum = sum(z.AvStreamBankEros)
    z.AvStreamBankNSum = sum(z.AvStreamBankN)
    z.AvStreamBankPSum = sum(z.AvStreamBankP)
    z.AvPtSrcFlowSum = sum(z.AvPtSrcFlow)
    z.AvTileDrainSum = sum(z.AvTileDrain)
    z.AvWithdrawalSum = sum(z.AvWithdrawal)
    z.AvTileDrainNSum = sum(z.AvTileDrainN)
    z.AvTileDrainPSum = sum(z.AvTileDrainP)
    z.AvTileDrainSedSum = sum(z.AvTileDrainSed)
    z.AvPrecipitationSum = sum(z.AvPrecipitation)
    z.AvEvapoTransSum = sum(z.AvEvapoTrans)
    z.AvGroundWaterSum = sum(z.AvGroundWater)
    z.AvRunoffSum = sum(z.AvRunoff)
    z.AvErosionSum = sum(z.AvErosion)
    z.AvSedYieldSum = sum(z.AvSedYield)
    z.AvDisNitrSum = sum(z.AvDisNitr)
    z.AvTotNitrSum = sum(z.AvTotNitr)
    z.AvDisPhosSum = sum(z.AvDisPhos)
    z.AvTotPhosSum = sum(z.AvTotPhos)
    z.AvGroundNitrSum = sum(z.AvGroundNitr)
    z.AvGroundPhosSum = sum(z.AvGroundPhos)
    z.AvAnimalNSum = sum(z.AvAnimalN)
    z.AvAnimalPSum = sum(z.AvAnimalP)
    z.AvGRLostBarnNSum = sum(z.AvGRLostBarnN)
    z.AvGRLostBarnPSum = sum(z.AvGRLostBarnP)
    z.AvGRLostBarnFCSum = sum(z.AvGRLostBarnFC)
    z.AvNGLostBarnNSum = sum(z.AvNGLostBarnN)
    z.AvNGLostBarnPSum = sum(z.AvNGLostBarnP)
    z.AvNGLostBarnFCSum = sum(z.AvNGLostBarnFC)
    z.AvNGLostManPSum = sum(z.AvNGLostManP)
    z.AvAnimalFCSum = sum(z.AvAnimalFC)
    z.AvWWOrgsSum = sum(z.AvWWOrgs)
    z.AvSSOrgsSum = sum(z.AvSSOrgs)
    z.AvUrbOrgsSum = sum(z.AvUrbOrgs)
    z.AvWildOrgsSum = sum(z.AvWildOrgs)
    z.AvTotalOrgsSum = sum(z.AvTotalOrgs)
    z.AvLuRunoffSum = sum(z.AvLuRunoff)
    z.AvLuErosionSum = sum(z.AvLuErosion)
    z.AvLuSedYieldSum = sum(z.AvLuSedYield)
    z.AvLuDisNitrSum = sum(z.AvLuDisNitr)
    z.AvLuTotNitrSum = sum(z.AvLuTotNitr)
    z.AvLuDisPhosSum = sum(z.AvLuDisPhos)
    z.AvLuTotPhosSum = sum(z.AvLuTotPhos)
