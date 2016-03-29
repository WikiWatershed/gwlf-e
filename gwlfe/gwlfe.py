#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import csv
import logging

from collections import defaultdict


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


EOL = '<EOL>'


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
    HAMMON_METHOD = '<Hammon method>'
    BLAINY_CRIDDLE_METHOD = '<Blainy-Criddle method>'

    @staticmethod
    def parse(value):
        value = int(value)
        if value == 0:
            return ETflag.HAMMON_METHOD
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


def iterate_csv_values(fp):
    """
    Yield values as a continuous stream for each line in a
    file-like object.
    """
    reader = csv.reader(fp)
    line_no = 1
    for line in reader:
        col_no = 1
        for value in line:
            yield value, line_no, col_no
            col_no += 1
        yield EOL, line_no, col_no
        line_no += 1


class GmsReader(object):
    def __init__(self, fp):
        self.fp = iterate_csv_values(fp)

    def read(self):
        result = defaultdict(list)

        # Line 1:
        result['NRur'] = self.next(int)  # Number of Rural Land Use Categories
        result['NUrb'] = self.next(int)  # Number Urban Land Use Categories
        result['BasinId'] = self.next(int)  # Basin ID
        self.next(EOL)

        # Line 2:
        result['TranVersionNo'] = self.next(str)  # GWLF-E Version
        result['RecessionCoef'] = self.next(float)  # Recession Coefficient
        result['SeepCoef'] = self.next(float)  # Seepage Coefficient
        result['UnsatStor'] = self.next(float)  # Unsaturated Storage
        result['SatStor'] = self.next(float)  # Saturated Storage
        result['InitSnow'] = self.next(int)  # Initial Snow Days
        result['SedDelivRatio'] = self.next(float)  # Sediment Delivery Ratio
        result['MaxWaterCap'] = self.next(float)  # Average Available Water Capacity
        result['StreamLength'] = self.next(float)  # Total Stream Length (meters)
        result['AgLength'] = self.next(float)  # Agricultural Stream Length (meters)
        result['UrbLength'] = self.next(float)  # Urban Stream Length (meters)
        result['AgSlope3'] = self.next(float)  # Area of agricultural land with slope > 3%
        result['AgSlope3to8'] = self.next(float)  # Area of agricultural land with slope > 3% and < 8%
        result['AvSlope'] = self.next(float)  # Average % Slope
        result['AEU'] = self.next(float)  # Number of Animal Units
        result['WxYrs'] = self.next(int)  # Total Weather Years
        result['WxYrBeg'] = self.next(int)  # Beginning Weather Year
        result['WxYrEnd'] = self.next(int)  # Ending Weather Year
        result['SedAFactor'] = self.next(float)  # Sediment A Factor
        result['TotArea'] = self.next(float)  # Total Basin Area (Ha)
        result['TileDrainRatio'] = self.next(float)  # Tile Drain Ratio
        result['TileDrainDensity'] = self.next(float)  # Tile Drain Density
        result['ETFlag'] = self.next(ETflag.parse)  # ET Flag
        result['AvKF'] = self.next(float)  # Average K Factor
        self.next(EOL)

        # Lines 3 - 7: (each line represents 1 day)
        # Antecedent Rain + Melt Moisture Condition for Days 1 to 5
        for i in range(5):
            result['AntMoist'].append(self.next(float))
            self.next(EOL)

        # Lines 8 - 19: (each line represents 1 month)
        for i in range(12):
            result['Month'].append(self.next(str))  # Month (Jan - Dec)
            result['KV'].append(self.next(float))  # KET (Flow Factor)
            result['DayHrs'].append(self.next(float))  # Day Length (hours)
            result['Grow'].append(self.next(GrowFlag.parse))  # Growing season flag
            result['Acoef'].append(self.next(float))  # Erosion Coefficient
            result['StreamWithdrawal'].append(self.next(float))  # Surface Water Withdrawal/Extraction
            result['GroundWithdrawal'].append(self.next(float))  # Groundwater Withdrawal/Extraction
            result['PcntET'].append(self.next(float))  # Percent monthly adjustment for ET calculation
            self.next(EOL)

        # Lines 20 - 29: (for each Rural Land Use Category)
        for i in range(result['NRur']):
            result['Landuse'] = self.next(LandUse.parse)  # Rural Land Use Category
            result['Area'] = self.next(float)  # Area (Ha)
            result['CN'] = self.next(float)  # Curve Number
            result['KF'] = self.next(float)  # K Factor
            result['LS'] = self.next(float)  # LS Factor
            result['C'] = self.next(float)   # C Factor
            result['P'] = self.next(float)   # P Factor
            self.next(EOL)

        # Lines 30 - 35: (for each Urban Land Use Category)
        for i in range(result['NUrb']):
            result['Landuse'] = self.next(LandUse.parse)  # Urban Land Use Category
            result['Area'] = self.next(float)  # Area (Ha)
            result['Imper'] = self.next(float)  # Impervious Surface %
            result['CNI'] = self.next(float)  # Curve Number(Impervious Surfaces)
            result['CNP'] = self.next(float)  # Curve Number(Pervious Surfaces)
            result['TotSusSolids'] = self.next(float)  # Total Suspended Solids Factor
            self.next(EOL)

        # Line 36:
        result['PhysFlag'] = self.next(YesOrNo.parse)  # Physiographic Province Layer Detected
        result['PointFlag'] = self.next(YesOrNo.parse)  # Point Source Layer Detected
        result['SeptSysFlag'] = self.next(YesOrNo.parse)  # Septic System Layer Detected
        result['CountyFlag'] = self.next(YesOrNo.parse)  # County Layer Detected
        result['SoilPFlag'] = self.next(YesOrNo.parse)  # Soil P Layer Detected
        result['GWNFlag'] = self.next(YesOrNo.parse)  # Groundwater N Layer Detected
        result['SedAAdjust'] = self.next(float)  # Default Percent ET
        self.next(EOL)

        # Line 37:
        result['SedNitr'] = self.next(float)  # Soil Concentration: N (mg/l)
        result['SedPhos'] = self.next(float)  # Soil Concentration: P (mg/l)
        result['GrNitrConc'] = self.next(float)  # Groundwater Concentration: N (mg/l)
        result['GrPhosConc'] = self.next(float)  # Groundwater Concentration: P (mg/l)
        result['BankNFrac'] = self.next(float)  # % Bank N Fraction (0 - 1)
        result['BankPFrac'] = self.next(float)  # % Bank P Fraction (0 - 1)
        self.next(EOL)

        # Line 38:
        result['ManuredAreas'] = self.next(int)  # Manure Spreading Periods (Default = 2)
        result['FirstManureMonth'] = self.next(int)  # MS Period 1: First Month
        result['LastManureMonth'] = self.next(int)  # MS Period 1: Last Month
        result['FirstManureMonth2'] = self.next(int)  # MS Period 2: First Month
        result['LastManureMonth2'] = self.next(int)  # MS Period 2: Last Month
        self.next(EOL)

        # Lines 39 - 48: (for each Rural Land Use Category)
        for i in range(result['NRur']):
            result['NitrConc'] = self.next(float)  # Dissolved Runoff Coefficient: N (mg/l)
            result['PhosConc'] = self.next(float)  # Dissolved Runoff Coefficient: P (mg/l)
            self.next(EOL)

        # Line 49:
        result['Nqual'] = self.next(int)  # Number of Contaminants (Default = 3; Nitrogen, Phosphorus, Sediment)
        self.next(EOL)

        # Lines 50 - 52:
        for i in range(result['Nqual']):
            result['Contaminant'].append(self.next(str))
            self.next(EOL)

        result['LoadRateImp'] = [[] for i in range(result['NUrb'])]
        result['LoadRatePerv'] = [[] for i in range(result['NUrb'])]
        result['DisFract'] = [[] for i in range(result['NUrb'])]
        result['UrbBMPRed'] = [[] for i in range(result['NUrb'])]

        # Lines 53 - 58 (for each Urban Land Use Category, Nitrogen Contaminant)
        # Lines 59 - 64: (for each Urban Land Use Category, Phosphorus Contaminant)
        # Lines 65 - 70: (for each Urban Land Use Category, Sediment Contaminant)
        for u in range(result['NUrb']):
            for q in range(result['Nqual']):
                result['LoadRateImp'][u].append(self.next(float))  # Loading Rate Impervious Surface
                result['LoadRatePerv'][u].append(self.next(float))  # Loading Rate Pervious Surface
                result['DisFract'][u].append(self.next(float))  # Dissolved Fraction
                result['UrbBMPRed'][u].append(self.next(float))  # Urban BMP Reduction
                self.next(EOL)

        # Lines 71 - 72: (for the 2 Manure Spreading Periods)
        result['ManNitr'] = (self.next(float), self.next(float))  # Manured N Concentration
        self.next(EOL)

        result['ManPhos'] = (self.next(float), self.next(float))  # Manured P Concentration
        self.next(EOL)

        # Lines 73 - 84: (Point Source data for each Month)
        for i in range(12):
            result['PointNitr'].append(self.next(float))  # N Load (kg)
            result['PointPhos'].append(self.next(float))  # P Load (kg)
            result['PointFlow'].append(self.next(float))  # Discharge (Millions of Gallons per Day)
            self.next(EOL)

        # Line 85:
        result['SepticFlag'] = self.next(YesOrNo.parse)  # Flag: Septic Systems Layer Detected (0 No; 1 Yes)
        self.next(EOL)

        # Lines 86 - 97: (Septic System data for each Month)
        for i in range(12):
            result['NumNormalSys'].append(self.next(int))  # Number of People on Normal Systems
            result['NumPondSys'].append(self.next(int))  # Number of People on Pond Systems
            result['NumShortSys'].append(self.next(int))  # Number of People on Short Circuit Systems
            result['NumDischargeSys'].append(self.next(int))  # Number of People on Discharge Systems
            result['NumSewerSys'].append(self.next(int))  # Number of People on Public Sewer Systems
            self.next(EOL)

        # Line 98: (if Septic System flag = 1)
        if result['SepticFlag'] == YesOrNo.YES:
            result['NitrSepticLoad'] = self.next(float)  # Per Capita Tank Load: N (g/d)
            result['PhosSepticLoad'] = self.next(float)  # Per Capita Tank Load: P (g/d)
            result['NitrPlantUptake'] = self.next(float)  # Growing System Uptake: N (g/d)
            result['PhosPlantUptake'] = self.next(float)  # Growing System Uptake: P (g/d)
            self.next(EOL)
        else:
            raise Exception('SepticFlag must be set to 1')

        # Line 99:
        result['TileNconc'] = self.next(float)  # Tile Drainage Concentration: N (mg/L)
        result['TilePConc'] = self.next(float)  # Tile Drainage Concentration: P (mg/L)
        result['TileSedConc'] = self.next(float)  # Tile Drainage Concentration: Sediment (mg/L)
        self.next(EOL)

        # Line 100: (variables passed through GWLF-E to PRedICT)
        result['InName'] = self.next(str)  # Scenario Run Name
        result['UnitsFileFlag'] = self.next(int)  # Units Flag (Default = 1)
        result['AssessDate'] = self.next(str)  # Assessment/Reference Date (mmyyyy)
        result['VersionNo'] = self.next(str)  # GWLF-E Version Number
        self.next(EOL)

        # Line 101: (variable passed through GWLF-E to PRedICT)
        result['ProjName'] = self.next(str)  # Project Name
        self.next(EOL)

        # Line 102: (Estimated Load by Land Use/Source – Total Sediment (kg x 1000))
        result['n1'] = self.next(float)  # Row Crops
        result['n2'] = self.next(float)  # Hay/Pasture
        result['n2b'] = self.next(float)  # High Density Urban
        result['n2c'] = self.next(float)  # Low Density Urban
        result['n2d'] = self.next(float)  # Unpaved Roads
        result['n3'] = self.next(float)  # Other
        result['n4'] = self.next(float)  # Streambank Erosion
        self.next(EOL)

        # Line 103: (Estimated Load by Land Use/Source – Total Nitrogen (kg))
        result['n5'] = self.next(float)  # Row Crops
        result['n6'] = self.next(float)  # Hay/Pasture
        result['n6b'] = self.next(float)  # High Density Urban
        result['n6c'] = self.next(float)  # Low Density Urban
        result['n6d'] = self.next(float)  # Unpaved Roads
        result['n7'] = self.next(float)  # Other
        result['n7b'] = self.next(float)  # Farm Animals
        result['n8'] = self.next(float)  # Streambank Erosion
        result['n9'] = self.next(float)  # Groundwater/Subsurface
        result['n10'] = self.next(float)  # Point Source Discharges
        result['n11'] = self.next(float)  # Septic Systems
        self.next(EOL)

        # Line 104: (Estimated Load by Land Use/Source – Total Phosphorus (kg))
        result['n12'] = self.next(float)  # Row Crops
        result['n13'] = self.next(float)  # Hay/Pasture
        result['n13b'] = self.next(float)  # High Density Urban
        result['n13c'] = self.next(float)  # Low Density Urban
        result['n13d'] = self.next(float)  # Unpaved Roads
        result['n14'] = self.next(float)  # Other
        result['n14b'] = self.next(float)  # Farm Animals
        result['n15'] = self.next(float)  # Streambank Erosion
        result['n16'] = self.next(float)  # Groundwater/Subsurface
        result['n17'] = self.next(float)  # Point Source Discharges
        result['n18'] = self.next(float)  # Septic Systems
        self.next(EOL)

        # Line 105:
        result['n19'] = self.next(float)  # Total Sediment Load (kg x 1000)
        result['n20'] = self.next(float)  # Total Nitrogen Load (kg)
        result['n21'] = self.next(float)  # Total Phosphorus Load (kg)
        result['n22'] = self.next(float)  # Basin Area (Ha)
        self.next(EOL)

        # Line 106:
        result['n23'] = self.next(float)  # Row Crops Area (Ha)
        result['n23b'] = self.next(float)  # High Density Urban Area (Ha)
        result['n23c'] = self.next(float)  # High Density Urban (Constructed Wetlands): % Drainage Used
        result['n24'] = self.next(float)  # Hay/Pasture Area (Ha)
        result['n24b'] = self.next(float)  # Low Density Urban Area (ha Ha
        result['n24c'] = self.next(float)  # Low Density Urban (Constructed Wetlands): % Drainage Used
        result['n24d'] = self.next(float)  # High Density Urban (Bioretention Areas): % Drainage Used
        result['n24e'] = self.next(float)  # Low Density Urban (Bioretention Areas): % Drainage Used
        self.next(EOL)

        # Line 107:
        result['n25'] = self.next(float)  # Row Crops (BMP 1): Existing (%)
        result['n25b'] = self.next(float)  # High Density Urban (Constructed Wetlands): Existing (%)
        result['n25c'] = self.next(float)  # Low Density Urban (Constructed Wetlands): Existing (%)
        result['n25d'] = self.next(float)  # High Density Urban (Bioretention Areas): Existing (%)
        result['n25e'] = self.next(float)  # Low Density Urban (Bioretention Areas): Existing (%)
        result['n26'] = self.next(float)  # Row Crops (BMP 2): Existing (%)
        result['n26b'] = self.next(float)  # High Density Urban (Detention Basin): Existing (%)
        result['n26c'] = self.next(float)  # Low Density Urban (Detention Basin): Existing (%)
        result['n27'] = self.next(float)  # Row Crops (BMP 3): Existing (%)
        result['n27b'] = self.next(float)  # Row Crops (BMP 4): Existing (%)
        result['n28'] = self.next(float)  # Row Crops (BMP 5): Existing (%)
        result['n28b'] = self.next(float)  # Row Crops (BMP 6): Existing (%)
        result['n29'] = self.next(float)  # Row Crops (BMP 8): Existing (%)
        self.next(EOL)

        # Line 108:
        result['n30'] = self.next(float)  # Row Crops (BMP 1): Future (%)
        result['n30b'] = self.next(float)  # High Density Urban (Constructed Wetlands): Future (%)
        result['n30c'] = self.next(float)  # Low Density Urban (Constructed Wetlands): Future (%)
        result['n30d'] = self.next(float)  # High Density Urban (Bioretention Areas): Future (%)
        result['n30e'] = self.next(float)  # Low Density Urban (Bioretention Areas): Future (%)
        result['n31'] = self.next(float)  # Row Crops (BMP 2): Future (%)
        result['n31b'] = self.next(float)  # High Density Urban (Detention Basin): Future (%)
        result['n31c'] = self.next(float)  # Low Density Urban (Detention Basin): Future (%)
        result['n32'] = self.next(float)  # Row Crops (BMP 3): Future (%)
        result['n32b'] = self.next(float)  # Row Crops (BMP 4): Future (%)
        result['n32c'] = self.next(float)  # Hay/Pasture (BMP 3): Existing (%)
        result['n32d'] = self.next(float)  # Hay/Pasture (BMP 3): Future (%)
        result['n33'] = self.next(float)  # Row Crops (BMP 5): Future (%)
        result['n33b'] = self.next(float)  # Row Crops (BMP 6): Future (%)
        result['n33c'] = self.next(float)  # Hay/Pasture (BMP 4): Existing (%)
        result['n33d'] = self.next(float)  # Hay/Pasture (BMP 4): Future (%)
        self.next(EOL)

        # Line 109:
        result['n34'] = self.next(float)  # Row Crops (BMP 8): Future (%)
        result['n35'] = self.next(float)  # Hay/Pasture (BMP 5): Existing (%)
        result['n35b'] = self.next(float)  # Hay/Pasture (BMP 6): Existing (%)
        result['n36'] = self.next(float)  # Hay/Pasture (BMP 7): Existing (%)
        result['n37'] = self.next(float)  # Hay/Pasture (BMP 8): Existing (%)
        result['n38'] = self.next(float)  # Hay/Pasture (BMP 5): Future (%)
        result['n38b'] = self.next(float)  # Hay/Pasture (BMP 6): Future (%)
        result['n39'] = self.next(float)  # Hay/Pasture (BMP 7): Future (%)
        result['n40'] = self.next(float)  # Hay/Pasture (BMP 8): Future (%)
        self.next(EOL)

        # Line 110:
        result['n41'] = self.next(float)  # Agricultural Land on Slope > 3% (Ha)
        result['n41b'] = self.next(float)  # AWMS (Livestock): Existing (%)
        result['n41c'] = self.next(float)  # AWMS (Livestock): Future (%)
        result['n41d'] = self.next(float)  # AWMS (Poultry): Existing (%)
        result['n41e'] = self.next(float)  # AWMS (Poultry): Future (%)
        result['n41f'] = self.next(float)  # Runoff Control: Existing (%)
        result['n41g'] = self.next(float)  # Runoff Control: Future (%)
        result['n41h'] = self.next(float)  # Phytase in Feed: Existing (%)
        result['n41i'] = self.next(float)  # Phytase in Feed: Future (%)
        result['n41j'] = self.next(float)  # Total Livestock AEUs
        result['n41k'] = self.next(float)  # Total Poultry AEUs
        result['n41l'] = self.next(float)  # Total AEUs
        result['n42'] = self.next(float)  # Streams in Agricultural Areas (km)
        result['n42b'] = self.next(float)  # Total Stream Length (km)
        result['n42c'] = self.next(float)  # Unpaved Road Length (km)
        result['n43'] = self.next(float)  # Stream Km with Vegetated Buffer Strips: Existing
        result['GRLBN'] = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        result['NGLBN'] = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        result['GRLBP'] = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        result['NGLBP'] = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        result['NGLManP'] = self.next(float)  # Average Non-Grazing Animal Loss Rate (Manure Spreading): Phosphorus
        result['NGLBFC'] = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        result['GRLBFC'] = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        result['GRSFC'] = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Fecal Coliform
        result['GRSN'] = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Nitrogen
        result['GRSP'] = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Phosphorus
        self.next(EOL)

        # Line 111:
        result['n43b'] = self.next(float)  # High Density Urban (Constructed Wetlands): Required Ha
        result['n43c'] = self.next(float)  # High Density Urban (Detention Basin): % Drainage Used
        result['n43d'] = self.next(float)  # High Density Urban: % Impervious Surface
        result['n43e'] = self.next(float)  # High Density Urban (Constructed Wetlands): Impervious Ha Drained
        result['n43f'] = self.next(float)  # High Density Urban (Detention Basin): Impervious Ha Drained
        result['n43g'] = self.next(float)  # High Density Urban (Bioretention Areas): Impervious Ha Drained
        result['n43h'] = self.next(float)  # High Density Urban (Bioretention Areas): Required Ha
        result['n43i'] = self.next(float)  # Low Density Urban (Bioretention Areas): Impervious Ha Drained
        result['n43j'] = self.next(float)  # Low Density Urban (Bioretention Areas): Required Ha
        result['n44'] = self.next(float)  # Stream Km with Vegetated Buffer Strips: Future
        result['n44b'] = self.next(float)  # High Density Urban (Detention Basin): Required Ha
        result['n45'] = self.next(float)  # Stream Km with Fencing: Existing
        result['n45b'] = self.next(float)  # Low Density Urban (Constructed Wetlands): Required Ha
        result['n45c'] = self.next(float)  # Low Density Urban (Detention Basin): % Drainage Used
        result['n45d'] = self.next(float)  # Low Density Urban: % Impervious Surface
        result['n45e'] = self.next(float)  # Low Density Urban (Constructed Wetlands): Impervious Ha Drained
        result['n45f'] = self.next(float)  # Low Density Urban (Detention Basin): Impervious Ha Drained
        self.next(EOL)

        # Line 112:
        result['n46'] = self.next(float)  # Stream Km with Fencing: Future
        result['n46b'] = self.next(float)  # Low Density Urban (Detention Basin): Required Ha
        result['n46c'] = self.next(float)  # Stream Km with Stabilization: Existing
        result['n46d'] = self.next(float)  # Stream Km with Stabilization: Future
        result['n46e'] = self.next(float)  # Stream Km in High Density Urban Areas
        result['n46f'] = self.next(float)  # Stream Km in Low Density Urban Areas
        result['n46g'] = self.next(float)  # Stream Km in High Density Urban Areas W/Buffers: Existing
        result['n46h'] = self.next(float)  # Stream Km in High Density Urban Areas W/Buffers: Future
        result['n46i'] = self.next(float)  # High Density Urban Streambank Stabilization (km): Existing
        result['n46j'] = self.next(float)  # High Density Urban Streambank Stabilization (km): Future
        result['n46k'] = self.next(float)  # Stream Km in Low Density Urban Areas W/Buffers: Existing
        result['n46l'] = self.next(float)  # Stream Km in Low Density Urban Areas W/Buffers: Future
        result['n46m'] = self.next(float)  # Low Density Urban Streambank Stabilization (km): Existing
        result['n46n'] = self.next(float)  # Low Density Urban Streambank Stabilization (km): Future
        result['n46o'] = self.next(float)  # Unpaved Road Km with E and S Controls (km): Existing
        result['n46p'] = self.next(float)  # Unpaved Road Km with E and S Controls (km): Future
        self.next(EOL)

        # Line 113:
        result['n47'] = self.next(float)  # Number of Persons on Septic Systems: Existing
        result['n48'] = self.next(float)  # No longer used (Default = 0)
        result['n49'] = self.next(float)  # Number of Persons on Septic Systems: Future
        result['n50'] = self.next(float)  # No longer used (Default = 0)
        result['n51'] = self.next(float)  # Septic Systems Converted by Secondary Treatment Type (%)
        result['n52'] = self.next(float)  # Septic Systems Converted by Tertiary Treatment Type (%)
        result['n53'] = self.next(float)  # No longer used (Default = 0)
        result['n54'] = self.next(float)  # Distribution of Pollutant Discharges by Primary Treatment Type (%): Existing
        result['n55'] = self.next(float)  # Distribution of Pollutant Discharges by Secondary Treatment Type (%): Existing
        result['n56'] = self.next(float)  # Distribution of Pollutant Discharges by Tertiary Treatment Type (%): Existing
        result['n57'] = self.next(float)  # Distribution of Pollutant Discharges by Primary Treatment Type (%): Future
        result['n58'] = self.next(float)  # Distribution of Pollutant Discharges by Secondary Treatment Type (%): Future
        result['n59'] = self.next(float)  # Distribution of Pollutant Discharges by Tertiary Treatment Type (%): Future
        result['n60'] = self.next(float)  # Distribution of Treatment Upgrades (%): Primary to Secondary
        result['n61'] = self.next(float)  # Distribution of Treatment Upgrades (%): Primary to Tertiary
        result['n62'] = self.next(float)  # Distribution of Treatment Upgrades (%): Secondary to Tertiary
        self.next(EOL)

        # Line 114: (BMP Load Reduction Efficiencies)
        result['n63'] = self.next(float)  # BMP 1 (Nitrogen)
        result['n64'] = self.next(float)  # Vegetated Buffer Strips (Nitrogen)
        result['n65'] = self.next(float)  # BMP 2 (Nitrogen)
        result['n66'] = self.next(float)  # BMP 3 (Nitrogen)
        result['n66b'] = self.next(float)  # BMP 4 (Nitrogen)
        result['n67'] = self.next(float)  # BMP 5 (Nitrogen)
        result['n68'] = self.next(float)  # BMP 8 (Nitrogen)
        result['n68b'] = self.next(float)  # BMP 7 (Nitrogen)
        result['n69'] = self.next(float)  # Streambank Fencing (Nitrogen)
        result['n69b'] = self.next(float)  # Constructed Wetlands (Nitrogen)
        result['n69c'] = self.next(float)  # Streambank Stabilization (Nitrogen)
        result['n70'] = self.next(float)  # BMP 6 (Nitrogen)
        result['n70b'] = self.next(float)  # Detention Basins (Nitrogen)
        self.next(EOL)

        # Line 115: (BMP Load Reduction Efficiencies cont.)
        result['n71'] = self.next(float)  # BMP 1 (Phosphorus)
        result['n71b'] = self.next(float)  # Bioretention Areas (Nitrogen)
        result['n72'] = self.next(float)  # Vegetated Buffer Strips (Phosphorus)
        result['n73'] = self.next(float)  # BMP 2 (Phosphorus)
        result['n74'] = self.next(float)  # BMP 3 (Phosphorus)
        result['n74b'] = self.next(float)  # BMP 4 (Phosphorus)
        result['n75'] = self.next(float)  # BMP 5 (Phosphorus)
        result['n76'] = self.next(float)  # BMP 8 (Phosphorus)
        result['n76b'] = self.next(float)  # BMP 7 (Phosphorus)
        result['n77'] = self.next(float)  # Streambank Fencing (Phosphorus)
        result['n77b'] = self.next(float)  # Constructed Wetlands (Phosphorus)
        result['n77c'] = self.next(float)  # Streambank Stabilization (Phosphorus)
        result['n78'] = self.next(float)  # BMP 6 (Phosphorus)
        result['n78b'] = self.next(float)  # Detention Basins (Phosphorus)
        self.next(EOL)

        # Line 116: (BMP Load Reduction Efficiencies cont.)
        result['n79'] = self.next(float)  # BMP 1 (Sediment)
        result['n79b'] = self.next(float)  # Bioretention Areas (Phosphorus)
        result['n79c'] = self.next(float)  # Bioretention Areas (Sediment)
        result['n80'] = self.next(float)  # Vegetated Buffer Strips (Sediment)
        result['n81'] = self.next(float)  # BMP 2 (Sediment)
        result['n82'] = self.next(float)  # BMP 3 (Sediment)
        result['n82b'] = self.next(float)  # BMP 4 (Sediment)
        result['n83'] = self.next(float)  # BMP 5 (Sediment)
        result['n84'] = self.next(float)  # BMP 8 (Sediment)
        result['n84b'] = self.next(float)  # BMP 7 (Sediment)
        result['n85'] = self.next(float)  # Streambank Fencing (Sediment)
        result['n85b'] = self.next(float)  # Constructed Wetlands (Sediment)
        result['n85c'] = self.next(float)  # Detention Basins (Sediment)
        result['n85d'] = self.next(float)  # Streambank Stabilization (Sediment)
        result['n85e'] = self.next(float)  # Unpaved Road (kg/meter) (Nitrogen)
        result['n85f'] = self.next(float)  # Unpaved Road (kg/meter) (Phosphorus)
        result['n85g'] = self.next(float)  # Unpaved Road (kg/meter) (Sediment)
        self.next(EOL)

        # Line 117: (BMP Load Reduction Efficiencies cont.)
        result['n85h'] = self.next(float)  # AWMS (Livestock) (Nitrogen)
        result['n85i'] = self.next(float)  # AWMS (Livestock) (Phosphorus)
        result['n85j'] = self.next(float)  # AWMS (Poultry) (Nitrogen)
        result['n85k'] = self.next(float)  # AWMS (Poultry) (Phosphorus)
        result['n85l'] = self.next(float)  # Runoff Control (Nitrogen)
        result['n85m'] = self.next(float)  # Runoff Control (Phosphorus)
        result['n85n'] = self.next(float)  # Phytase in Feed (Phosphorus)
        result['n85o'] = self.next(float)  # Vegetated Buffer Strips (Pathogens)
        result['n85p'] = self.next(float)  # Streambank Fencing (Pathogens)
        result['n85q'] = self.next(float)  # AWMS (Livestock) (Pathogens)
        result['n85r'] = self.next(float)  # AWMS (Poultry) (Pathogens)
        result['n85s'] = self.next(float)  # Runoff Control (Pathogens)
        result['n85t'] = self.next(float)  # Constructed Wetlands (Pathogens)
        result['n85u'] = self.next(float)  # Bioretention Areas (Pathogens)
        result['n85v'] = self.next(float)  # Detention Basins (Pathogens)
        self.next(EOL)

        # Line 118: (Wastewater Discharge BMP Reduction Efficiencies)
        result['n86'] = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Nitrogen)
        result['n87'] = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Nitrogen)
        result['n88'] = self.next(float)  # Conversion of Primary System to Secondary Treatment Plant (Nitrogen)
        result['n89'] = self.next(float)  # Conversion of Primary System to Tertiary Treatment Plant (Nitrogen)
        result['n90'] = self.next(float)  # Conversion of Secondary System to Tertiary Treatment Plant (Nitrogen)
        result['n91'] = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Phosphorus)
        result['n92'] = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Phosphorus)
        result['n93'] = self.next(float)  # Conversion of Primary System to Secondary Treatment Plant (Phosphorus)
        result['n94'] = self.next(float)  # Conversion of Primary System to Tertiary Treatment Plant (Phosphorus)
        result['n95'] = self.next(float)  # Conversion of Secondary System to Tertiary Treatment Plant (Phosphorus)
        result['n95b'] = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Pathogens)
        result['n95c'] = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Pathogens)
        result['n95d'] = self.next(float)  # Wastewater Treatment Plants Pathogen Distribution (cfu/100mL): Existing
        result['n95e'] = self.next(float)  # Wastewater Treatment Plants Pathogen Distribution (cfu/100mL): Future
        self.next(EOL)

        # Line 119: (BMP Costs $)
        result['n96'] = self.next(float)  # Conservation Tillage (per Ha)
        result['n97'] = self.next(float)  # Cover Crops (per Ha)
        result['n98'] = self.next(float)  # Grazing Land Management (per Ha)
        result['n99'] = self.next(float)  # Streambank Fencing (per km)
        result['n99b'] = self.next(float)  # Strip Cropping/Contour Farming (per Ha)
        result['n99c'] = self.next(float)  # Constructed Wetlands (per impervious Ha drained)
        result['n99d'] = self.next(float)  # Streambank Stabilization (per meter)
        result['n99e'] = self.next(float)  # Bioretention Areas (per impervious Ha drained)
        result['n100'] = self.next(float)  # Vegetated Buffer Strip (per Km)
        result['n101'] = self.next(float)  # Agricultural Land Retirement (per Ha)
        result['n101b'] = self.next(float)  # AWMS/Livestock (per AEU)
        result['n101c'] = self.next(float)  # AWMS/Poultry (per AEU)
        result['n101d'] = self.next(float)  # Runoff Control (per AEU)
        result['n101e'] = self.next(float)  # Phytase in Feed (per AEU)
        result['n102'] = self.next(float)  # Nutrient Management (per Ha)
        result['n103a'] = self.next(float)  # User Defined (per Ha)
        result['n103b'] = self.next(float)  # Detention Basins (per impervious Ha drained)
        result['n103c'] = self.next(float)  # Conservation Plan (per Ha)
        result['n103d'] = self.next(float)  # Unpaved Roads (per meter)
        self.next(EOL)

        # Line 120:
        result['n104'] = self.next(float)  # BMP Costs $: Conversion of Septic Systems to Centralized Sewage Treatment (per home)
        result['n105'] = self.next(float)  # BMP Costs $: Conversion from Primary to Secondary Sewage Treatment (per capita)
        result['n106'] = self.next(float)  # BMP Costs $: Conversion from Primary to Tertiary Sewage Treatment (per capita)
        result['n106b'] = self.next(float)  # No longer used (Default = 0)
        result['n106c'] = self.next(float)  # No longer used (Default = 0)
        result['n106d'] = self.next(float)  # No longer used (Default = 0)
        result['n107'] = self.next(float)  # BMP Costs $: Conversion from Secondary to Tertiary Sewage Treatment (per capita)
        result['n107b'] = self.next(float)  # No longer used (Default = 0)
        result['n107c'] = self.next(float)  # No longer used (Default = 0)
        result['n107d'] = self.next(float)  # No longer used (Default = 0)
        result['n107e'] = self.next(float)  # No longer used (Default = 0)
        result['Storm'] = self.next(float)  # CSN Tool: Storm Event Simulated (cm)
        result['CSNAreaSim'] = self.next(float)  # CSN Tool: Area Simulated (Ha)
        result['CSNDevType'] = self.next(str)  # CSN Tool: Development Type
        self.next(EOL)

        # Line 121:
        result['Qretention'] = self.next(float)  # Detention Basin: Amount of runoff retention (cm)
        result['FilterWidth'] = self.next(float)  # Stream Protection: Vegetative buffer strip width (meters)
        result['Capacity'] = self.next(float)  # Detention Basin: Detention basin volume (cubic meters)
        result['BasinDeadStorage'] = self.next(float)  # Detention Basin: Basin dead storage (cubic meters)
        result['BasinArea'] = self.next(float)  # Detention Basin: Basin surface area (square meters)
        result['DaysToDrain'] = self.next(float)  # Detention Basin: Basin days to drain
        result['CleanMon'] = self.next(float)  # Detention Basin: Basin cleaning month
        result['PctAreaInfil'] = self.next(float)  # Infiltration/Bioretention: Fraction of area treated (0-1)
        result['PctStrmBuf'] = self.next(float)  # Stream Protection: Fraction of streams treated (0-1)
        result['UrbBankStab'] = self.next(float)  # Stream Protection: Streams w/bank stabilization (km)
        result['ISRR(0)'] = self.next(float)  # Impervious Surface Reduction: Low Density Mixed (% Reduction)
        result['ISRA(0)'] = self.next(float)  # Impervious Surface Reduction: Low Density Mixed (% Area)
        result['ISRR(1)'] = self.next(float)  # Impervious Surface Reduction: Medium Density Mixed (% Reduction)
        result['ISRA(1)'] = self.next(float)  # Impervious Surface Reduction: Medium Density Mixed (% Area)
        result['ISRR(2)'] = self.next(float)  # Impervious Surface Reduction: High Density Mixed (% Reduction)
        result['ISRA(2)'] = self.next(float)  # Impervious Surface Reduction: High Density Mixed (% Area)
        result['ISRR(3)'] = self.next(float)  # Impervious Surface Reduction: Low Density Residential (% Reduction)
        result['ISRA(3)'] = self.next(float)  # Impervious Surface Reduction: Low Density Residential (% Area)
        result['ISRR(4)'] = self.next(float)  # Impervious Surface Reduction: Medium Density Residential (% Reduction)
        result['ISRA(4)'] = self.next(float)  # Impervious Surface Reduction: Medium Density Residential (% Area)
        result['ISRR(5)'] = self.next(float)  # Impervious Surface Reduction: High Density Residential (% Reduction)
        result['ISRA(5)'] = self.next(float)  # Impervious Surface Reduction: High Density Residential (% Area)
        result['SweepType'] = self.next(float)  # Street Sweeping: Sweep Type (1-2)
        result['UrbSweepFrac'] = self.next(float)  # Street Sweeping: Fraction of area treated (0-1)
        self.next(EOL)

        # Lines 122 - 133: (Street Sweeping data for each Month)
        for i in range(12):
            result['StreetSweepNo'].append(self.next(float))  # Street sweeping times per month
            self.next(EOL)

        # Line 134:
        result['OutName'] = self.next(str)  # PRedICT Output Name
        self.next(EOL)

        # Line 135: (Estimated Reduced Load)
        result['n108'] = self.next(float)  # Row Crops: Sediment (kg x 1000)
        result['n109'] = self.next(float)  # Row Crops: Nitrogen (kg)
        result['n110'] = self.next(float)  # Row Crops: Phosphorus (kg)
        self.next(EOL)

        # Line 136: (Estimated Reduced Load)
        result['n111'] = self.next(float)  # Hay/Pasture: Sediment (kg x 1000)
        result['n111b'] = self.next(float)  # High Density Urban: Sediment (kg x 1000)
        result['n111c'] = self.next(float)  # Low Density Urban: Sediment (kg x 1000)
        result['n111d'] = self.next(float)  # Unpaved Roads: Sediment (kg x 1000)
        result['n112'] = self.next(float)  # Hay/Pasture: Nitrogen (kg)
        result['n112b'] = self.next(float)  # High Density Urban: Nitrogen (kg)
        result['n112c'] = self.next(float)  # Low Density Urban: Nitrogen (kg)
        result['n112d'] = self.next(float)  # Unpaved Roads: Nitrogen (kg)
        result['n113'] = self.next(float)  # Hay/Pasture: Phosphorus (kg)
        result['n113b'] = self.next(float)  # High Density Urban: Phosphorus (kg)
        result['n113c'] = self.next(float)  # Low Density Urban: Phosphorus (kg)
        result['n113d'] = self.next(float)  # Unpaved Roads: Phosphorus (kg)
        self.next(EOL)

        # Line 137: (Estimated Reduced Load)
        result['n114'] = self.next(float)  # Other: Sediment (kg x 1000)
        result['n115'] = self.next(float)  # Other: Nitrogen (kg)
        result['n115b'] = self.next(float)  # Farm Animals: Nitrogen (kg)
        result['n116'] = self.next(float)  # Other: Phosphorus (kg)
        result['n116b'] = self.next(float)  # Farm Animals: Phosphorus (kg)
        self.next(EOL)

        # Line 138: (Estimated Reduced Load)
        result['n117'] = self.next(float)  # Streambank Erosion: Sediment (kg x 1000)
        result['n118'] = self.next(float)  # Streambank Erosion: Nitrogen (kg)
        result['n119'] = self.next(float)  # Streambank Erosion: Phosphorus (kg)
        self.next(EOL)

        # Line 139: (Estimated Reduced Load)
        result['n120'] = self.next(float)  # Groundwater/Subsurface: Nitrogen (kg)
        result['n121'] = self.next(float)  # Groundwater/Subsurface: Phosphorus (kg)
        self.next(EOL)

        # Line 140: (Estimated Reduced Load)
        result['n122'] = self.next(float)  # Point Source Discharges: Nitrogen (kg)
        result['n123'] = self.next(float)  # Point Source Discharges: Phosphorus (kg)
        self.next(EOL)

        # Line 141: (Estimated Reduced Load)
        result['n124'] = self.next(float)  # Septic Systems: Nitrogen (kg)
        result['n125'] = self.next(float)  # Septic Systems: Phosphorus (kg)
        self.next(EOL)

        # Line 142: (Estimated Reduced Load)
        result['n126'] = self.next(float)  # Total: Sediment (kg x 1000)
        result['n127'] = self.next(float)  # Total: Nitrogen (kg)
        result['n128'] = self.next(float)  # Total: Phosphorus (kg)
        self.next(EOL)

        # Line 143: (Estimated Reduced Load)
        result['n129'] = self.next(float)  # Percent Reduction: Sediment (%)
        result['n130'] = self.next(float)  # Percent Reduction: Nitrogen (%)
        result['n131'] = self.next(float)  # Percent Reduction: Phosphorus (%)
        self.next(EOL)

        # Line 144:
        result['n132'] = self.next(float)  # Estimated Scenario Cost $: Total
        result['n133'] = self.next(float)  # Estimated Scenario Cost $: Agricultural BMPs
        result['n134'] = self.next(float)  # Estimated Scenario Cost $: Waste Water Upgrades
        result['n135'] = self.next(float)  # Estimated Scenario Cost $: Urban BMPs
        result['n136'] = self.next(float)  # Estimated Scenario Cost $: Stream Protection
        result['n137'] = self.next(float)  # Estimated Scenario Cost $: Unpaved Road Protection
        result['n138'] = self.next(float)  # Estimated Scenario Cost $: Animal BMPs
        result['n139'] = self.next(float)  # Pathogen Loads (Farm Animals): Existing (orgs/month)
        result['n140'] = self.next(float)  # Pathogen Loads (Wastewater Treatment Plants): Existing (orgs/month)
        self.next(EOL)

        # Line 145:
        result['n141'] = self.next(float)  # Pathogen Loads (Septic Systems): Existing (orgs/month)
        result['n142'] = self.next(float)  # Pathogen Loads (Urban Areas): Existing (orgs/month)
        result['n143'] = self.next(float)  # Pathogen Loads (Wildlife): Existing (orgs/month)
        result['n144'] = self.next(float)  # Pathogen Loads (Total): Existing (orgs/month)
        result['n145'] = self.next(float)  # Pathogen Loads (Farm Animals): Future (orgs/month)
        result['n146'] = self.next(float)  # Pathogen Loads (Wastewater Treatment Plants): Future (orgs/month)
        result['n147'] = self.next(float)  # Pathogen Loads (Septic Systems): Future (orgs/month)
        result['n148'] = self.next(float)  # Pathogen Loads (Urban Areas): Future (orgs/month)
        result['n149'] = self.next(float)  # Pathogen Loads (Wildlife): Future (orgs/month)
        result['n150'] = self.next(float)  # Pathogen Loads (Total): Future (orgs/month)
        result['n151'] = self.next(float)  # Pathogen Loads: Percent Reduction (%)
        self.next(EOL)

        # Line 146:
        result['InitNgN'] = self.next(float)  # Initial Non-Grazing Animal Totals: Nitrogen (kg/yr)
        result['InitNgP'] = self.next(float)  # Initial Non-Grazing Animal Totals: Phosphorus (kg/yr)
        result['InitNgFC'] = self.next(float)  # Initial Non-Grazing Animal Totals: Fecal Coliforms (orgs/yr)
        result['NGAppSum'] = self.next(float)  # Non-Grazing Manure Data Check: Land Applied (%)
        result['NGBarnSum'] = self.next(float)  # Non-Grazing Manure Data Check: In Confined Areas (%)
        result['NGTotSum'] = self.next(float)  # Non-Grazing Manure Data Check: Total (<= 1)
        result['InitGrN'] = self.next(float)  # Initial Grazing Animal Totals: Nitrogen (kg/yr)
        result['InitGrP'] = self.next(float)  # Initial Grazing Animal Totals: Phosphorus (kg/yr)
        result['InitGrFC'] = self.next(float)  # Initial Grazing Animal Totals: Fecal Coliforms (orgs/yr)
        result['GRAppSum'] = self.next(float)  # Grazing Manure Data Check: Land Applied (%)
        result['GRBarnSum'] = self.next(float)  # Grazing Manure Data Check: In Confined Areas (%)
        result['GRTotSum'] = self.next(float)  # Grazing Manure Data Check: Total (<= 1)
        result['AnimalFlag'] = self.next(YesOrNo.parse)  # Flag: Animal Layer Detected (0 No; 1 Yes)
        self.next(EOL)

        # Line 147:
        result['WildOrgsDay'] = self.next(float)  # Wildlife Loading Rate (org/animal/per day)
        result['WildDensity'] = self.next(float)  # Wildlife Density (animals/square mile)
        result['WuDieoff'] = self.next(float)  # Wildlife/Urban Die-Off Rate
        result['UrbEMC'] = self.next(float)  # Urban EMC (org/100ml)
        result['SepticOrgsDay'] = self.next(float)  # Septic Loading Rate (org/person per day)
        result['SepticFailure'] = self.next(float)  # Malfunctioning System Rate (0 - 1)
        result['WWTPConc'] = self.next(float)  # Wastewater Treatment Plants Loading Rate (cfu/100ml)
        result['InstreamDieoff'] = self.next(float)  # In-Stream Die-Off Rate
        result['AWMSGrPct'] = self.next(float)  # Animal Waste Management Systems: Livestock (%)
        result['AWMSNgPct'] = self.next(float)  # Animal Waste Management Systems: Poultry (%)
        result['RunContPct'] = self.next(float)  # Runoff Control (%)
        result['PhytasePct'] = self.next(float)  # Phytase in Feed (%)
        self.next(EOL)

        # Line 148-156: (For each Animal type)
        # TODO: Where is the number of animal types defined?
        for i in range(9):
            result['AnimalName'].append(self.next(str))  # Animal Name
            result['NumAnimals'].append(self.next(int))  # Number of Animals
            result['GrazingAnimal'].append(self.next(YesOrNo.parse))  # Flag: Grazing Animal (“N” No, “Y” Yes)
            result['AvgAnimalWt'].append(self.next(float))  # Average Animal Weight (kg)
            result['AnimalDailyN'].append(self.next(float))  # Animal Daily Loads: Nitrogen (kg/AEU)
            result['AnimalDailyP'].append(self.next(float))  # Animal Daily Loads: Phosphorus (kg/AEU)
            result['FCOrgsPerDay'].append(self.next(float))  # Fecal Coliforms (orgs/day)
            self.next(EOL)

        # Line 157-168: (For each month: Non-Grazing Animal Worksheet values)
        for i in range(12):
            # Month is already populated on lines 8 - 19
            self.next(str)  # Month (Jan-Dec)
            result['NGPctManApp'].append(self.next(float))  # Manure Spreading: % Of Annual Load Applied To Crops/Pasture
            result['NGAppNRate'].append(self.next(float))  # Manure Spreading: Base Nitrogen Loss Rate
            result['NGAppPRate'].append(self.next(float))  # Manure Spreading: Base Phosphorus Loss Rate
            result['NGAppFCRate'].append(self.next(float))  # Manure Spreading: Base Fecal Coliform Loss Rate
            result['NGPctSoilIncRate'].append(self.next(float))  # Manure Spreading: % Of Manure Load Incorporated Into Soil
            result['NGBarnNRate'].append(self.next(float))  # Barnyard/Confined Area: Base Nitrogen Loss Rate
            result['NGBarnPRate'].append(self.next(float))  # Barnyard/Confined Area: Base Phosphorus Loss Rate
            result['NGBarnFCRate'].append(self.next(float))  # Barnyard/Confined Area: Base Fecal Coliform Loss Rate
            self.next(EOL)

        # Line 169-180: (For each month: Grazing Animal Worksheet values)
        for i in range(12):
            # Month is already populated on lines 8 - 19
            self.next(str)  # Month (Jan-Dec)
            result['PctGrazing'].append(self.next(float))  # Grazing Land: % Of Time Spent Grazing
            result['PctStreams'].append(self.next(float))  # Grazing Land: % Of Time Spent In Streams
            result['GrazingNRate'].append(self.next(float))  # Grazing Land: Base Nitrogen Loss Rate
            result['GrazingPRate'].append(self.next(float))  # Grazing Land: Base Phosphorus Loss Rate
            result['GrazingFCRate'].append(self.next(float))  # Grazing Land: Base Fecal Coliform Loss Rate
            result['GRPctManApp'].append(self.next(float))  # Manure Spreading: % Of Annual Load Applied To Crops/Pasture
            result['GRAppNRate'].append(self.next(float))  # Manure Spreading: Base Nitrogen Loss Rate
            result['GRAppPRate'].append(self.next(float))  # Manure Spreading: Base Phosphorus Loss Rate
            result['GRAppFCRate'].append(self.next(float))  # Manure Spreading: Base Fecal Coliform Loss Rate
            result['GRPctSoilIncRate'].append(self.next(float))  # Manure Spreading: % Of Manure Load Incorporated Into Soil
            result['GRBarnNRate'].append(self.next(float))  # Barnyard/Confined Area: Base Nitrogen Loss Rate
            result['GRBarnPRate'].append(self.next(float))  # Barnyard/Confined Area: Base Phosphorus Loss Rate
            result['GRBarnFCRate'].append(self.next(float))  # Barnyard/Confined Area: Base Fecal Coliform Loss Rate
            self.next(EOL)

        # Line 181: (Nutrient Retention data)
        result['ShedAreaDrainLake'] = self.next(float)  # Percentage of watershed area that drains into a lake or wetlands: (0 - 1)
        result['RetentNLake'] = self.next(float)  # Lake Retention Rate: Nitrogen
        result['RetentPLake'] = self.next(float)  # Lake Retention Rate: Phosphorus
        result['RetentSedLake'] = self.next(float)  # Lake Retention Rate: Sediment
        result['AttenFlowDist'] = self.next(float)  # Attenuation: Flow Distance (km)
        result['AttenFlowVel'] = self.next(float)  # Attenuation: Flow Velocity (km/hr)
        result['AttenLossRateN'] = self.next(float)  # Attenuation: Loss Rate: Nitrogen
        result['AttenLossRateP'] = self.next(float)  # Attenuation: Loss Rate: Phosphorus
        result['AttenLossRateTSS'] = self.next(float)  # Attenuation: Loss Rate: Total Suspended Solids
        result['AttenLossRatePath'] = self.next(float)  # Attenuation: Loss Rate: Pathogens
        result['StreamFlowVolAdj'] = self.next(float)  # Streamflow Volume Adjustment Factor
        self.next(EOL)

        # Line 182 – Last Weather Day: (Weather data)
        for year in range(result['WxYrs']):
            result['DaysMonth'].append([])
            result['WxMonth'].append([])
            result['WxYear'].append([])

            result['Temp'].append([])
            result['Prec'].append([])

            for month in range(12):
                num_days = self.next(int)
                result['DaysMonth'][year].append(num_days)  # Days
                result['WxMonth'][year].append(self.next(str))  # Month (Jan-Dec)
                result['WxYear'][year].append(self.next(int))  # Year
                self.next(EOL)

                result['Temp'][year].append([])
                result['Prec'][year].append([])

                for day in range(num_days):
                    result['Temp'][year][month].append(self.next(int))  # Average Temperature (C)
                    result['Prec'][year][month].append(self.next(float))  # Precipitation (cm)
                    self.next(EOL)

        # Line Beginning After Weather: (Urban Area data)
        result['NumUAs'] = self.next(int)  # Number of Urban Areas
        result['UABasinArea'] = self.next(float)  # Urban Area Basin Area (Ha)
        self.next(EOL)

        # Lines if Number of Urban Areas > 0: (for each Urban Area)
        for ua in range(result['NumUAs']):
            # Line 1:
            result['UAId'].append(self.next(int))  # Urban Area ID
            result['UAName'].append(self.next(str))  # Urban Area Name
            result['UAArea'].append(self.next(float))  # Urban Area Area (Ha)
            self.next(EOL)

            result['UALU'].append([])
            result['UALUArea'].append([])

            # +1 for "Water"
            num_land_use_categories = result['NRur'] + result['NUrb'] + 1

            # Lines 2 - 17: (For each Land Use Category)
            for i in range(num_land_use_categories):
                result['UALU'][ua].append(self.next(LandUse.parse))  # Land Use Category
                result['UALUArea'][ua].append(self.next(float))  # Urban Land Use Area (Ha)
                self.next(EOL)

            # Line 18:
            result['UAfa'].append(self.next('Farm Animals'))
            result['UAfaAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

            # Line 19:
            result['UATD'].append(self.next('Tile Drainage'))
            result['UATDAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

            # Line 20:
            result['UASB'].append(self.next('Stream Bank'))
            result['UASBAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

            # Line 21:
            result['UAGW'].append(self.next('Groundwater'))
            result['UAGWAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

            # Line 22:
            result['UAPS'].append(self.next('Point Sources'))
            result['UAPSAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

            # Line 23:
            result['UASS'].append(self.next('Septic Systems'))
            result['UASSAreaFrac'].append(self.next(float))  # Area Fraction
            self.next(EOL)

        return result

    def next(self, typ):
        """
        Pop the next token and cast it using the given callable function
        or type. If a scalar value is passed instead, assert that the
        next token value matches and raise a ValueError if it does not.
        """
        value, line_no, col_no = self.fp.next()

        if callable(typ):
            try:
                return typ(value)
            except ValueError:
                log.error('Unexpected token at Line {} Column {}'.format(line_no, col_no))
                raise

        if typ != value:
            raise ValueError('Expected "{}" but got "{}" at Line {} Column {}'.format(typ, value, line_no, col_no))

        return value


if __name__ == '__main__':
    import sys
    import json

    ch = logging.StreamHandler()
    log.addHandler(ch)

    gms_filename = sys.argv[1]

    fp = open(gms_filename, 'r')
    gms = GmsReader(fp).read()

    print(json.dumps(gms))
