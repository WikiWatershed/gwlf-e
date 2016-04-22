# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


class YesOrNo(object):
    NO = '<No>'
    YES = '<Yes>'

    @staticmethod
    def parse(value):
        if value in ('0', 'N'):
            return YesOrNo.NO
        elif value in ('1', 'Y'):
            return YesOrNo.YES
        raise ValueError('Unexpected value: ' + str(value))


class ETflag(object):
    HAMON_METHOD = '<Hamon method>'
    BLAINY_CRIDDLE_METHOD = '<Blainy-Criddle method>'

    @staticmethod
    def parse(value):
        value = int(value)
        if value == 0:
            return ETflag.HAMON_METHOD
        elif value == 1:
            return ETflag.BLAINY_CRIDDLE_METHOD
        raise ValueError('Unexpected value: ' + str(value))


class GrowFlag(object):
    NON_GROWING_SEASON = '<Non-growing season>'
    GROWING_SEASON = '<Growing season>'

    @staticmethod
    def parse(value):
        value = int(value)
        if value == 0:
            return GrowFlag.NON_GROWING_SEASON
        elif value == 1:
            return GrowFlag.GROWING_SEASON
        raise ValueError('Unexpected value: ' + str(value))

    @staticmethod
    def intval(value):
        if value == GrowFlag.NON_GROWING_SEASON:
            return 0
        elif value == GrowFlag.GROWING_SEASON:
            return 1
        raise ValueError('Unexpected value: ' + str(value))


class SweepType(object):
    VACUUM = '<Vacuum>'
    MECHANICAL = '<Mechanical>'

    @staticmethod
    def parse(value):
        value = int(value)
        if value == 1:
            return SweepType.MECHANICAL
        elif value == 2:
            return GrowFlag.VACUUM
        raise ValueError('Unexpected value: ' + str(value))


# TODO: Use actual NLCD values
# Reference: https://drive.google.com/a/azavea.com/file/d/0B3v0QxIOuR_nX3Rnekp0NGUyOGM/view
class LandUse(object):
    WATER = '<Water>'
    HAY_PAST = '<Hay/Past>'
    CROPLAND = '<Cropland>'
    FOREST = '<Forest>'
    WETLAND = '<Wetland>'
    DISTURBED = '<Disturbed>'
    TURFGRASS = '<Turfgrass>'
    OPEN_LAND = '<Open_Land>'
    BARE_ROCK = '<Bare_Rock>'
    SANDY_AREAS = '<Sandy_Areas>'
    UNPAVED_ROAD = '<Unpaved_Road>'
    LD_MIXED = '<Ld_Mixed>'
    MD_MIXED = '<Md_Mixed>'
    HD_MIXED = '<Hd_Mixed>'
    LD_RESIDENTIAL = '<Ld_Residential>'
    MD_RESIDENTIAL = '<Md_Residential>'
    HD_RESIDENTIAL = '<Hd_Residential>'

    @staticmethod
    def parse(value):
        if value == 'Water':
            return LandUse.WATER
        if value in ('Hay/Past', 'Hay'):
            return LandUse.HAY_PAST
        elif value == 'Cropland':
            return LandUse.CROPLAND
        elif value == 'Forest':
            return LandUse.FOREST
        elif value == 'Wetland':
            return LandUse.WETLAND
        elif value in ('Disturbed', 'Disturbed Land'):
            return LandUse.DISTURBED
        elif value == 'Turfgrass':
            return LandUse.TURFGRASS
        elif value in ('Open_Land', 'Open Land'):
            return LandUse.OPEN_LAND
        elif value in ('Bare_Rock', 'Bare Rock'):
            return LandUse.BARE_ROCK
        elif value in ('Sandy_Areas', 'Sandy Areas'):
            return LandUse.SANDY_AREAS
        elif value in ('Unpaved_Road', 'Unpaved Roads'):
            return LandUse.UNPAVED_ROAD
        elif value in ('Ld_Mixed', 'LD Mixed'):
            return LandUse.LD_MIXED
        elif value in ('Md_Mixed', 'MD Mixed'):
            return LandUse.MD_MIXED
        elif value in ('Hd_Mixed', 'HD Mixed'):
            return LandUse.HD_MIXED
        elif value in ('Ld_Residential', 'LD Residential'):
            return LandUse.LD_RESIDENTIAL
        elif value in ('Md_Residential', 'MD Residential'):
            return LandUse.MD_RESIDENTIAL
        elif value in ('Hd_Residential', 'HD Residential'):
            return LandUse.HD_RESIDENTIAL
        raise ValueError('Unexpected value: ' + str(value))
