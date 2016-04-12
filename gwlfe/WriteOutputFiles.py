# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from . import LoadReductions


def WriteOutput(z):
    print('WriteOutput')
    LoadReductions.AdjustScnLoads(z)
    UrbanAreasOutput()


def WriteOutputSumFiles():
    print('WriteOutputSumFiles')


def UrbanAreasOutput():
    print('UrbanAreasOutput')
