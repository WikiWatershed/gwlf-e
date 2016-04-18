# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import numpy as np

def ReDimRunQualVars(z):
    print('ReDimRunQualVars')
    # TODO: Port PrelimQualCalculations
    # Most of these values are placeholder
    # to get the model to run.
    z.ImpervAccum = np.zeros(16)
    z.PervAccum = np.zeros(16)
    z.LuLoad = np.zeros([z.DimYrs, 16, 3])
    z.LuDisLoad = np.zeros([z.DimYrs, 16, 3])
    z.Erosiv = 6.46
    z.QrunI = np.zeros(16)
    z.QrunP = np.zeros(16)
    z.WashPerv = np.zeros(16)
    z.NetDisLoad = np.zeros(3)
    z.UrbanQTotal = 0
