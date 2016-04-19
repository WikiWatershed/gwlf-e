# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from StreamBank.bas
"""

import logging


log = logging.getLogger(__name__)


def CalculateStreamBankEros(z, Y):
    log.debug('CalculateStreamBankEros')

    # CALCULATE THE STREAM BANK SEDIMENT AND N AND P
    for i in range(12):
        # CALCULATE ER FACTOR FOR STREAMBANK EROSION
        z.LE[Y, i] = z.SedAFactor * (z.StreamFlowVolAdj * (z.StreamFlowVol[Y, i] ** -1.6))

        z.StreamBankEros[Y, i] = z.LE[Y, i] * z.StreamLength * 1500 * 1.5

        # CALCULATE STREAM ABANK N AND P
        z.StreamBankN[Y, i] = z.StreamBankEros[Y, i] * (z.SedNitr / 1000000) * z.BankNFrac
        z.StreamBankP[Y, i] = z.StreamBankEros[Y, i] * (z.SedPhos / 1000000) * z.BankPFrac

        # CALCULATIONS FOR STREAM BANK STABILIZATION AND FENCING
        z.SURBBANK = 0
        z.NURBBANK = 0
        z.PURBBANK = 0
        z.FCURBBANK = 0

        if z.n42b > 0:
            z.SEDSTAB = (z.n46c / z.n42b) * z.StreamBankEros[Y, i] * z.n85d
            z.SURBBANK = (z.UrbBankStab / z.n42b) * z.StreamBankEros[Y, i] * z.n85d

        if z.n42 > 0:
            z.SEDFEN = (z.n45 / z.n42) * z.StreamBankEros[Y, i] * z.AGSTRM * z.n85

        z.StreamBankEros[Y, i] = z.StreamBankEros[Y, i] - (z.SEDSTAB + z.SEDFEN + z.SURBBANK)
        if z.StreamBankEros[Y, i] < 0:
            z.StreamBankEros[Y, i] = 0

        if z.n42b > 0:
            z.NSTAB = (z.n46c / z.n42b) * z.StreamBankN[Y, i] * z.n69c
            z.NURBBANK = (z.UrbBankStab / z.n42b) * z.StreamBankN[Y, i] * z.n69c

        if z.n42 > 0:
            z.NFEN = (z.n45 / z.n42) * z.StreamBankN[Y, i] * z.AGSTRM * z.n69

        z.StreamBankN[Y, i] = z.StreamBankN[Y, i] - (z.NSTAB + z.NFEN + z.NURBBANK)
        if z.StreamBankN[Y, i] < 0:
            z.StreamBankN[Y, i] = 0

        if z.n42b > 0:
            z.PSTAB = (z.n46c / z.n42b) * z.StreamBankP[Y, i] * z.n77c
            z.PURBBANK = (z.UrbBankStab / z.n42b) * z.StreamBankP[Y, i] * z.n77c

        if z.n42 > 0:
            z.PFEN = (z.n45 / z.n42) * z.StreamBankP[Y, i] * z.AGSTRM * z.n77

        z.StreamBankP[Y, i] = z.StreamBankP[Y, i] - (z.PSTAB + z.PFEN + z.PURBBANK)
        if z.StreamBankP[Y, i] < 0:
            z.StreamBankP[Y, i] = 0

        # CALCULATE ANNUAL STREAMBANK N AND P AND SEDIMENT
        z.StreamBankN[Y, 0] = z.StreamBankN[Y, 0] + z.StreamBankN[Y, i]
        z.StreamBankP[Y, 0] = z.StreamBankP[Y, 0] + z.StreamBankP[Y, i]
        z.StreamBankEros[Y, 0] = z.StreamBankEros[Y, 0] + z.StreamBankEros[Y, i]

        # GROUNDWATER N LOADS ARE REDUCED BASED ON SPECIFIC BMPS
        z.GWNRF = 0
        z.CHNGN1 = 0
        z.CHNGN2 = 0
        z.CHNGN3 = 0
        z.CHNGN4 = 0
        z.CHNGN5 = 0
        z.CHNGNTOT = 0
        z.PCTN1 = 0
        z.PCTN2 = 0
        z.PCTN3 = 0
        z.PCTN4 = 0
        z.PCBMPAC = 0
        z.HPBMPAC = 0
        z.BMPACRES = 0
        z.PCTAG = 0
        z.RCNMAC = 0
        z.HPNMAC = 0

        z.CHNGN1 = z.n25 / 100
        z.CHNGN2 = z.n26 / 100
        z.CHNGN3 = z.n27 / 100
        z.CHNGN4 = z.n27b / 100
        z.CHNGN5 = z.n28 / 100
        z.CHNGNTOT = z.CHNGN1 + z.CHNGN2 + z.CHNGN3 + z.CHNGN4 + z.CHNGN5

        if z.AreaTotal > 0 and z.n23 > 0 and z.n42 > 0 and z.n42b > 0:
            z.PCTAG = (z.n23 + z.n24) / z.AreaTotal
            z.GroundNitr[Y, i] -= z.GroundNitr[Y, i] * ((z.n28b / 100) * z.n23) / z.n23 * z.PCTAG * z.n70
            z.GroundNitr[Y, i] -= z.GroundNitr[Y, i] * (z.n43 / z.n42) * (z.n42 / z.n42b) * z.PCTAG * z.n64
            z.GroundNitr[Y, i] -= (z.GroundNitr[Y, i] * ((((z.n29 / 100) * z.n23) + ((z.n37 / 100) * z.n24)) / (z.n23 + z.n24))) * z.PCTAG * z.n68

        # Groundwater P loads are reduced based on extent of nutrient management BMP
        z.RCNMAC = (z.n28b / 100) * z.n23
        z.HPNMAC = (z.n35b / 100) * z.n24

        z.GroundPhos[Y, i] -= (((z.RCNMAC + z.HPNMAC) / z.AreaTotal) * z.GroundPhos[Y, i] * z.n78)

        z.GroundNitr[Y, 0] += z.GroundNitr[Y, i]
        z.GroundPhos[Y, 0] += z.GroundPhos[Y, i]

        z.TileDrain[Y, 0] += z.TileDrain[Y, i]
        z.TileDrainN[Y, 0] += z.TileDrainN[Y, i]
        z.TileDrainP[Y, 0] += z.TileDrainP[Y, i]
        z.TileDrainSed[Y, 0] += z.TileDrainSed[Y, i]
        z.AnimalN[Y, 0] += z.AnimalN[Y, i]
        z.AnimalP[Y, 0] += z.AnimalP[Y, i]

        z.GRLostBarnN[Y, 0] += z.GRLostBarnN[Y, i]
        z.GRLostBarnP[Y, 0] += z.GRLostBarnP[Y, i]
        z.GRLostBarnFC[Y, 0] += z.GRLostBarnFC[Y, i]
        z.NGLostBarnN[Y, 0] += z.NGLostBarnN[Y, i]
        z.NGLostBarnP[Y, 0] += z.NGLostBarnP[Y, i]
        z.NGLostBarnFC[Y, 0] += z.NGLostBarnFC[Y, i]
        z.NGLostManP[Y, 0] += z.NGLostManP[Y, i]

        z.TotNitr[Y, i] += z.StreamBankN[Y, i] + z.TileDrainN[Y, i] + z.AnimalN[Y, i]
        z.TotPhos[Y, i] += z.StreamBankP[Y, i] + z.TileDrainP[Y, i] + z.AnimalP[Y, i]
        z.TotNitr[Y, 0] += z.StreamBankN[Y, i] + z.TileDrainN[Y, i] + z.AnimalN[Y, i]
        z.TotPhos[Y, 0] += z.StreamBankP[Y, i] + z.TileDrainP[Y, i] + z.AnimalP[Y, i]
