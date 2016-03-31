#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from . import ReadGwlfDataFile
from . import PrelimCalculations
from . import CalcCnErosRunoffSed
from . import AFOS
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles


def run():
    print('Running model...')
    ReadGwlfDataFile.ReadAllData()
    PrelimCalculations.InitialCalculations()

    for year in range(100):
        for month in range(12):
            for day in range(30):
                CalcCnErosRunoffSed.CalcCN()

        AFOS.AnimalOperations()
        CalcLoads.CalculateLoads()
        StreamBank.CalculateStreamBankEros()
        AnnualMeans.CalculateAnnualMeanLoads()

    WriteOutputFiles.WriteOutput()
    WriteOutputFiles.WriteOutputSumFiles()

    print('Done')
