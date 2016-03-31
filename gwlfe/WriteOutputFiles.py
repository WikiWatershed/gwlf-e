# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from . import LoadReductions


def WriteOutput():
    print('WriteOutput')
    LoadReductions.AdjustScnLoads()
    UrbanAreasOutput()


def WriteOutputSumFiles():
    print('WriteOutputSumFiles')


def UrbanAreasOutput():
    print('UrbanAreasOutput')
