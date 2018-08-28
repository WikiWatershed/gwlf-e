# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class YesOrNo(object):
    NO = '<No>'
    YES = '<Yes>'

    @classmethod
    def parse(cls, value):
        if value in ('0', 'N'):
            return cls.NO
        elif value in ('1', 'Y'):
            return cls.YES
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def intval(cls, value):
        if value == cls.NO:
            return 0
        elif value == cls.YES:
            return 1
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def gmsval(cls, value):
        if value == cls.NO:
            return 'N'
        elif value == cls.YES:
            return 'Y'
        raise ValueError('Unexpected value: ' + str(value))


class ETflag(object):
    HAMON_METHOD = '<Hamon method>'
    BLAINY_CRIDDLE_METHOD = '<Blainy-Criddle method>'

    @classmethod
    def parse(cls, value):
        value = int(value)
        if value == 0:
            return cls.HAMON_METHOD
        elif value == 1:
            return cls.BLAINY_CRIDDLE_METHOD
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def gmsval(cls, value):
        if value == cls.HAMON_METHOD:
            return 0
        elif value == cls.BLAINY_CRIDDLE_METHOD:
            return 1
        raise ValueError('Unexpected value: ' + str(value))


GROWING_SEASON = '<Growing season>'


class GrowFlag(object):
    NON_GROWING_SEASON = '<Non-growing season>'
    GROWING_SEASON = '<Growing season>'

    @classmethod
    def parse(cls, value):
        value = int(value)
        if value == 0:
            return cls.NON_GROWING_SEASON
        elif value == 1:
            return cls.GROWING_SEASON
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def intval(cls, value):
        if value == cls.NON_GROWING_SEASON:
            return 0
        elif value == cls.GROWING_SEASON:
            return 1
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def gmsval(cls, value):
        return cls.intval(value)


class SweepType(object):
    VACUUM = '<Vacuum>'
    MECHANICAL = '<Mechanical>'

    @classmethod
    def parse(cls, value):
        value = int(value)
        if value == 1:
            return cls.MECHANICAL
        elif value == 2:
            return cls.VACUUM
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def gmsval(cls, value):
        if value == cls.MECHANICAL:
            return 1
        elif value == cls.VACUUM:
            return 2
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

    @classmethod
    def parse(cls, value):
        if value == 'Water':
            return cls.WATER
        if value in ('Hay/Past', 'Hay'):
            return cls.HAY_PAST
        elif value == 'Cropland':
            return cls.CROPLAND
        elif value == 'Forest':
            return cls.FOREST
        elif value == 'Wetland':
            return cls.WETLAND
        elif value in ('Disturbed', 'Disturbed Land'):
            return cls.DISTURBED
        elif value == 'Turfgrass':
            return cls.TURFGRASS
        elif value in ('Open_Land', 'Open Land'):
            return cls.OPEN_LAND
        elif value in ('Bare_Rock', 'Bare Rock'):
            return cls.BARE_ROCK
        elif value in ('Sandy_Areas', 'Sandy Areas'):
            return cls.SANDY_AREAS
        elif value in ('Unpaved_Road', 'Unpaved Roads'):
            return cls.UNPAVED_ROAD
        elif value in ('Ld_Mixed', 'LD Mixed'):
            return cls.LD_MIXED
        elif value in ('Md_Mixed', 'MD Mixed'):
            return cls.MD_MIXED
        elif value in ('Hd_Mixed', 'HD Mixed'):
            return cls.HD_MIXED
        elif value in ('Ld_Residential', 'LD Residential',
                       'Ld_Open_Space', 'LD Open Space'):
            return cls.LD_RESIDENTIAL
        elif value in ('Md_Residential', 'MD Residential'):
            return cls.MD_RESIDENTIAL
        elif value in ('Hd_Residential', 'HD Residential'):
            return cls.HD_RESIDENTIAL
        raise ValueError('Unexpected value: ' + str(value))

    @classmethod
    def gmsval(cls, value):
        if value == cls.WATER:
            return 'Water'
        elif value == cls.HAY_PAST:
            return 'Hay/Past'
        elif value == cls.CROPLAND:
            return 'Cropland'
        elif value == cls.FOREST:
            return 'Forest'
        elif value == cls.WETLAND:
            return 'Wetland'
        elif value == cls.DISTURBED:
            return 'Disturbed'
        elif value == cls.TURFGRASS:
            return 'Turfgrass'
        elif value == cls.OPEN_LAND:
            return 'Open_Land'
        elif value == cls.BARE_ROCK:
            return 'Bare_Rock'
        elif value == cls.SANDY_AREAS:
            return 'Sandy_Areas'
        elif value == cls.UNPAVED_ROAD:
            return 'Unpaved_Road'
        elif value == cls.LD_MIXED:
            return 'Ld_Mixed'
        elif value == cls.MD_MIXED:
            return 'Md_Mixed'
        elif value == cls.HD_MIXED:
            return 'Hd_Mixed'
        elif value == cls.LD_RESIDENTIAL:
            return 'Ld_Open_Space'
        elif value == cls.MD_RESIDENTIAL:
            return 'Md_Residential'
        elif value == cls.HD_RESIDENTIAL:
            return 'Hd_Residential'
        raise ValueError('Unexpected value: ' + str(value))
