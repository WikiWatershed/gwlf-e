# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from LoadReductions.bas
"""

import logging


log = logging.getLogger(__name__)


def AdjustScnLoads(z):
    log.debug('AdjustScnLoads')

    # Check for zero values
    if z.n23 == 0:
        z.n23 = 0.0000001
    if z.n24 == 0:
        z.n24 = 0.0000001
    if z.n42 == 0:
        z.n42 = 0.0000001

    # Estimate sediment reductions for row crops based on ag BMPs
    SROWBMP1 = (z.n25 / 100) * z.n1 * z.n79
    SROWBMP2 = (z.n26 / 100) * z.n1 * z.n81
    SROWBMP3 = (z.n27 / 100) * z.n1 * z.n82
    SROWBMP4 = (z.n27b / 100) * z.n1 * z.n82b
    SROWBMP5 = (z.n28 / 100) * z.n1 * z.n83
    SROWBMP8 = (z.n29 / 100) * z.n1 * z.n84
    SROWRED = z.n1 - (SROWBMP1 + SROWBMP2 + SROWBMP3 + SROWBMP4 + SROWBMP5 + SROWBMP8)
    if (z.SMCheck == "Both" or z.SMCheck == "Upland"):
        if z.n42 > 0:
            SROWSM1 = (z.n43 / z.n42) * SROWRED * z.n80
        if z.n42 > 0:
            SROWSM2 = (z.n46c / z.n42) * SROWRED * z.n85d
        SROWBUF = SROWSM1 + SROWSM2
    else:
        if (z.n42 > 0):
            SROWBUF = (z.n43 / z.n42) * SROWRED * z.n80

    n1Start = z.n1
    z.n1 = SROWRED - SROWBUF
    if (z.n1 < (n1Start * 0.05)):
        z.n1 = n1Start * 0.05

    # Calculate total nitrogen reduction for row crops based on ag BMPs
    NROWBMP6 = (z.n28b / 100) * z.n5 * z.n70
    NROWNM = z.n5 - NROWBMP6
    NROWBMP1 = (z.n25 / 100) * NROWNM * z.n63
    NROWBMP2 = (z.n26 / 100) * NROWNM * z.n65
    NROWBMP3 = (z.n27 / 100) * NROWNM * z.n66
    NROWBMP4 = (z.n27b / 100) * NROWNM * z.n66b
    NROWBMP5 = (z.n28 / 100) * NROWNM * z.n67
    NROWBMP8 = (z.n29 / 100) * NROWNM * z.n68
    NROWRED = NROWNM - (NROWBMP1 + NROWBMP2 + NROWBMP3 + NROWBMP4 + NROWBMP5 + NROWBMP8)
    if (z.SMCheck == "Both" or z.SMCheck == "Upland"):
        if (z.n42 > 0):
            NROWSM1 = (z.n43 / z.n42) * NROWRED * z.n64
        if (z.n42 > 0):
            NROWSM2 = (z.n46c / z.n42) * NROWRED * z.n69c
        NROWBUF = NROWSM1 + NROWSM2
    else:
        if (z.n42 > 0):
            NROWBUF = (z.n43 / z.n42) * NROWRED * z.n64

    n5Start = z.n5
    z.n5 = NROWRED - NROWBUF
    if (z.n5 < (n5Start * 0.05)):
        z.n5 = n5Start * 0.05

    # Calculate dissolved nitrogen reduction for row crops based on ag BMPs
    NROWBMP6 = (z.n28b / 100) * z.n5dn * z.n70
    NROWNM = z.n5dn - NROWBMP6
    NROWBMP1 = (z.n25 / 100) * NROWNM * z.n63
    NROWBMP2 = (z.n26 / 100) * NROWNM * z.n65
    NROWBMP3 = (z.n27 / 100) * NROWNM * z.n66
    NROWBMP4 = (z.n27b / 100) * NROWNM * z.n66b
    NROWBMP5 = (z.n28 / 100) * NROWNM * z.n67
    NROWBMP8 = (z.n29 / 100) * NROWNM * z.n68
    NROWRED = NROWNM - (NROWBMP1 + NROWBMP2 + NROWBMP3 + NROWBMP4 + NROWBMP5 + NROWBMP8)
    if (z.SMCheck == "Both" or z.SMCheck == "Upland"):
        if (z.n42 > 0):
            NROWSM1 = (z.n43 / z.n42) * NROWRED * z.n64
        if (z.n42 > 0):
            NROWSM2 = (z.n46c / z.n42) * NROWRED * z.n69c
        NROWBUF = NROWSM1 + NROWSM2
    else:
        if (z.n42 > 0):
            NROWBUF = (z.n43 / z.n42) * NROWRED * z.n64

    n5dnStart = z.n5dn
    z.n5dn = NROWRED - NROWBUF
    if (z.n5dn < (n5dnStart * 0.05)):
        z.n5dn = n5dnStart * 0.05

    # Calculate total phosphorus reduction for row crops based on ag BMPs
    PROWBMP6 = (z.n28b / 100) * z.n12 * z.n78
    PROWNM = z.n12 - PROWBMP6
    PROWBMP1 = (z.n25 / 100) * PROWNM * z.n71
    PROWBMP2 = (z.n26 / 100) * PROWNM * z.n73
    PROWBMP3 = (z.n27 / 100) * PROWNM * z.n74
    PROWBMP4 = (z.n27b / 100) * PROWNM * z.n74b
    PROWBMP5 = (z.n28 / 100) * PROWNM * z.n75

    PROWBMP8 = (z.n29 / 100) * PROWNM * z.n76
    PROWRED = PROWNM - (PROWBMP1 + PROWBMP2 + PROWBMP3 + PROWBMP4 + PROWBMP5 + PROWBMP8)
    if (z.SMCheck == "Both" or z.SMCheck == "Upland"):
        if (z.n42 > 0):
            PROWSM1 = (z.n43 / z.n42) * PROWRED * z.n72
        if (z.n42 > 0):
            PROWSM2 = (z.n46c / z.n42) * PROWRED * z.n77c
        PROWBUF = PROWSM1 + PROWSM2
    else:
        if (z.n42 > 0):
            PROWBUF = (z.n43 / z.n42) * PROWRED * z.n72

    z.n12Start = z.n12
    z.n12 = PROWRED - PROWBUF
    if (z.n12 < (z.n12Start * 0.05)):
        z.n12 = z.n12Start * 0.05

    # Calculate dissolved phosphorus reduction for row crops based on ag BMPs
    PROWBMP6 = (z.n28b / 100) * z.n12dp * z.n78
    PROWNM = z.n12dp - PROWBMP6
    PROWBMP1 = (z.n25 / 100) * PROWNM * z.n71
    PROWBMP2 = (z.n26 / 100) * PROWNM * z.n73
    PROWBMP3 = (z.n27 / 100) * PROWNM * z.n74
    PROWBMP4 = (z.n27b / 100) * PROWNM * z.n74b
    PROWBMP5 = (z.n28 / 100) * PROWNM * z.n75

    PROWBMP8 = (z.n29 / 100) * PROWNM * z.n76
    PROWRED = PROWNM - (PROWBMP1 + PROWBMP2 + PROWBMP3 + PROWBMP4 + PROWBMP5 + PROWBMP8)
    if (z.SMCheck == "Both" or z.SMCheck == "Upland"):
        if (z.n42 > 0):
            PROWSM1 = (z.n43 / z.n42) * PROWRED * z.n72
        if (z.n42 > 0):
            PROWSM2 = (z.n46c / z.n42) * PROWRED * z.n77c
        PROWBUF = PROWSM1 + PROWSM2
    else:
        if (z.n42 > 0):
            PROWBUF = (z.n43 / z.n42) * PROWRED * z.n72

    n12dpStart = z.n12dp
    z.n12dp = PROWRED - PROWBUF
    if (z.n12dp < (n12dpStart * 0.05)):
        z.n12dp = n12dpStart * 0.05

    # Calculate sed reduction for hay/pasture based on ag BMPs
    SHAYBMP4 = (z.n33c / 100) * z.n2 * z.n82b
    SHAYBMP5 = (z.n35 / 100) * z.n2 * z.n83
    SHAYBMP7 = (z.n36 / 100) * z.n2 * z.n84b
    SHAYBMP8 = (z.n37 / 100) * z.n2 * z.n84

    n2Start = z.n2
    z.n2 = z.n2 - (SHAYBMP4 + SHAYBMP5 + SHAYBMP7 + SHAYBMP8)
    if (z.n2 < (n2Start * 0.05)):
        z.n2 = n2Start * 0.05

    # Calculate total nitrogen reduction for hay/pasture based on different percent usage of BMPs
    NHAYBMP6 = (z.n35b / 100) * z.n6 * z.n70
    NHAYNM = z.n6 - NHAYBMP6
    NHAYBMP4 = (z.n33c / 100) * NHAYNM * z.n66b
    NHAYBMP5 = (z.n35 / 100) * NHAYNM * z.n67
    NHAYBMP7 = (z.n36 / 100) * NHAYNM * z.n68b
    NHAYBMP8 = (z.n37 / 100) * NHAYNM * z.n68

    n6Start = z.n6
    z.n6 = NHAYNM - (NHAYBMP4 + NHAYBMP5 + NHAYBMP7 + NHAYBMP8)
    if (z.n6 < (n6Start * 0.05)):
        z.n6 = n6Start * 0.05

    # Calculate dissolved nitrogen reduction for hay/pasture
    NHAYBMP6 = (z.n35b / 100) * z.n6dn * z.n70
    NHAYNM = z.n6dn - NHAYBMP6
    NHAYBMP4 = (z.n33c / 100) * NHAYNM * z.n66b
    NHAYBMP5 = (z.n35 / 100) * NHAYNM * z.n67
    NHAYBMP7 = (z.n36 / 100) * NHAYNM * z.n68b
    NHAYBMP8 = (z.n37 / 100) * NHAYNM * z.n68

    n6dnStart = z.n6dn
    z.n6dn = NHAYNM - (NHAYBMP4 + NHAYBMP5 + NHAYBMP7 + NHAYBMP8)
    if (z.n6dn < (n6dnStart * 0.05)):
        z.n6dn = n6dnStart * 0.05

    # Calculate total phosphorus reduction for hay/pasture based on different percent usage of BMPs
    PHAYBMP6 = (z.n35b / 100) * z.n13 * z.n78
    PHAYNM = z.n13 - PHAYBMP6
    PHAYBMP4 = (z.n33c / 100) * PHAYNM * z.n74b
    PHAYBMP5 = (z.n35 / 100) * PHAYNM * z.n75
    PHAYBMP7 = (z.n36 / 100) * PHAYNM * z.n76b
    PHAYBMP8 = (z.n37 / 100) * PHAYNM * z.n76

    n13Start = z.n13
    z.n13 = PHAYNM - (PHAYBMP4 + PHAYBMP5 + PHAYBMP7 + PHAYBMP8)
    if (z.n13 < (n13Start * 0.05)):
        z.n13 = n13Start * 0.05

    # Calculate dissolved phosphorus reduction for hay/pasture
    PHAYBMP6 = (z.n35b / 100) * z.n13dp * z.n78
    PHAYNM = z.n13dp - PHAYBMP6
    PHAYBMP4 = (z.n33c / 100) * PHAYNM * z.n74b
    PHAYBMP5 = (z.n35 / 100) * PHAYNM * z.n75
    PHAYBMP7 = (z.n36 / 100) * PHAYNM * z.n76b
    PHAYBMP8 = (z.n37 / 100) * PHAYNM * z.n76

    n13dpStart = z.n13dp
    z.n13dp = PHAYNM - (PHAYBMP4 + PHAYBMP5 + PHAYBMP7 + PHAYBMP8)
    if (z.n13dp < (n13dpStart * 0.05)):
        z.n13dp = n13dpStart * 0.05

    # Calculate nitrogen reducton for animal activities based on differnt percent usage of BMPs
    NAWMSL = (z.n41b / 100) * z.n85h * z.GRLBN
    NAWMSP = (z.n41d / 100) * z.n85j * z.NGLBN
    NRUNCON = (z.n41f / 100) * z.n85l * (z.GRLBN + z.NGLBN)
    if z.n42 > 0:
        NFENCING = (z.n45 / z.n42) * z.n69 * z.GRSN
        NAGBUFFER = (z.n43 / z.n42) * z.n64 * (z.n7b - (z.NGLBN + z.GRLBN + z.GRSN))

    z.n7b = z.n7b - (NAWMSL + NAWMSP + NRUNCON + NFENCING + NAGBUFFER)

    # Calculate phosphorus reduction for animal activities based on different percent of BMPs
    PAWMSL = (z.n41b / 100) * z.n85i * z.GRLBP
    PAWMSP = (z.n41d / 100) * z.n85k * z.NGLBP
    PRUNCON = (z.n41f / 100) * z.n85m * (z.GRLBP + z.NGLBP)
    PHYTASEP = (z.n41h / 100) * z.n85n * (z.NGLManP + z.NGLBP)
    if z.n42 > 0:
        PFENCING = (z.n45 / z.n42) * z.n77 * z.GRSP
        PAGBUFFER = (z.n43 / z.n42) * z.n72 * (z.n14b - (z.NGLBP + z.GRLBP + z.GRSP))

    z.n14b = z.n14b - (PAWMSL + PAWMSP + PRUNCON + PHYTASEP + PFENCING + PAGBUFFER)

    # Calculate Urban Load Reductions

    # High Urban S load
    # Urban Sediment Load Reduction from Wetlands and Streambank Stabilization
    # . . . High-density areas
    SURBWETH = z.n25b * z.n2b * z.n85b
    z.n2b = z.n2b - SURBWETH
    if z.n2b < 0:
        z.n2b = 0

    # . . . Low-density areas
    SURBWETL = z.n25b * z.n2c * z.n85b
    z.n2c = z.n2c - SURBWETL
    if z.n2c < 0:
        z.n2c = 0

    # Urban Nitrogen Load Reduction from Wetlands and Streambank Stabilization
    # . . . High-density areas
    NURBWETH = z.n25b * z.n6b * z.n69b
    z.n6b = z.n6b - NURBWETH
    if z.n6b < 0:
        z.n6b = 0

    # Urban Dissolved Nitrogen Reduction
    NURBWETH = z.n25b * z.n6bdn * z.n69b
    z.n6bdn = z.n6bdn - NURBWETH
    if z.n6bdn < 0:
        z.n6bdn = 0

    # . . . Low-density areas
    NURBWETL = z.n25b * z.n6c * z.n69b
    z.n6c = z.n6c - NURBWETL
    if z.n6c < 0:
        z.n6c = 0

    # Urban Dissolved Nitrogen Reduction
    NURBWETL = z.n25b * z.n6cdn * z.n69b
    z.n6cdn = z.n6cdn - NURBWETL
    if z.n6cdn < 0:
        z.n6cdn = 0

    # Urban Phosphorus Load Reduction from Wetlands and Streambank Stabilization
    # . . . High-density areas
    PURBWETH = z.n25b * z.n13b * z.n77b
    z.n13b = z.n13b - PURBWETH
    if z.n13b < 0:
        z.n13b = 0

    # Urban Dissolved Phosphorus Reduction
    PURBWETH = z.n25b * z.n13bdp * z.n77b
    z.n13bdp = z.n13bdp - PURBWETH
    if z.n13bdp < 0:
        z.n13bdp = 0

    # . . . Low-density areas
    PURBWETL = z.n25b * z.n13c * z.n77b
    z.n13c = z.n13c - PURBWETL
    if z.n13c < 0:
        z.n13c = 0

    # Urban Dissolved Phosphorus Reduction
    PURBWETL = z.n25b * z.n13cdp * z.n77b
    z.n13cdp = z.n13cdp - PURBWETL
    if z.n13cdp < 0:
        z.n13cdp = 0

    # Farm animal FC load reductions
    FCAWMSL = (z.n41b / 100) * z.n85q * z.GRLBFC
    FCAWMSP = (z.n41d / 100) * z.n85r * z.NGLBFC
    FCRUNCON = (z.n41f / 100) * z.n85s * (z.NGLBFC + z.GRLBFC)
    FCFENCING = (z.n45 / z.n42) * z.n85p * z.GRSFC
    FCAGBUFFER = (z.n43 / z.n42) * z.n85o * (z.n139 - (z.NGLBFC + z.GRLBFC + z.GRSFC))
    if FCAGBUFFER < 0:
        FCAGBUFFER = 0

    # For Animal FC
    z.n145 = z.n139 - (FCAWMSL + FCAWMSP + FCRUNCON + FCFENCING + FCAGBUFFER)
    if z.n145 < 0:
        z.n145 = 0

    # For urban FC
    FCURBBIO = z.n142 * z.RetentEff * z.n85u
    FCURBWET = z.n142 * z.n25b * z.n85t
    FCURBBUF = z.n142 * z.FilterEff * z.PctStrmBuf * z.n85o
    z.n148 = z.n142 - (FCURBBIO + FCURBWET + FCURBBUF)
    if z.n148 < 0:
        z.n148 = 0

    # Calculations for Unpaved Roads N, P and Sed Load Reduction
    if z.n42c > 0:
        SEDUNPAVED = (z.n46o / z.n42c) * z.n2d * z.n85g * 1.4882
        z.n2d = z.n2d - SEDUNPAVED
        if z.n2d < 0:
            z.n2d = 0

        NUNPAVED = (z.n46o / z.n42c) * z.n6d * z.n85e * 1.4882
        z.n6d = z.n6d - NUNPAVED
        if z.n6d < 0:
            z.n6d = 0

        NUNPAVED = (z.n46o / z.n42c) * z.n6ddn * z.n85e * 1.4882
        z.n6ddn = z.n6ddn - NUNPAVED
        if z.n6ddn < 0:
            z.n6ddn = 0

        PUNPAVED = (z.n46o / z.n42c) * z.n13d * z.n85f * 1.4882
        z.n13d = z.n13d - PUNPAVED
        if z.n13d < 0:
            z.n13d = 0

        PUNPAVED = (z.n46o / z.n42c) * z.n13ddp * z.n85f * 1.4882
        z.n13ddp = z.n13ddp - PUNPAVED
        if z.n13d < 0:
            z.n13ddp = 0
