# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import csv
import logging
import re

from numpy import zeros

from .AFOS.GrazingAnimals.Loads.InitGrN import InitGrN_f
from .AFOS.GrazingAnimals.Losses.GRLBN_2 import GRLBN_2
from .AFOS.GrazingAnimals.Losses.GRStreamN import AvGRStreamN_f
from .AFOS.nonGrazingAnimals.Loads.InitNgN import InitNgN_f
from .AFOS.nonGrazingAnimals.Losses.NGLostBarnNSum import NGLostBarnNSum
from .Input.WaterBudget.AntMoist import AntMoist
from .Input.WaterBudget.SatStorCarryOver import SatStorCarryOver_f
from .Input.WaterBudget.UnSatStorCarryover import UnSatStorCarryover_f
from .MultiUse_Fxns.Runoff.CNI import CNI_f
from .MultiUse_Fxns.Runoff.CNP import CNP_f
from .Output.AvAnimalNSum.N7b_2 import N7b_2
from .datamodel import DataModel
from .enums import YesOrNo, ETflag, GrowFlag, LandUse, SweepType

log = logging.getLogger(__name__)

EOL = '<EOL>'


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
        z = DataModel()

        # AFOs loss rate coefficients
        z.NgAWMSCoeffN = 0.14
        z.NgAWMSCoeffP = 0.14
        z.GrAWMSCoeffN = 0.75
        z.GrAWMSCoeffP = 0.75
        z.RunConCoeffN = 0.15
        z.RunConCoeffP = 0.15
        z.PhytaseCoeff = 0.16

        z.AvGRStreamFC = 0
        z.AvGRStreamP = 0
        z.d = zeros(12)
        z.KVD = zeros(12)
        z.CV = zeros(12)
        z.AreaE = zeros(16)
        z.KLSCP = zeros(16)
        z.UrbanNitr = zeros(16)
        z.UrbanPhos = zeros(16)
        z.AvStreamFlow = zeros(12)
        z.AvPrecipitation = zeros(12)
        z.AFON = zeros(12)
        z.AFOP = zeros(12)
        z.AvLoad = zeros((12, 3))
        z.AvLuLoad = zeros((16, 3))
        z.AvDisLoad = zeros((16, 3))
        z.AvLuDisLoad = zeros((16, 3))
        z.AvGroundNitr = zeros(12)
        z.AvGroundPhos = zeros(12)
        z.AvDisNitr = zeros(12)
        z.AvTotNitr = zeros(12)
        z.AvDisPhos = zeros(12)
        z.AvTotPhos = zeros(12)
        z.AvLuRunoff = zeros(16)
        z.AvLuErosion = zeros(16)
        z.AvLuSedYield = zeros(16)
        z.AvLuDisNitr = zeros(16)
        z.AvLuTotNitr = zeros(16)
        z.AvLuDisPhos = zeros(16)
        z.AvLuTotPhos = zeros(16)
        z.BSed = zeros(16)
        z.UrbanSed = zeros(16)
        z.UrbanErosion = zeros(16)
        z.QRunoff = zeros((16, 12))
        z.AgQRunoff = zeros((16, 12))
        z.DailyLoad = zeros((50, 12, 31))
        z.SepticsDay = zeros(12)
        z.MonthlyLoad = zeros((12, 31))

        # Declare the daily values as ReDimensional arrays in
        # to Pesticide components
        z.DayPondNitr = zeros((12, 31))
        z.DayPondPhos = zeros((12, 31))
        z.DayNormNitr = zeros((12, 31))
        z.DayNormPhos = zeros((12, 31))
        z.DayShortNitr = zeros((12, 31))
        z.DayShortPhos = zeros((12, 31))
        z.DayDischargeNitr = zeros((12, 31))
        z.DayDischargePhos = zeros((12, 31))
        z.PestAppMonth1 = zeros(16)
        z.PestAppYear1 = zeros(16)
        z.PestAppDate1 = zeros(16)
        z.PestAppMonth2 = zeros(16)
        z.PestAppYear2 = zeros(16)
        z.PestAppDate2 = zeros(16)
        z.PestShedName = zeros(12)
        z.PestCropArea = zeros(12)
        z.PestSoilBd = zeros(12)
        z.PestSoilAwc = zeros(12)
        z.PestSoilOm = zeros(12)
        z.PestCropName = zeros(12)
        z.PestName1 = zeros(16)
        z.PestRate1 = zeros(31)
        z.PestParamCarbon1 = zeros(16)
        z.PestParamWater1 = zeros(16)
        z.PestDecay1 = zeros(16)
        z.PestHalfLife1 = zeros(16)
        z.PestName2 = zeros(16)
        z.PestRate2 = zeros(31)
        z.PestParamCarbon2 = zeros(16)
        z.PestParamWater2 = zeros(16)
        z.PestDecay2 = zeros(16)
        z.PestHalfLife2 = zeros(16)
        z.AvStreamBankP = zeros(12)
        z.CropPercent = zeros(12)
        z.PestSoilAwcCm = zeros(12)

        # Tile Drainage and Flow Variables
        z.AvTileDrainN = zeros(12)
        z.AvTileDrainP = zeros(12)
        z.AvTileDrainSed = zeros(12)
        z.AvPtSrcFlow = zeros(12)

        # Calculated Values for Animal Feeding Operations
        z.NGLoadP = zeros(9)
        z.NGLoadFC = zeros(9)
        z.NGAccManAppP = zeros(12)
        z.NGAccManAppFC = zeros(12)
        z.NGAppManP = zeros(12)
        z.NGInitBarnP = zeros(12)
        z.NGAppManFC = zeros(12)
        z.NGInitBarnFC = zeros(12)

        z.GRLoadP = zeros(9)
        z.GRLoadFC = zeros(9)
        z.GRAccManAppP = zeros(12)
        z.GRAccManAppFC = zeros(12)
        z.GRAppManP = zeros(12)
        z.GRInitBarnP = zeros(12)
        z.GRAppManFC = zeros(12)
        z.GRInitBarnFC = zeros(12)
        z.GrazingP = zeros(12)
        z.GrazingFC = zeros(12)
        z.GRStreamN = zeros(12)
        z.GRStreamP = zeros(12)
        z.GRStreamFC = zeros(12)
        z.AvAnimalP = zeros(12)
        z.AvAnimalFC = zeros(12)
        z.AvWWOrgs = zeros(12)
        z.AvSSOrgs = zeros(12)
        z.AvUrbOrgs = zeros(12)
        z.AvWildOrgs = zeros(12)
        z.AvTotalOrgs = zeros(12)
        z.AvCMStream = zeros(12)
        z.AvOrgConc = zeros(12)
        z.AvGRLostBarnP = zeros(12)
        z.AvNGLostBarnP = zeros(12)
        z.AvNGLostManP = zeros(12)
        z.AvNGLostBarnFC = zeros(12)
        z.AvGRLostBarnFC = zeros(12)
        z.SweepFrac = zeros(12)

        z.q = 0
        z.k = 0
        z.OutFiltWidth = 0
        z.Clean = 0
        z.CleanSwitch = 0
        z.OutletCoef = 0
        z.BasinVol = 0
        z.Volume = 0
        z.ActiveVol = 0
        z.DetentFlow = 0
        z.AnnDayHrs = 0
        z.FrozenPondNitr = 0
        z.FrozenPondPhos = 0
        z.AvSeptNitr = 0
        z.AvSeptPhos = 0
        z.ForestAreaTotal = 0

        # Referenced in LoadReductions
        # Mostly initialized in PublicVariables.bas
        z.SMCheck = 'Both'
        z.n5dn = 0
        z.n12dp = 0
        z.n13dp = 0
        z.n6dn = 0
        z.n6bdn = 0
        z.n6cdn = 0
        z.n13bdp = 0
        z.n13cdp = 0
        z.RetentEff = 0

        # Line 1:
        z.NRur = self.next(int)  # Number of Rural Land Use Categories
        z.NUrb = self.next(int)  # Number Urban Land Use Categories
        z.BasinId = self.next(int)  # Basin ID
        self.next(EOL)

        # Line 2:
        z.TranVersionNo = self.next(str)  # GWLF-E Version
        z.RecessionCoef = self.next(float)  # Recession Coefficient
        z.SeepCoef = self.next(float)  # Seepage Coefficient
        z.UnsatStor_0 = self.next(float)  # Unsaturated Storage
        z.SatStor_0 = self.next(float)  # Saturated Storage
        z.InitSnow_0 = self.next(int)  # Initial Snow Days
        z.SedDelivRatio_0 = self.next(float)  # Sediment Delivery Ratio
        z.MaxWaterCap = self.next(float)  # Average Available Water Capacity
        z.StreamLength = self.next(float)  # Total Stream Length (meters)
        z.AgLength = self.next(float)  # Agricultural Stream Length (meters)
        z.UrbLength = self.next(float)  # Urban Stream Length (meters)
        z.AgSlope3 = self.next(float)  # Area of agricultural land with slope > 3%
        z.AgSlope3to8 = self.next(float)  # Area of agricultural land with slope > 3% and < 8%
        z.AvSlope = self.next(float)  # Average % Slope
        z.AEU = self.next(float)  # Number of Animal Units
        z.WxYrs = self.next(int)  # Total Weather Years
        z.WxYrBeg = self.next(int)  # Beginning Weather Year
        z.WxYrEnd = self.next(int)  # Ending Weather Year
        z.SedAFactor_0 = self.next(float)  # Sediment A Factor
        z.TotArea = self.next(float)  # Total Basin Area (Ha)
        z.TileDrainRatio = self.next(float)  # Tile Drain Ratio
        z.TileDrainDensity = self.next(float)  # Tile Drain Density
        z.ETFlag = self.next(ETflag.parse)  # ET Flag
        z.AvKF = self.next(float)  # Average K Factor
        self.next(EOL)

        z.NYrs = z.WxYrs
        # TODO: Remove DimYrs
        z.DimYrs = z.WxYrs

        z.UplandN = zeros((z.DimYrs, 12))
        z.UplandP = zeros((z.DimYrs, 12))
        z.UrbRunoffCm = zeros((z.DimYrs, 12))
        z.DailyFlowMGD = zeros((z.DimYrs, 12, 31))
        z.DailyPtSrcFlow = zeros((z.DimYrs, 12, 31))

        # Declare the daily values as ReDimensional arrays in
        # to Pesticide components
        z.DailyUplandSed = zeros((z.DimYrs, 12, 31))
        z.DailyUplandN = zeros((z.DimYrs, 12, 31))
        z.DailyUplandP = zeros((z.DimYrs, 12, 31))
        z.DailyTileDrainN = zeros((z.DimYrs, 12, 31))
        z.DailyTileDrainP = zeros((z.DimYrs, 12, 31))
        z.DailyStrmSed = zeros((z.DimYrs, 12, 31))
        z.DailySepticN = zeros((z.DimYrs, 12, 31))
        z.DailySepticP = zeros((z.DimYrs, 12, 31))
        z.DailyStrmN = zeros((z.DimYrs, 12, 31))
        z.DailyStrmP = zeros((z.DimYrs, 12, 31))
        z.DailyGroundN = zeros((z.DimYrs, 12, 31))
        z.DailyGroundP = zeros((z.DimYrs, 12, 31))
        z.DayGroundNitr = zeros((z.DimYrs, 12, 31))
        z.DayGroundPhos = zeros((z.DimYrs, 12, 31))
        z.DayDisPhos = zeros((z.DimYrs, 12, 31))
        z.DayDisNitr = zeros((z.DimYrs, 12, 31))
        z.DayTotNitr = zeros((z.DimYrs, 12, 31))
        z.DailyPointN = zeros((z.DimYrs, 12, 31))
        z.DailyPointP = zeros((z.DimYrs, 12, 31))
        z.DayTotPhos = zeros((z.DimYrs, 12, 31))
        z.DayLuTotN = zeros((16, z.DimYrs, 12, 31))
        z.DayLuTotP = zeros((16, z.DimYrs, 12, 31))
        z.DayLuDisN = zeros((16, z.DimYrs, 12, 31))
        z.DayLuDisP = zeros((16, z.DimYrs, 12, 31))
        z.DayErWashoff = zeros((16, z.DimYrs, 12, 31))
        z.Perc = zeros((z.DimYrs, 12, 31))
        z.DeepFlow = zeros((z.DimYrs, 12, 31))
        z.DayQRunoff = zeros((z.DimYrs, 12, 31))
        z.SdYld = zeros((z.DimYrs, 12, 31))
        z.Erosn = zeros((z.DimYrs, 12, 31))
        z.DayErosion = zeros((z.DimYrs, 12, 31))
        z.DayLuErosion = zeros((16, z.DimYrs, 12, 31))
        z.DaySed = zeros((z.DimYrs, 12, 31))
        z.DayLuSed = zeros((16, z.DimYrs, 12, 31))
        z.DayLuRunoff = zeros((16, z.DimYrs, 12, 31))
        z.PrecPest = zeros((z.DimYrs, 12, 31))
        z.DailyETCm = zeros((z.DimYrs, 12, 31))
        z.DailyETShal = zeros((z.DimYrs, 12, 31))
        z.PercShal = zeros((z.DimYrs, 12, 31))
        z.DailyUnsatStorCm = zeros((z.DimYrs, 12, 31))
        z.DailyUnsatStorShal = zeros((z.DimYrs, 12, 31))
        z.DailyET = zeros((z.DimYrs, 12, 31))
        z.DailyRetent = zeros((z.DimYrs, 12, 31))
        z.SatStorPest = zeros((z.DimYrs, 12, 31))
        z.DailyInfilt = zeros((z.DimYrs, 12, 31))
        z.StreamBankP = zeros((z.DimYrs, 12))
        z.LuGrFlow = zeros((16, z.DimYrs, 12, 31))
        z.LuDeepSeep = zeros((16, z.DimYrs, 12, 31))
        z.LuInfiltration = zeros((16, z.DimYrs, 12, 31))
        z.PestTemp = zeros((z.DimYrs, 12, 31))
        z.PestPrec = zeros((z.DimYrs, 12, 31))

        # Tile Drainage and Flow Variables
        z.TileDrainN = zeros((z.DimYrs, 12))
        z.TileDrainP = zeros((z.DimYrs, 12))
        z.TileDrainSed = zeros((z.DimYrs, 12))
        z.GroundNitr = zeros((z.DimYrs, 12))
        z.GroundPhos = zeros((z.DimYrs, 12))
        z.DisNitr = zeros((z.DimYrs, 12))
        z.SepticN = zeros((z.DimYrs, 12))
        z.SepticP = zeros((z.DimYrs, 12))
        z.TotNitr = zeros((z.DimYrs, 12))
        z.DisPhos = zeros((z.DimYrs, 12))
        z.TotPhos = zeros((z.DimYrs, 12))
        z.LuSedYield = zeros((z.DimYrs, 16))
        z.LuDisNitr = zeros((z.DimYrs, 16))
        z.LuTotNitr_2 = zeros((z.DimYrs, 16))
        z.LuDisPhos = zeros((z.DimYrs, 16))
        z.LuTotPhos_1 = zeros((z.DimYrs, 16))
        z.SepticNitr = zeros(z.DimYrs)
        z.SepticPhos = zeros(z.DimYrs)

        # ANIMAL FEEDING OPERATIONS VARIABLES
        z.DailyAnimalN = zeros((z.DimYrs, 12, 31))
        z.DailyAnimalP = zeros((z.DimYrs, 12, 31))

        # Calculated Values for Animal Feeding Operations
        z.NGLostManN = zeros((z.DimYrs, 12))
        z.NGLostBarnN = zeros((z.DimYrs, 12))
        z.NGLostManP = zeros((z.DimYrs, 12))
        z.NGLostBarnP = zeros((z.DimYrs, 12))
        z.NGLostManFC = zeros((z.DimYrs, 12))
        z.NGLostBarnFC = zeros((z.DimYrs, 12))

        z.GRLostBarnN = zeros((z.DimYrs, 12))
        z.GRLossN = zeros((z.DimYrs, 12))
        z.GRLostManP = zeros((z.DimYrs, 12))
        z.GRLostBarnP = zeros((z.DimYrs, 12))
        z.GRLossP = zeros((z.DimYrs, 12))
        z.GRLostManFC = zeros((z.DimYrs, 12))
        z.GRLostBarnFC = zeros((z.DimYrs, 12))
        z.GRLossFC = zeros((z.DimYrs, 12))
        z.AnimalP = zeros((z.DimYrs, 12))
        z.AnimalFC = zeros((z.DimYrs, 12))
        z.WWOrgs = zeros((z.DimYrs, 12))
        z.SSOrgs = zeros((z.DimYrs, 12))
        z.UrbOrgs = zeros((z.DimYrs, 12))
        z.WildOrgs = zeros((z.DimYrs, 12))
        z.TotalOrgs = zeros((z.DimYrs, 12))
        z.CMStream = zeros((z.DimYrs, 12))
        z.OrgConc = zeros((z.DimYrs, 12))

        z.StreamBankPSum = zeros(z.WxYrs)
        z.StreamBankErosSum = zeros(z.WxYrs)
        z.StreamBankPSum = zeros(z.WxYrs)
        z.GroundNitrSum = zeros(z.WxYrs)
        z.GroundPhosSum = zeros(z.WxYrs)
        z.TileDrainSum = zeros(z.WxYrs)
        z.TileDrainNSum = zeros(z.WxYrs)
        z.TileDrainPSum = zeros(z.WxYrs)
        z.TileDrainSedSum = zeros(z.WxYrs)
        z.AnimalNSum = zeros(z.WxYrs)
        z.AnimalPSum = zeros(z.WxYrs)
        z.AnimalFCSum = zeros(z.WxYrs)
        z.WWOrgsSum = zeros(z.WxYrs)
        z.SSOrgsSum = zeros(z.WxYrs)
        z.UrbOrgsSum = zeros(z.WxYrs)
        z.WildOrgsSum = zeros(z.WxYrs)
        z.TotalOrgsSum = zeros(z.WxYrs)
        z.GRLostBarnPSum = zeros(z.WxYrs)
        z.GRLostBarnFCSum = zeros(z.WxYrs)
        z.NGLostBarnPSum = zeros(z.WxYrs)
        z.NGLostBarnFCSum = zeros(z.WxYrs)
        z.NGLostManPSum = zeros(z.WxYrs)
        z.TotNitrSum = zeros(z.WxYrs)
        z.TotPhosSum = zeros(z.WxYrs)

        # Set the Total AEU to the value from the Animal Density layer
        if not self.version_match(z.TranVersionNo, '1.[0-9].[0-9]'):
            raise Exception('Input data file is not in the correct format or is no longer supported')

        # Lines 3 - 7: (each line represents 1 day)
        # Antecedent Rain + Melt Moisture Condition for Days 1 to 5
        z.AntMoist = zeros(5)
        z.AntMoist_0 = zeros(5)

        for i in range(5):
            z.AntMoist_0[i] = self.next(float)
            self.next(EOL)

        # Lines 8 - 19: (each line represents 1 month)
        z.Month = zeros(12, dtype=object)
        z.KV = zeros(12)
        z.DayHrs = zeros(12)
        z.Grow_0 = zeros(12, dtype=object)
        z.Acoef = zeros(12)
        z.StreamWithdrawal = zeros(12)
        z.GroundWithdrawal = zeros(12)
        z.PcntET = zeros(12)

        for i in range(12):
            z.Month[i] = self.next(str)  # Month (Jan - Dec)
            z.KV[i] = self.next(float)  # KET (Flow Factor)
            z.DayHrs[i] = self.next(float)  # Day Length (hours)
            z.Grow_0[i] = self.next(GrowFlag.parse)  # Growing season flag
            z.Acoef[i] = self.next(float)  # Erosion Coefficient
            z.StreamWithdrawal[i] = self.next(float)  # Surface Water Withdrawal/Extraction
            z.GroundWithdrawal[i] = self.next(float)  # Groundwater Withdrawal/Extraction
            z.PcntET[i] = self.next(float)  # Percent monthly adjustment for ET calculation
            self.next(EOL)

        # Lines 20 - 29: (for each Rural Land Use Category)
        for i in range(z.NRur):
            z.Landuse[i] = self.next(LandUse.parse)  # Rural Land Use Category
            z.Area[i] = self.next(float)  # Area (Ha)
            z.CN[i] = self.next(float)  # Curve Number
            z.KF[i] = self.next(float)  # K Factor
            z.LS[i] = self.next(float)  # LS Factor
            z.C[i] = self.next(float)  # C Factor
            z.P[i] = self.next(float)  # P Factor
            self.next(EOL)

        # Lines 30 - 35: (for each Urban Land Use Category)
        z.Imper = zeros(z.NLU)
        z.TotSusSolids = zeros(z.NLU)

        z.CNI_0 = zeros((3, z.NLU))
        z.CNP_0 = zeros((3, z.NLU))

        for i in range(z.NRur, z.NLU):
            z.Landuse[i] = self.next(LandUse.parse)  # Urban Land Use Category
            z.Area[i] = self.next(float)  # Area (Ha)
            z.Imper[i] = self.next(float)  # Impervious Surface %
            z.CNI_0[1][i] = self.next(float)  # Curve Number(Impervious Surfaces)
            z.CNP_0[1][i] = self.next(float)  # Curve Number(Pervious Surfaces)
            z.TotSusSolids[i] = self.next(float)  # Total Suspended Solids Factor
            self.next(EOL)

        # Line 36:
        z.PhysFlag = self.next(YesOrNo.parse)  # Physiographic Province Layer Detected
        z.PointFlag = self.next(YesOrNo.parse)  # Point Source Layer Detected
        z.SeptSysFlag = self.next(YesOrNo.parse)  # Septic System Layer Detected
        z.CountyFlag = self.next(YesOrNo.parse)  # County Layer Detected
        z.SoilPFlag = self.next(YesOrNo.parse)  # Soil P Layer Detected
        z.GWNFlag = self.next(YesOrNo.parse)  # Groundwater N Layer Detected
        z.SedAAdjust = self.next(float)  # Default Percent ET
        self.next(EOL)

        # Line 37:
        z.SedNitr = self.next(float)  # Soil Concentration: N (mg/l)
        z.SedPhos = self.next(float)  # Soil Concentration: P (mg/l)
        z.GrNitrConc = self.next(float)  # Groundwater Concentration: N (mg/l)
        z.GrPhosConc = self.next(float)  # Groundwater Concentration: P (mg/l)
        z.BankNFrac = self.next(float)  # % Bank N Fraction (0 - 1)
        z.BankPFrac = self.next(float)  # % Bank P Fraction (0 - 1)
        self.next(EOL)

        # Line 38:
        z.ManuredAreas = self.next(int)  # Manure Spreading Periods (Default = 2)
        z.FirstManureMonth = self.next(int)  # MS Period 1: First Month
        z.LastManureMonth = self.next(int)  # MS Period 1: Last Month
        z.FirstManureMonth2 = self.next(int)  # MS Period 2: First Month
        z.LastManureMonth2 = self.next(int)  # MS Period 2: Last Month
        self.next(EOL)

        # Convert 1-based indexes to 0-based.
        z.FirstManureMonth -= 1
        z.FirstManureMonth2 -= 1
        z.LastManureMonth -= 1
        z.LastManureMonth2 -= 1

        # Lines 39 - 48: (for each Rural Land Use Category)
        z.NitrConc = zeros(16)
        z.PhosConc = zeros(16)

        for i in range(z.NRur):
            z.NitrConc[i] = self.next(float)  # Dissolved Runoff Coefficient: N (mg/l)
            z.PhosConc[i] = self.next(float)  # Dissolved Runoff Coefficient: P (mg/l)
            self.next(EOL)

        # Line 49:
        z.Nqual = self.next(int)  # Number of Contaminants (Default = 3; Nitrogen, Phosphorus, Sediment)
        self.next(EOL)

        # Lines 50 - 52:
        z.Contaminant = zeros(z.Nqual, dtype=object)
        z.SolidBasinMass = zeros(z.Nqual)
        z.DisBasinMass = zeros(z.Nqual)

        for i in range(z.Nqual):
            z.Contaminant[i] = self.next(str)
            self.next(EOL)

        # Lines 53 - 58 (for each Urban Land Use Category, Nitrogen Contaminant)
        # Lines 59 - 64: (for each Urban Land Use Category, Phosphorus Contaminant)
        # Lines 65 - 70: (for each Urban Land Use Category, Sediment Contaminant)
        z.LoadRateImp = zeros((z.NLU, z.Nqual))
        z.LoadRatePerv = zeros((z.NLU, z.Nqual))
        z.DisFract = zeros((z.NLU, z.Nqual))
        z.UrbBMPRed = zeros((z.NLU, z.Nqual))

        for u in range(z.NRur, z.NLU):
            for q in range(z.Nqual):
                z.LoadRateImp[u][q] = self.next(float)  # Loading Rate Impervious Surface
                z.LoadRatePerv[u][q] = self.next(float)  # Loading Rate Pervious Surface
                z.DisFract[u][q] = self.next(float)  # Dissolved Fraction
                z.UrbBMPRed[u][q] = self.next(float)  # Urban BMP Reduction
                self.next(EOL)

        z.ManNitr = zeros(z.ManuredAreas)
        z.ManPhos = zeros(z.ManuredAreas)

        # Lines 71 - 72: (for the 2 Manure Spreading Periods)
        for i in range(z.ManuredAreas):
            z.ManNitr[i] = self.next(float)  # Manured N Concentration
            z.ManPhos[i] = self.next(float)  # Manured P Concentration
            self.next(EOL)

        # Lines 73 - 84: (Point Source data for each Month)
        z.PointNitr = zeros(12)
        z.PointPhos = zeros(12)
        z.PointFlow = zeros(12)

        for i in range(12):
            z.PointNitr[i] = self.next(float)  # N Load (kg)
            z.PointPhos[i] = self.next(float)  # P Load (kg)
            z.PointFlow[i] = self.next(float)  # Discharge (Millions of Gallons per Day)
            self.next(EOL)

        # Line 85:
        z.SepticFlag = self.next(YesOrNo.parse)  # Flag: Septic Systems Layer Detected (0 No; 1 Yes)
        self.next(EOL)

        # Lines 86 - 97: (Septic System data for each Month)
        for i in range(12):
            z.NumNormalSys[i] = self.next(int)  # Number of People on Normal Systems
            z.NumPondSys[i] = self.next(int)  # Number of People on Pond Systems
            z.NumShortSys[i] = self.next(int)  # Number of People on Short Circuit Systems
            z.NumDischargeSys[i] = self.next(int)  # Number of People on Discharge Systems
            z.NumSewerSys[i] = self.next(int)  # Number of People on Public Sewer Systems
            self.next(EOL)

        # Line 98: (if Septic System flag = 1)
        if z.SepticFlag == YesOrNo.YES:
            z.NitrSepticLoad = self.next(float)  # Per Capita Tank Load: N (g/d)
            z.PhosSepticLoad = self.next(float)  # Per Capita Tank Load: P (g/d)
            z.NitrPlantUptake = self.next(float)  # Growing System Uptake: N (g/d)
            z.PhosPlantUptake = self.next(float)  # Growing System Uptake: P (g/d)
            self.next(EOL)
        else:
            raise Exception('SepticFlag must be set to 1')

        # Line 99:
        z.TileNconc = self.next(float)  # Tile Drainage Concentration: N (mg/L)
        z.TilePConc = self.next(float)  # Tile Drainage Concentration: P (mg/L)
        z.TileSedConc = self.next(float)  # Tile Drainage Concentration: Sediment (mg/L)
        self.next(EOL)

        # Line 100: (variables passed through GWLF-E to PRedICT)
        z.InName = self.next(str)  # Scenario Run Name
        z.UnitsFileFlag = self.next(int)  # Units Flag (Default = 1)
        z.AssessDate = self.next(str)  # Assessment/Reference Date (mmyyyy)
        z.VersionNo = self.next(str)  # GWLF-E Version Number
        self.next(EOL)

        # Line 101: (variable passed through GWLF-E to PRedICT)
        z.ProjName = self.next(str)  # Project Name
        self.next(EOL)

        # Line 102: (Estimated Load by Land Use/Source – Total Sediment (kg x 1000))
        z.n1 = self.next(float)  # Row Crops
        z.n2 = self.next(float)  # Hay/Pasture
        z.n2b = self.next(float)  # High Density Urban
        z.n2c = self.next(float)  # Low Density Urban
        z.n2d = self.next(float)  # Unpaved Roads
        z.n3 = self.next(float)  # Other
        z.n4 = self.next(float)  # Streambank Erosion
        self.next(EOL)

        # Line 103: (Estimated Load by Land Use/Source – Total Nitrogen (kg))
        z.n5 = self.next(float)  # Row Crops
        z.n6 = self.next(float)  # Hay/Pasture
        z.n6b = self.next(float)  # High Density Urban
        z.n6c = self.next(float)  # Low Density Urban
        z.n6d = self.next(float)  # Unpaved Roads
        z.n7 = self.next(float)  # Other
        _ = self.next(float)  # Farm Animals
        z.n8 = self.next(float)  # Streambank Erosion
        z.n9 = self.next(float)  # Groundwater/Subsurface
        z.n10 = self.next(float)  # Point Source Discharges
        z.n11 = self.next(float)  # Septic Systems
        self.next(EOL)

        # Line 104: (Estimated Load by Land Use/Source – Total Phosphorus (kg))
        z.n12 = self.next(float)  # Row Crops
        z.n13 = self.next(float)  # Hay/Pasture
        z.n13b = self.next(float)  # High Density Urban
        z.n13c = self.next(float)  # Low Density Urban
        z.n13d = self.next(float)  # Unpaved Roads
        z.n14 = self.next(float)  # Other
        z.n14b = self.next(float)  # Farm Animals
        z.n15 = self.next(float)  # Streambank Erosion
        z.n16 = self.next(float)  # Groundwater/Subsurface
        z.n17 = self.next(float)  # Point Source Discharges
        z.n18 = self.next(float)  # Septic Systems
        self.next(EOL)

        # Line 105:
        z.n19 = self.next(float)  # Total Sediment Load (kg x 1000)
        z.n20 = self.next(float)  # Total Nitrogen Load (kg)
        z.n21 = self.next(float)  # Total Phosphorus Load (kg)
        z.n22 = self.next(float)  # Basin Area (Ha)
        self.next(EOL)

        # Line 106:
        z.n23 = self.next(float)  # Row Crops Area (Ha)
        z.n23b = self.next(float)  # High Density Urban Area (Ha)
        z.n23c = self.next(float)  # High Density Urban (Constructed Wetlands): % Drainage Used
        z.n24 = self.next(float)  # Hay/Pasture Area (Ha)
        z.n24b = self.next(float)  # Low Density Urban Area (ha Ha
        z.n24c = self.next(float)  # Low Density Urban (Constructed Wetlands): % Drainage Used
        z.n24d = self.next(float)  # High Density Urban (Bioretention Areas): % Drainage Used
        z.n24e = self.next(float)  # Low Density Urban (Bioretention Areas): % Drainage Used
        self.next(EOL)

        # Line 107:
        z.n25 = self.next(float)  # Row Crops (BMP 1): Existing (%)
        z.n25b = self.next(float)  # High Density Urban (Constructed Wetlands): Existing (%)
        z.n25c = self.next(float)  # Low Density Urban (Constructed Wetlands): Existing (%)
        z.n25d = self.next(float)  # High Density Urban (Bioretention Areas): Existing (%)
        z.n25e = self.next(float)  # Low Density Urban (Bioretention Areas): Existing (%)
        z.n26 = self.next(float)  # Row Crops (BMP 2): Existing (%)
        z.n26b = self.next(float)  # High Density Urban (Detention Basin): Existing (%)
        z.n26c = self.next(float)  # Low Density Urban (Detention Basin): Existing (%)
        z.n27 = self.next(float)  # Row Crops (BMP 3): Existing (%)
        z.n27b = self.next(float)  # Row Crops (BMP 4): Existing (%)
        z.n28 = self.next(float)  # Row Crops (BMP 5): Existing (%)
        z.n28b = self.next(float)  # Row Crops (BMP 6): Existing (%)
        z.n29 = self.next(float)  # Row Crops (BMP 8): Existing (%)
        self.next(EOL)

        # Line 108:
        z.n30 = self.next(float)  # Row Crops (BMP 1): Future (%)
        z.n30b = self.next(float)  # High Density Urban (Constructed Wetlands): Future (%)
        z.n30c = self.next(float)  # Low Density Urban (Constructed Wetlands): Future (%)
        z.n30d = self.next(float)  # High Density Urban (Bioretention Areas): Future (%)
        z.n30e = self.next(float)  # Low Density Urban (Bioretention Areas): Future (%)
        z.n31 = self.next(float)  # Row Crops (BMP 2): Future (%)
        z.n31b = self.next(float)  # High Density Urban (Detention Basin): Future (%)
        z.n31c = self.next(float)  # Low Density Urban (Detention Basin): Future (%)
        z.n32 = self.next(float)  # Row Crops (BMP 3): Future (%)
        z.n32b = self.next(float)  # Row Crops (BMP 4): Future (%)
        z.n32c = self.next(float)  # Hay/Pasture (BMP 3): Existing (%)
        z.n32d = self.next(float)  # Hay/Pasture (BMP 3): Future (%)
        z.n33 = self.next(float)  # Row Crops (BMP 5): Future (%)
        z.n33b = self.next(float)  # Row Crops (BMP 6): Future (%)
        z.n33c = self.next(float)  # Hay/Pasture (BMP 4): Existing (%)
        z.n33d = self.next(float)  # Hay/Pasture (BMP 4): Future (%)
        self.next(EOL)

        # Line 109:
        z.n34 = self.next(float)  # Row Crops (BMP 8): Future (%)
        z.n35 = self.next(float)  # Hay/Pasture (BMP 5): Existing (%)
        z.n35b = self.next(float)  # Hay/Pasture (BMP 6): Existing (%)
        z.n36 = self.next(float)  # Hay/Pasture (BMP 7): Existing (%)
        z.n37 = self.next(float)  # Hay/Pasture (BMP 8): Existing (%)
        z.n38 = self.next(float)  # Hay/Pasture (BMP 5): Future (%)
        z.n38b = self.next(float)  # Hay/Pasture (BMP 6): Future (%)
        z.n39 = self.next(float)  # Hay/Pasture (BMP 7): Future (%)
        z.n40 = self.next(float)  # Hay/Pasture (BMP 8): Future (%)
        self.next(EOL)

        # Line 110:
        z.n41 = self.next(float)  # Agricultural Land on Slope > 3% (Ha)
        z.n41b = self.next(float)  # AWMS (Livestock): Existing (%)
        z.n41c = self.next(float)  # AWMS (Livestock): Future (%)
        z.n41d = self.next(float)  # AWMS (Poultry): Existing (%)
        z.n41e = self.next(float)  # AWMS (Poultry): Future (%)
        z.n41f = self.next(float)  # Runoff Control: Existing (%)
        z.n41g = self.next(float)  # Runoff Control: Future (%)
        z.n41h = self.next(float)  # Phytase in Feed: Existing (%)
        z.n41i = self.next(float)  # Phytase in Feed: Future (%)
        z.n41j = self.next(float)  # Total Livestock AEUs
        z.n41k = self.next(float)  # Total Poultry AEUs
        z.n41l = self.next(float)  # Total AEUs
        z.n42 = self.next(float)  # Streams in Agricultural Areas (km)
        z.n42b = self.next(float)  # Total Stream Length (km)
        z.n42c = self.next(float)  # Unpaved Road Length (km)
        z.n43 = self.next(float)  # Stream Km with Vegetated Buffer Strips: Existing
        _ = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        _ = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        z.GRLBP = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        z.NGLBP = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        z.NGLManP = self.next(float)  # Average Non-Grazing Animal Loss Rate (Manure Spreading): Phosphorus
        z.NGLBFC = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        z.GRLBFC = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        z.GRSFC = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Fecal Coliform
        _ = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Nitrogen
        z.GRSP = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Phosphorus
        self.next(EOL)

        # Line 111:
        z.n43b = self.next(float)  # High Density Urban (Constructed Wetlands): Required Ha
        z.n43c = self.next(float)  # High Density Urban (Detention Basin): % Drainage Used
        z.n43d = self.next(float)  # High Density Urban: % Impervious Surface
        z.n43e = self.next(float)  # High Density Urban (Constructed Wetlands): Impervious Ha Drained
        z.n43f = self.next(float)  # High Density Urban (Detention Basin): Impervious Ha Drained
        z.n43g = self.next(float)  # High Density Urban (Bioretention Areas): Impervious Ha Drained
        z.n43h = self.next(float)  # High Density Urban (Bioretention Areas): Required Ha
        z.n43i = self.next(float)  # Low Density Urban (Bioretention Areas): Impervious Ha Drained
        z.n43j = self.next(float)  # Low Density Urban (Bioretention Areas): Required Ha
        z.n44 = self.next(float)  # Stream Km with Vegetated Buffer Strips: Future
        z.n44b = self.next(float)  # High Density Urban (Detention Basin): Required Ha
        z.n45 = self.next(float)  # Stream Km with Fencing: Existing
        z.n45b = self.next(float)  # Low Density Urban (Constructed Wetlands): Required Ha
        z.n45c = self.next(float)  # Low Density Urban (Detention Basin): % Drainage Used
        z.n45d = self.next(float)  # Low Density Urban: % Impervious Surface
        z.n45e = self.next(float)  # Low Density Urban (Constructed Wetlands): Impervious Ha Drained
        z.n45f = self.next(float)  # Low Density Urban (Detention Basin): Impervious Ha Drained
        self.next(EOL)

        # Line 112:
        z.n46 = self.next(float)  # Stream Km with Fencing: Future
        z.n46b = self.next(float)  # Low Density Urban (Detention Basin): Required Ha
        z.n46c = self.next(float)  # Stream Km with Stabilization: Existing
        z.n46d = self.next(float)  # Stream Km with Stabilization: Future
        z.n46e = self.next(float)  # Stream Km in High Density Urban Areas
        z.n46f = self.next(float)  # Stream Km in Low Density Urban Areas
        z.n46g = self.next(float)  # Stream Km in High Density Urban Areas W/Buffers: Existing
        z.n46h = self.next(float)  # Stream Km in High Density Urban Areas W/Buffers: Future
        z.n46i = self.next(float)  # High Density Urban Streambank Stabilization (km): Existing
        z.n46j = self.next(float)  # High Density Urban Streambank Stabilization (km): Future
        z.n46k = self.next(float)  # Stream Km in Low Density Urban Areas W/Buffers: Existing
        z.n46l = self.next(float)  # Stream Km in Low Density Urban Areas W/Buffers: Future
        z.n46m = self.next(float)  # Low Density Urban Streambank Stabilization (km): Existing
        z.n46n = self.next(float)  # Low Density Urban Streambank Stabilization (km): Future
        z.n46o = self.next(float)  # Unpaved Road Km with E and S Controls (km): Existing
        z.n46p = self.next(float)  # Unpaved Road Km with E and S Controls (km): Future
        self.next(EOL)

        # Line 113:
        z.n47 = self.next(float)  # Number of Persons on Septic Systems: Existing
        z.n48 = self.next(float)  # No longer used (Default = 0)
        z.n49 = self.next(float)  # Number of Persons on Septic Systems: Future
        z.n50 = self.next(float)  # No longer used (Default = 0)
        z.n51 = self.next(float)  # Septic Systems Converted by Secondary Treatment Type (%)
        z.n52 = self.next(float)  # Septic Systems Converted by Tertiary Treatment Type (%)
        z.n53 = self.next(float)  # No longer used (Default = 0)
        z.n54 = self.next(float)  # Distribution of Pollutant Discharges by Primary Treatment Type (%): Existing
        z.n55 = self.next(float)  # Distribution of Pollutant Discharges by Secondary Treatment Type (%): Existing
        z.n56 = self.next(float)  # Distribution of Pollutant Discharges by Tertiary Treatment Type (%): Existing
        z.n57 = self.next(float)  # Distribution of Pollutant Discharges by Primary Treatment Type (%): Future
        z.n58 = self.next(float)  # Distribution of Pollutant Discharges by Secondary Treatment Type (%): Future
        z.n59 = self.next(float)  # Distribution of Pollutant Discharges by Tertiary Treatment Type (%): Future
        z.n60 = self.next(float)  # Distribution of Treatment Upgrades (%): Primary to Secondary
        z.n61 = self.next(float)  # Distribution of Treatment Upgrades (%): Primary to Tertiary
        z.n62 = self.next(float)  # Distribution of Treatment Upgrades (%): Secondary to Tertiary
        self.next(EOL)

        # Line 114: (BMP Load Reduction Efficiencies)
        z.n63 = self.next(float)  # BMP 1 (Nitrogen)
        z.n64 = self.next(float)  # Vegetated Buffer Strips (Nitrogen)
        z.n65 = self.next(float)  # BMP 2 (Nitrogen)
        z.n66 = self.next(float)  # BMP 3 (Nitrogen)
        z.n66b = self.next(float)  # BMP 4 (Nitrogen)
        z.n67 = self.next(float)  # BMP 5 (Nitrogen)
        z.n68 = self.next(float)  # BMP 8 (Nitrogen)
        z.n68b = self.next(float)  # BMP 7 (Nitrogen)
        z.n69 = self.next(float)  # Streambank Fencing (Nitrogen)
        z.n69b = self.next(float)  # Constructed Wetlands (Nitrogen)
        z.n69c = self.next(float)  # Streambank Stabilization (Nitrogen)
        z.n70 = self.next(float)  # BMP 6 (Nitrogen)
        z.n70b = self.next(float)  # Detention Basins (Nitrogen)
        self.next(EOL)

        # Line 115: (BMP Load Reduction Efficiencies cont.)
        z.n71 = self.next(float)  # BMP 1 (Phosphorus)
        z.n71b = self.next(float)  # Bioretention Areas (Nitrogen)
        z.n72 = self.next(float)  # Vegetated Buffer Strips (Phosphorus)
        z.n73 = self.next(float)  # BMP 2 (Phosphorus)
        z.n74 = self.next(float)  # BMP 3 (Phosphorus)
        z.n74b = self.next(float)  # BMP 4 (Phosphorus)
        z.n75 = self.next(float)  # BMP 5 (Phosphorus)
        z.n76 = self.next(float)  # BMP 8 (Phosphorus)
        z.n76b = self.next(float)  # BMP 7 (Phosphorus)
        z.n77 = self.next(float)  # Streambank Fencing (Phosphorus)
        z.n77b = self.next(float)  # Constructed Wetlands (Phosphorus)
        z.n77c = self.next(float)  # Streambank Stabilization (Phosphorus)
        z.n78 = self.next(float)  # BMP 6 (Phosphorus)
        z.n78b = self.next(float)  # Detention Basins (Phosphorus)
        self.next(EOL)

        # Line 116: (BMP Load Reduction Efficiencies cont.)
        z.n79 = self.next(float)  # BMP 1 (Sediment)
        z.n79b = self.next(float)  # Bioretention Areas (Phosphorus)
        z.n79c = self.next(float)  # Bioretention Areas (Sediment)
        z.n80 = self.next(float)  # Vegetated Buffer Strips (Sediment)
        z.n81 = self.next(float)  # BMP 2 (Sediment)
        z.n82 = self.next(float)  # BMP 3 (Sediment)
        z.n82b = self.next(float)  # BMP 4 (Sediment)
        z.n83 = self.next(float)  # BMP 5 (Sediment)
        z.n84 = self.next(float)  # BMP 8 (Sediment)
        z.n84b = self.next(float)  # BMP 7 (Sediment)
        z.n85 = self.next(float)  # Streambank Fencing (Sediment)
        z.n85b = self.next(float)  # Constructed Wetlands (Sediment)
        z.n85c = self.next(float)  # Detention Basins (Sediment)
        z.n85d = self.next(float)  # Streambank Stabilization (Sediment)
        z.n85e = self.next(float)  # Unpaved Road (kg/meter) (Nitrogen)
        z.n85f = self.next(float)  # Unpaved Road (kg/meter) (Phosphorus)
        z.n85g = self.next(float)  # Unpaved Road (kg/meter) (Sediment)
        self.next(EOL)

        # Line 117: (BMP Load Reduction Efficiencies cont.)
        z.n85h = self.next(float)  # AWMS (Livestock) (Nitrogen)
        z.n85i = self.next(float)  # AWMS (Livestock) (Phosphorus)
        z.n85j = self.next(float)  # AWMS (Poultry) (Nitrogen)
        z.n85k = self.next(float)  # AWMS (Poultry) (Phosphorus)
        z.n85l = self.next(float)  # Runoff Control (Nitrogen)
        z.n85m = self.next(float)  # Runoff Control (Phosphorus)
        z.n85n = self.next(float)  # Phytase in Feed (Phosphorus)
        z.n85o = self.next(float)  # Vegetated Buffer Strips (Pathogens)
        z.n85p = self.next(float)  # Streambank Fencing (Pathogens)
        z.n85q = self.next(float)  # AWMS (Livestock) (Pathogens)
        z.n85r = self.next(float)  # AWMS (Poultry) (Pathogens)
        z.n85s = self.next(float)  # Runoff Control (Pathogens)
        z.n85t = self.next(float)  # Constructed Wetlands (Pathogens)
        z.n85u = self.next(float)  # Bioretention Areas (Pathogens)
        z.n85v = self.next(float)  # Detention Basins (Pathogens)
        self.next(EOL)

        # Line 118: (Wastewater Discharge BMP Reduction Efficiencies)
        z.n86 = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Nitrogen)
        z.n87 = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Nitrogen)
        z.n88 = self.next(float)  # Conversion of Primary System to Secondary Treatment Plant (Nitrogen)
        z.n89 = self.next(float)  # Conversion of Primary System to Tertiary Treatment Plant (Nitrogen)
        z.n90 = self.next(float)  # Conversion of Secondary System to Tertiary Treatment Plant (Nitrogen)
        z.n91 = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Phosphorus)
        z.n92 = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Phosphorus)
        z.n93 = self.next(float)  # Conversion of Primary System to Secondary Treatment Plant (Phosphorus)
        z.n94 = self.next(float)  # Conversion of Primary System to Tertiary Treatment Plant (Phosphorus)
        z.n95 = self.next(float)  # Conversion of Secondary System to Tertiary Treatment Plant (Phosphorus)
        z.n95b = self.next(float)  # Conversion of Septic System to Secondary Treatment Plant (Pathogens)
        z.n95c = self.next(float)  # Conversion of Septic System to Tertiary Treatment Plant (Pathogens)
        z.n95d = self.next(float)  # Wastewater Treatment Plants Pathogen Distribution (cfu/100mL): Existing
        z.n95e = self.next(float)  # Wastewater Treatment Plants Pathogen Distribution (cfu/100mL): Future
        self.next(EOL)

        # Line 119: (BMP Costs $)
        z.n96 = self.next(float)  # Conservation Tillage (per Ha)
        z.n97 = self.next(float)  # Cover Crops (per Ha)
        z.n98 = self.next(float)  # Grazing Land Management (per Ha)
        z.n99 = self.next(float)  # Streambank Fencing (per km)
        z.n99b = self.next(float)  # Strip Cropping/Contour Farming (per Ha)
        z.n99c = self.next(float)  # Constructed Wetlands (per impervious Ha drained)
        z.n99d = self.next(float)  # Streambank Stabilization (per meter)
        z.n99e = self.next(float)  # Bioretention Areas (per impervious Ha drained)
        z.n100 = self.next(float)  # Vegetated Buffer Strip (per Km)
        z.n101 = self.next(float)  # Agricultural Land Retirement (per Ha)
        z.n101b = self.next(float)  # AWMS/Livestock (per AEU)
        z.n101c = self.next(float)  # AWMS/Poultry (per AEU)
        z.n101d = self.next(float)  # Runoff Control (per AEU)
        z.n101e = self.next(float)  # Phytase in Feed (per AEU)
        z.n102 = self.next(float)  # Nutrient Management (per Ha)
        z.n103a = self.next(float)  # User Defined (per Ha)
        z.n103b = self.next(float)  # Detention Basins (per impervious Ha drained)
        z.n103c = self.next(float)  # Conservation Plan (per Ha)
        z.n103d = self.next(float)  # Unpaved Roads (per meter)
        self.next(EOL)

        # Line 120:
        z.n104 = self.next(
            float)  # BMP Costs $: Conversion of Septic Systems to Centralized Sewage Treatment (per home)
        z.n105 = self.next(float)  # BMP Costs $: Conversion from Primary to Secondary Sewage Treatment (per capita)
        z.n106 = self.next(float)  # BMP Costs $: Conversion from Primary to Tertiary Sewage Treatment (per capita)
        z.n106b = self.next(float)  # No longer used (Default = 0)
        z.n106c = self.next(float)  # No longer used (Default = 0)
        z.n106d = self.next(float)  # No longer used (Default = 0)
        z.n107 = self.next(float)  # BMP Costs $: Conversion from Secondary to Tertiary Sewage Treatment (per capita)
        z.n107b = self.next(float)  # No longer used (Default = 0)
        z.n107c = self.next(float)  # No longer used (Default = 0)
        z.n107d = self.next(float)  # No longer used (Default = 0)
        z.n107e = self.next(float)  # No longer used (Default = 0)

        if self.version_match(z.TranVersionNo, '1.[0-2].[0-9]'):
            z.Storm = 0
            z.CSNAreaSim = 0
            z.CSNDevType = "None"
        else:
            z.Storm = self.next(float)  # CSN Tool: Storm Event Simulated (cm)
            z.CSNAreaSim = self.next(float)  # CSN Tool: Area Simulated (Ha)
            z.CSNDevType = self.next(str)  # CSN Tool: Development Type

        self.next(EOL)

        # Line 121:
        z.Qretention = self.next(float)  # Detention Basin: Amount of runoff retention (cm)
        z.FilterWidth = self.next(float)  # Stream Protection: Vegetative buffer strip width (meters)
        z.Capacity = self.next(float)  # Detention Basin: Detention basin volume (cubic meters)
        z.BasinDeadStorage = self.next(float)  # Detention Basin: Basin dead storage (cubic meters)
        z.BasinArea = self.next(float)  # Detention Basin: Basin surface area (square meters)
        z.DaysToDrain = self.next(float)  # Detention Basin: Basin days to drain
        z.CleanMon = self.next(float)  # Detention Basin: Basin cleaning month
        z.PctAreaInfil = self.next(float)  # Infiltration/Bioretention: Fraction of area treated (0-1)
        z.PctStrmBuf = self.next(float)  # Stream Protection: Fraction of streams treated (0-1)
        z.UrbBankStab = self.next(float)  # Stream Protection: Streams w/bank stabilization (km)

        z.ISRR = zeros(6)
        z.ISRA = zeros(6)
        z.ISRR[0] = self.next(float)  # Impervious Surface Reduction: Low Density Mixed (% Reduction)
        z.ISRA[0] = self.next(float)  # Impervious Surface Reduction: Low Density Mixed (% Area)
        z.ISRR[1] = self.next(float)  # Impervious Surface Reduction: Medium Density Mixed (% Reduction)
        z.ISRA[1] = self.next(float)  # Impervious Surface Reduction: Medium Density Mixed (% Area)
        z.ISRR[2] = self.next(float)  # Impervious Surface Reduction: High Density Mixed (% Reduction)
        z.ISRA[2] = self.next(float)  # Impervious Surface Reduction: High Density Mixed (% Area)
        z.ISRR[3] = self.next(float)  # Impervious Surface Reduction: Low Density Residential (% Reduction)
        z.ISRA[3] = self.next(float)  # Impervious Surface Reduction: Low Density Residential (% Area)
        z.ISRR[4] = self.next(float)  # Impervious Surface Reduction: Medium Density Residential (% Reduction)
        z.ISRA[4] = self.next(float)  # Impervious Surface Reduction: Medium Density Residential (% Area)
        z.ISRR[5] = self.next(float)  # Impervious Surface Reduction: High Density Residential (% Reduction)
        z.ISRA[5] = self.next(float)  # Impervious Surface Reduction: High Density Residential (% Area)

        if self.version_match(z.TranVersionNo, '1.[0-3].[0-9]'):
            z.SweepType = SweepType.MECHANICAL
            z.UrbSweepFrac = 1
        else:
            z.SweepType = self.next(SweepType.parse)  # Street Sweeping: Sweep Type (1-2)
            z.UrbSweepFrac = self.next(float)  # Street Sweeping: Fraction of area treated (0-1)

        self.next(EOL)

        # Lines 122 - 133: (Street Sweeping data for each Month)
        z.StreetSweepNo = zeros(12)

        for i in range(12):
            z.StreetSweepNo[i] = self.next(float)  # Street sweeping times per month
            self.next(EOL)

        # Line 134:
        z.OutName = self.next(str)  # PRedICT Output Name
        self.next(EOL)

        # Line 135: (Estimated Reduced Load)
        z.n108 = self.next(float)  # Row Crops: Sediment (kg x 1000)
        z.n109 = self.next(float)  # Row Crops: Nitrogen (kg)
        z.n110 = self.next(float)  # Row Crops: Phosphorus (kg)
        self.next(EOL)

        # Line 136: (Estimated Reduced Load)
        z.n111 = self.next(float)  # Hay/Pasture: Sediment (kg x 1000)
        z.n111b = self.next(float)  # High Density Urban: Sediment (kg x 1000)
        z.n111c = self.next(float)  # Low Density Urban: Sediment (kg x 1000)
        z.n111d = self.next(float)  # Unpaved Roads: Sediment (kg x 1000)
        z.n112 = self.next(float)  # Hay/Pasture: Nitrogen (kg)
        z.n112b = self.next(float)  # High Density Urban: Nitrogen (kg)
        z.n112c = self.next(float)  # Low Density Urban: Nitrogen (kg)
        z.n112d = self.next(float)  # Unpaved Roads: Nitrogen (kg)
        z.n113 = self.next(float)  # Hay/Pasture: Phosphorus (kg)
        z.n113b = self.next(float)  # High Density Urban: Phosphorus (kg)
        z.n113c = self.next(float)  # Low Density Urban: Phosphorus (kg)
        z.n113d = self.next(float)  # Unpaved Roads: Phosphorus (kg)
        self.next(EOL)

        # Line 137: (Estimated Reduced Load)
        z.n114 = self.next(float)  # Other: Sediment (kg x 1000)
        z.n115 = self.next(float)  # Other: Nitrogen (kg)
        z.n115b = self.next(float)  # Farm Animals: Nitrogen (kg)
        z.n116 = self.next(float)  # Other: Phosphorus (kg)
        z.n116b = self.next(float)  # Farm Animals: Phosphorus (kg)
        self.next(EOL)

        # Line 138: (Estimated Reduced Load)
        z.n117 = self.next(float)  # Streambank Erosion: Sediment (kg x 1000)
        z.n118 = self.next(float)  # Streambank Erosion: Nitrogen (kg)
        z.n119 = self.next(float)  # Streambank Erosion: Phosphorus (kg)
        self.next(EOL)

        # Line 139: (Estimated Reduced Load)
        z.n120 = self.next(float)  # Groundwater/Subsurface: Nitrogen (kg)
        z.n121 = self.next(float)  # Groundwater/Subsurface: Phosphorus (kg)
        self.next(EOL)

        # Line 140: (Estimated Reduced Load)
        z.n122 = self.next(float)  # Point Source Discharges: Nitrogen (kg)
        z.n123 = self.next(float)  # Point Source Discharges: Phosphorus (kg)
        self.next(EOL)

        # Line 141: (Estimated Reduced Load)
        z.n124 = self.next(float)  # Septic Systems: Nitrogen (kg)
        z.n125 = self.next(float)  # Septic Systems: Phosphorus (kg)
        self.next(EOL)

        # Line 142: (Estimated Reduced Load)
        z.n126 = self.next(float)  # Total: Sediment (kg x 1000)
        z.n127 = self.next(float)  # Total: Nitrogen (kg)
        z.n128 = self.next(float)  # Total: Phosphorus (kg)
        self.next(EOL)

        # Line 143: (Estimated Reduced Load)
        z.n129 = self.next(float)  # Percent Reduction: Sediment (%)
        z.n130 = self.next(float)  # Percent Reduction: Nitrogen (%)
        z.n131 = self.next(float)  # Percent Reduction: Phosphorus (%)
        self.next(EOL)

        # Line 144:
        z.n132 = self.next(float)  # Estimated Scenario Cost $: Total
        z.n133 = self.next(float)  # Estimated Scenario Cost $: Agricultural BMPs
        z.n134 = self.next(float)  # Estimated Scenario Cost $: Waste Water Upgrades
        z.n135 = self.next(float)  # Estimated Scenario Cost $: Urban BMPs
        z.n136 = self.next(float)  # Estimated Scenario Cost $: Stream Protection
        z.n137 = self.next(float)  # Estimated Scenario Cost $: Unpaved Road Protection
        z.n138 = self.next(float)  # Estimated Scenario Cost $: Animal BMPs
        z.n139 = self.next(float)  # Pathogen Loads (Farm Animals): Existing (orgs/month)
        z.n140 = self.next(float)  # Pathogen Loads (Wastewater Treatment Plants): Existing (orgs/month)
        self.next(EOL)

        # Line 145:
        z.n141 = self.next(float)  # Pathogen Loads (Septic Systems): Existing (orgs/month)
        z.n142 = self.next(float)  # Pathogen Loads (Urban Areas): Existing (orgs/month)
        z.n143 = self.next(float)  # Pathogen Loads (Wildlife): Existing (orgs/month)
        z.n144 = self.next(float)  # Pathogen Loads (Total): Existing (orgs/month)
        z.n145 = self.next(float)  # Pathogen Loads (Farm Animals): Future (orgs/month)
        z.n146 = self.next(float)  # Pathogen Loads (Wastewater Treatment Plants): Future (orgs/month)
        z.n147 = self.next(float)  # Pathogen Loads (Septic Systems): Future (orgs/month)
        z.n148 = self.next(float)  # Pathogen Loads (Urban Areas): Future (orgs/month)
        z.n149 = self.next(float)  # Pathogen Loads (Wildlife): Future (orgs/month)
        z.n150 = self.next(float)  # Pathogen Loads (Total): Future (orgs/month)
        z.n151 = self.next(float)  # Pathogen Loads: Percent Reduction (%)
        self.next(EOL)

        # Line 146:
        _ = self.next(float)  # Seems to be set to 0 before it is used
        z.InitNgP = self.next(float)  # Initial Non-Grazing Animal Totals: Phosphorus (kg/yr)
        z.InitNgFC = self.next(float)  # Initial Non-Grazing Animal Totals: Fecal Coliforms (orgs/yr)
        z.NGAppSum = self.next(float)  # Non-Grazing Manure Data Check: Land Applied (%)
        z.NGBarnSum = self.next(float)  # Non-Grazing Manure Data Check: In Confined Areas (%)
        z.NGTotSum = self.next(float)  # Non-Grazing Manure Data Check: Total (<= 1)
        _ = self.next(
            float)  # # Initial Grazing Animal Totals: Nitrogen (kg/yr) (Value seems to be set to 0 before it is used)
        z.InitGrP = self.next(float)  # Initial Grazing Animal Totals: Phosphorus (kg/yr)
        z.InitGrFC = self.next(float)  # Initial Grazing Animal Totals: Fecal Coliforms (orgs/yr)
        z.GRAppSum = self.next(float)  # Grazing Manure Data Check: Land Applied (%)
        z.GRBarnSum = self.next(float)  # Grazing Manure Data Check: In Confined Areas (%)
        z.GRTotSum = self.next(float)  # Grazing Manure Data Check: Total (<= 1)
        z.AnimalFlag = self.next(YesOrNo.parse)  # Flag: Animal Layer Detected (0 No; 1 Yes)
        self.next(EOL)

        # Line 147:
        z.WildOrgsDay = self.next(float)  # Wildlife Loading Rate (org/animal/per day)
        z.WildDensity = self.next(float)  # Wildlife Density (animals/square mile)
        z.WuDieoff = self.next(float)  # Wildlife/Urban Die-Off Rate
        z.UrbEMC = self.next(float)  # Urban EMC (org/100ml)
        z.SepticOrgsDay = self.next(float)  # Septic Loading Rate (org/person per day)
        z.SepticFailure = self.next(float)  # Malfunctioning System Rate (0 - 1)
        z.WWTPConc = self.next(float)  # Wastewater Treatment Plants Loading Rate (cfu/100ml)
        z.InstreamDieoff = self.next(float)  # In-Stream Die-Off Rate
        z.AWMSGrPct = self.next(float)  # Animal Waste Management Systems: Livestock (%)
        z.AWMSNgPct = self.next(float)  # Animal Waste Management Systems: Poultry (%)
        z.RunContPct = self.next(float)  # Runoff Control (%)
        z.PhytasePct = self.next(float)  # Phytase in Feed (%)
        self.next(EOL)

        # Line 148-156: (For each Animal type)
        z.AnimalName = zeros(z.NAnimals, dtype=object)
        z.NumAnimals = zeros(z.NAnimals, dtype=int)
        z.GrazingAnimal_0 = zeros(z.NAnimals, dtype=object)
        z.AvgAnimalWt = zeros(z.NAnimals)
        z.AnimalDailyN = zeros(z.NAnimals)
        z.AnimalDailyP = zeros(z.NAnimals)
        z.FCOrgsPerDay = zeros(z.NAnimals)

        for i in range(z.NAnimals):
            z.AnimalName[i] = self.next(str)  # Animal Name
            z.NumAnimals[i] = self.next(int)  # Number of Animals
            z.GrazingAnimal_0[i] = self.next(YesOrNo.parse)  # Flag: Grazing Animal (“N” No, “Y” Yes)
            z.AvgAnimalWt[i] = self.next(float)  # Average Animal Weight (kg)
            z.AnimalDailyN[i] = self.next(float)  # Animal Daily Loads: Nitrogen (kg/AEU)
            z.AnimalDailyP[i] = self.next(float)  # Animal Daily Loads: Phosphorus (kg/AEU)
            z.FCOrgsPerDay[i] = self.next(float)  # Fecal Coliforms (orgs/day)
            self.next(EOL)

        # Line 157-168: (For each month: Non-Grazing Animal Worksheet values)
        z.NGPctManApp = zeros(12)
        z.NGAppNRate = zeros(12)
        z.NGAppPRate = zeros(12)
        z.NGAppFCRate = zeros(12)
        z.NGPctSoilIncRate = zeros(12)
        z.NGBarnNRate = zeros(12)
        z.NGBarnPRate = zeros(12)
        z.NGBarnFCRate = zeros(12)

        for i in range(12):
            z.Month[i] = self.next(str)  # Month (Jan-Dec)
            z.NGPctManApp[i] = self.next(float)  # Manure Spreading: % Of Annual Load Applied To Crops/Pasture
            z.NGAppNRate[i] = self.next(float)  # Manure Spreading: Base Nitrogen Loss Rate
            z.NGAppPRate[i] = self.next(float)  # Manure Spreading: Base Phosphorus Loss Rate
            z.NGAppFCRate[i] = self.next(float)  # Manure Spreading: Base Fecal Coliform Loss Rate
            z.NGPctSoilIncRate[i] = self.next(float)  # Manure Spreading: % Of Manure Load Incorporated Into Soil
            z.NGBarnNRate[i] = self.next(float)  # Barnyard/Confined Area: Base Nitrogen Loss Rate
            z.NGBarnPRate[i] = self.next(float)  # Barnyard/Confined Area: Base Phosphorus Loss Rate
            z.NGBarnFCRate[i] = self.next(float)  # Barnyard/Confined Area: Base Fecal Coliform Loss Rate
            self.next(EOL)

        # Line 169-180: (For each month: Grazing Animal Worksheet values)
        z.PctGrazing = zeros(12)
        z.PctStreams = zeros(12)
        z.GrazingNRate = zeros(12)
        z.GrazingPRate = zeros(12)
        z.GrazingFCRate = zeros(12)
        z.GRPctManApp = zeros(12)
        z.GRAppNRate = zeros(12)
        z.GRAppPRate = zeros(12)
        z.GRAppFCRate = zeros(12)
        z.GRPctSoilIncRate = zeros(12)
        z.GRBarnNRate = zeros(12)
        z.GRBarnPRate = zeros(12)
        z.GRBarnFCRate = zeros(12)

        for i in range(12):
            z.Month[i] = self.next(str)  # Month (Jan-Dec)
            z.PctGrazing[i] = self.next(float)  # Grazing Land: % Of Time Spent Grazing
            z.PctStreams[i] = self.next(float)  # Grazing Land: % Of Time Spent In Streams
            z.GrazingNRate[i] = self.next(float)  # Grazing Land: Base Nitrogen Loss Rate
            z.GrazingPRate[i] = self.next(float)  # Grazing Land: Base Phosphorus Loss Rate
            z.GrazingFCRate[i] = self.next(float)  # Grazing Land: Base Fecal Coliform Loss Rate
            z.GRPctManApp[i] = self.next(float)  # Manure Spreading: % Of Annual Load Applied To Crops/Pasture
            z.GRAppNRate[i] = self.next(float)  # Manure Spreading: Base Nitrogen Loss Rate
            z.GRAppPRate[i] = self.next(float)  # Manure Spreading: Base Phosphorus Loss Rate
            z.GRAppFCRate[i] = self.next(float)  # Manure Spreading: Base Fecal Coliform Loss Rate
            z.GRPctSoilIncRate[i] = self.next(float)  # Manure Spreading: % Of Manure Load Incorporated Into Soil
            z.GRBarnNRate[i] = self.next(float)  # Barnyard/Confined Area: Base Nitrogen Loss Rate
            z.GRBarnPRate[i] = self.next(float)  # Barnyard/Confined Area: Base Phosphorus Loss Rate
            z.GRBarnFCRate[i] = self.next(float)  # Barnyard/Confined Area: Base Fecal Coliform Loss Rate
            self.next(EOL)

        # Line 181: (Nutrient Retention data)
        z.ShedAreaDrainLake = self.next(
            float)  # Percentage of watershed area that drains into a lake or wetlands: (0 - 1)
        z.RetentNLake = self.next(float)  # Lake Retention Rate: Nitrogen
        z.RetentPLake = self.next(float)  # Lake Retention Rate: Phosphorus
        z.RetentSedLake = self.next(float)  # Lake Retention Rate: Sediment
        z.AttenFlowDist = self.next(float)  # Attenuation: Flow Distance (km)
        z.AttenFlowVel = self.next(float)  # Attenuation: Flow Velocity (km/hr)
        z.AttenLossRateN = self.next(float)  # Attenuation: Loss Rate: Nitrogen
        z.AttenLossRateP = self.next(float)  # Attenuation: Loss Rate: Phosphorus
        z.AttenLossRateTSS = self.next(float)  # Attenuation: Loss Rate: Total Suspended Solids
        z.AttenLossRatePath = self.next(float)  # Attenuation: Loss Rate: Pathogens
        z.StreamFlowVolAdj = self.next(float)  # Streamflow Volume Adjustment Factor
        self.next(EOL)

        # Line 182 – Last Weather Day: (Weather data)
        z.DaysMonth = zeros((z.WxYrs, 12), dtype=int)
        z.WxMonth = zeros((z.WxYrs, 12), dtype=object)
        z.WxYear = zeros((z.WxYrs, 12))
        z.Temp = zeros((z.WxYrs, 12, 31))
        z.Prec = zeros((z.WxYrs, 12, 31))

        for year in range(z.WxYrs):
            for month in range(12):
                z.DaysMonth[year][month] = self.next(int)  # Days
                z.WxMonth[year][month] = self.next(str)  # Month (Jan-Dec)
                z.WxYear[year][month] = self.next(int)  # Year
                self.next(EOL)

                for day in range(z.DaysMonth[year][month]):
                    z.Temp[year][month][day] = self.next(float)  # Average Temperature (C)
                    z.Prec[year][month][day] = self.next(float)  # Precipitation (cm)
                    self.next(EOL)

        # Line Beginning After Weather: (Urban Area data)
        z.NumUAs = self.next(int)  # Number of Urban Areas
        z.UABasinArea = self.next(float)  # Urban Area Basin Area (Ha)
        self.next(EOL)

        z.UAId = zeros(z.NumUAs)
        z.UAName = zeros(z.NumUAs, dtype=object)
        z.UAArea = zeros(z.NumUAs)
        z.UAfa = zeros(z.NumUAs, dtype=object)
        z.UAfaAreaFrac = zeros(z.NumUAs)
        z.UATD = zeros(z.NumUAs, dtype=object)
        z.UATDAreaFrac = zeros(z.NumUAs)
        z.UASB = zeros(z.NumUAs, dtype=object)
        z.UASBAreaFrac = zeros(z.NumUAs)
        z.UAGW = zeros(z.NumUAs, dtype=object)
        z.UAGWAreaFrac = zeros(z.NumUAs)
        z.UAPS = zeros(z.NumUAs, dtype=object)
        z.UAPSAreaFrac = zeros(z.NumUAs)
        z.UASS = zeros(z.NumUAs, dtype=object)
        z.UASSAreaFrac = zeros(z.NumUAs)

        # +1 for "Water"
        z.UALU = zeros((z.NumUAs, z.NLU + 1), dtype=object)
        z.UALUArea = zeros((z.NumUAs, z.NLU + 1))

        # Lines if Number of Urban Areas > 0: (for each Urban Area)
        for i in range(z.NumUAs):
            # Line 1:
            z.UAId[i] = self.next(int)  # Urban Area ID
            z.UAName[i] = self.next(str)  # Urban Area Name
            z.UAArea[i] = self.next(float)  # Urban Area Area (Ha)
            self.next(EOL)

            # Lines 2 - 17: (For each Land Use Category)
            # +1 for "Water"
            for l in range(z.NLU + 1):
                z.UALU[i][l] = self.next(LandUse.parse)  # Land Use Category
                z.UALUArea[i][l] = self.next(float)  # Urban Land Use Area (Ha)
                self.next(EOL)

            # Line 18:
            z.UAfa[i] = self.next('Farm Animals')
            z.UAfaAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

            # Line 19:
            z.UATD[i] = self.next('Tile Drainage')
            z.UATDAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

            # Line 20:
            z.UASB[i] = self.next('Stream Bank')
            z.UASBAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

            # Line 21:
            z.UAGW[i] = self.next('Groundwater')
            z.UAGWAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

            # Line 22:
            z.UAPS[i] = self.next('Point Sources')
            z.UAPSAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

            # Line 23:
            z.UASS[i] = self.next('Septic Systems')
            z.UASSAreaFrac[i] = self.next(float)  # Area Fraction
            self.next(EOL)

        return z

    def next(self, typ):
        """
        Pop the next token and cast it using the given callable function
        or type. If a scalar value is passed instead, assert that the
        next token value matches and raise a ValueError if it does not.
        """
        value, line_no, col_no = next(self.fp)

        if callable(typ):
            try:
                return typ(value)
            except ValueError:
                log.error('Unexpected token at Line {} Column {}'.format(line_no, col_no))
                raise

        if typ != value:
            raise ValueError('Expected "{}" but got "{}" at Line {} Column {}'.format(typ, value, line_no, col_no))

        return value

    def version_match(self, TranVersionNo, VersionPatternRegex):
        pattern = '^{}$'.format(VersionPatternRegex)
        return re.match(pattern, TranVersionNo)


class GmsWriter(object):
    ENUMS = (YesOrNo, ETflag, GrowFlag, SweepType, LandUse)

    def __init__(self, fp):
        self.fp = csv.writer(fp)

    def writeOutput(self, z):
        """This function writes the result of running the model to a GMS file for later analysis"""
        unsatstor_carryover = UnSatStorCarryover_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb,
                                                   z.Area, z.CNI_0,
                                                   z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                                   z.UnsatStor_0, z.KV,
                                                   z.PcntET, z.DayHrs, z.MaxWaterCap)
        satstor_carryover = SatStorCarryOver_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb,
                                               z.Area, z.CNI_0,
                                               z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                               z.UnsatStor_0, z.KV,
                                               z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef,
                                               z.SeepCoef)
        antmoist = AntMoist(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0)
        cni = CNI_f(z.NRur, z.NUrb, z.CNI_0)
        cnp = CNP_f(z.NRur, z.NUrb, z.CNP_0)
        n7b_2 = N7b_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                      z.NGAppNRate,
                      z.Prec,
                      z.DaysMonth,
                      z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct,
                      z.NgAWMSCoeffN,
                      z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                      z.PctStreams,
                      z.GrazingNRate,
                      z.n41b,
                      z.n85h, z.n41d, z.n85j, z.n41f, z.n85l, z.n42, z.n45, z.n69, z.n43, z.n64)
        grlbn_2 = GRLBN_2(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                          z.PctGrazing, z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                          z.RunConCoeffN)
        ng_lost_barn_n_sum = NGLostBarnNSum(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                            z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct,
                                            z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN)
        av_gr_stream_n = AvGRStreamN_f(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                       z.AnimalDailyN)
        init_ng_n = InitNgN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)
        init_gr_n = InitGrN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)
        self.write_gms(z, unsatstor_carryover, satstor_carryover, z.InitSnow_0, z.SedDelivRatio_0, z.SedAFactor_0, antmoist, z.Grow_0, cni, cnp,
                       n7b_2, grlbn_2,
                       ng_lost_barn_n_sum,
                       av_gr_stream_n, init_ng_n, init_gr_n,z.GrazingAnimal_0)

    def write(self, python_ob):  # TODO: rename this function something like "python_to_gms"
        """This function converts Azavea's internal structure to a GMS file"""

        self.write_gms(python_ob, python_ob.UnsatStor, python_ob.SatStor, python_ob.InitSnow, python_ob.SedDelivRatio,
                       python_ob.SedAFactor,
                       python_ob.AntMoist, python_ob.Grow, python_ob.CNI,
                       python_ob.CNP, [python_ob.n7b], [python_ob.GRLBN], [python_ob.NGLBN],
                       python_ob.GRSN, python_ob.InitNgN, python_ob.InitGrN, python_ob.GrazingAnimal)

    def write_gms(self, z, UnSatStorCarryover, SatStorCarryOver, InitSnow_0, SedDelivRatio_0, SedAFactor_0, AntMoist, Grow_0, CNI, CNP, N7b_2,
                  GRLBN_2, NGLostBarnNSum,
                  AvGRStreamN, InitNgN, InitGrN, GrazingAnimal_0):
        """This is a generalized function for writing GMS files. The z argument should eventually be replaced by explicit arguments"""
        self.writerow([
            z.NRur,
            z.NUrb,
            z.BasinId,
        ])

        self.writerow([
            z.TranVersionNo,
            z.RecessionCoef,
            z.SeepCoef,
            UnSatStorCarryover,
            SatStorCarryOver,
            InitSnow_0,
            SedDelivRatio_0,
            z.MaxWaterCap,
            z.StreamLength,
            z.AgLength,
            z.UrbLength,
            z.AgSlope3,
            z.AgSlope3to8,
            z.AvSlope,
            z.AEU,
            z.WxYrs,
            z.WxYrBeg,
            z.WxYrEnd,
            SedAFactor_0,
            z.TotArea,
            z.TileDrainRatio,
            z.TileDrainDensity,
            z.ETFlag,
            z.AvKF,
        ])

        for i in range(5):
            self.writerow([AntMoist[i]])

        for i in range(12):
            self.writerow([
                z.Month[i],
                z.KV[i],
                z.DayHrs[i],
                Grow_0[i],
                z.Acoef[i],
                z.StreamWithdrawal[i],
                z.GroundWithdrawal[i],
                z.PcntET[i],
            ])

        for i in range(z.NRur):
            self.writerow([
                z.Landuse[i],
                z.Area[i],
                z.CN[i],
                z.KF[i],
                z.LS[i],
                z.C[i],
                z.P[i],
            ])

        for i in range(z.NRur, z.NLU):
            self.writerow([
                z.Landuse[i],
                z.Area[i],
                z.Imper[i],

                CNI[1][i],
                CNP[1][i],
                z.TotSusSolids[i],
            ])

        self.writerow([
            YesOrNo.intval(z.PhysFlag),
            YesOrNo.intval(z.PointFlag),
            YesOrNo.intval(z.SeptSysFlag),
            YesOrNo.intval(z.CountyFlag),
            YesOrNo.intval(z.SoilPFlag),
            YesOrNo.intval(z.GWNFlag),
            z.SedAAdjust,
        ])

        self.writerow([
            z.SedNitr,
            z.SedPhos,
            z.GrNitrConc,
            z.GrPhosConc,
            z.BankNFrac,
            z.BankPFrac,
        ])

        # Convert 0-based indexes to 1-based.
        self.writerow([
            z.ManuredAreas,
            z.FirstManureMonth + 1,
            z.LastManureMonth + 1,
            z.FirstManureMonth2 + 1,
            z.LastManureMonth2 + 1,
        ])

        for i in range(z.NRur):
            self.writerow([
                z.NitrConc[i],
                z.PhosConc[i],
            ])

        self.writerow([z.Nqual])

        for i in range(z.Nqual):
            self.writerow([z.Contaminant[i]])

        for u in range(z.NRur, z.NLU):
            for q in range(z.Nqual):
                self.writerow([
                    z.LoadRateImp[u][q],
                    z.LoadRatePerv[u][q],
                    z.DisFract[u][q],
                    z.UrbBMPRed[u][q],
                ])

        for i in range(z.ManuredAreas):
            self.writerow([z.ManNitr[i], z.ManPhos[i]])

        for i in range(12):
            self.writerow([
                z.PointNitr[i],
                z.PointPhos[i],
                z.PointFlow[i],
            ])

        self.writerow([YesOrNo.intval(z.SepticFlag)])

        for i in range(12):
            self.writerow([
                z.NumNormalSys[i],
                z.NumPondSys[i],
                z.NumShortSys[i],
                z.NumDischargeSys[i],
                z.NumSewerSys[i],
            ])

        self.writerow([
            z.NitrSepticLoad,
            z.PhosSepticLoad,
            z.NitrPlantUptake,
            z.PhosPlantUptake,
        ])

        self.writerow([
            z.TileNconc,
            z.TilePConc,
            z.TileSedConc,
        ])

        self.writerow([
            z.InName,
            z.UnitsFileFlag,
            z.AssessDate,
            z.VersionNo,
        ])

        self.writerow([z.ProjName])

        self.writerow([
            z.n1,
            z.n2,
            z.n2b,
            z.n2c,
            z.n2d,
            z.n3,
            z.n4,
        ])

        self.writerow([
            z.n5,
            z.n6,
            z.n6b,
            z.n6c,
            z.n6d,
            z.n7,
            N7b_2[-1],  # get the carried over value
            z.n8,
            z.n9,
            z.n10,
            z.n11,
        ])

        self.writerow([
            z.n12,
            z.n13,
            z.n13b,
            z.n13c,
            z.n13d,
            z.n14,
            z.n14b,
            z.n15,
            z.n16,
            z.n17,
            z.n18,
        ])

        self.writerow([
            z.n19,
            z.n20,
            z.n21,
            z.n22,
        ])

        self.writerow([
            z.n23,
            z.n23b,
            z.n23c,
            z.n24,
            z.n24b,
            z.n24c,
            z.n24d,
            z.n24e,
        ])

        self.writerow([
            z.n25,
            z.n25b,
            z.n25c,
            z.n25d,
            z.n25e,
            z.n26,
            z.n26b,
            z.n26c,
            z.n27,
            z.n27b,
            z.n28,
            z.n28b,
            z.n29,
        ])

        self.writerow([
            z.n30,
            z.n30b,
            z.n30c,
            z.n30d,
            z.n30e,
            z.n31,
            z.n31b,
            z.n31c,
            z.n32,
            z.n32b,
            z.n32c,
            z.n32d,
            z.n33,
            z.n33b,
            z.n33c,
            z.n33d,
        ])

        self.writerow([
            z.n34,
            z.n35,
            z.n35b,
            z.n36,
            z.n37,
            z.n38,
            z.n38b,
            z.n39,
            z.n40,
        ])

        self.writerow([
            z.n41,
            z.n41b,
            z.n41c,
            z.n41d,
            z.n41e,
            z.n41f,
            z.n41g,
            z.n41h,
            z.n41i,
            z.n41j,
            z.n41k,
            z.n41l,
            z.n42,
            z.n42b,
            z.n42c,
            z.n43,
            GRLBN_2[-1],
            NGLostBarnNSum[-1],
            z.GRLBP,
            z.NGLBP,
            z.NGLManP,
            z.NGLBFC,
            z.GRLBFC,
            z.GRSFC,
            AvGRStreamN,
            z.GRSP,
        ])

        self.writerow([
            z.n43b,
            z.n43c,
            z.n43d,
            z.n43e,
            z.n43f,
            z.n43g,
            z.n43h,
            z.n43i,
            z.n43j,
            z.n44,
            z.n44b,
            z.n45,
            z.n45b,
            z.n45c,
            z.n45d,
            z.n45e,
            z.n45f,
        ])

        self.writerow([
            z.n46,
            z.n46b,
            z.n46c,
            z.n46d,
            z.n46e,
            z.n46f,
            z.n46g,
            z.n46h,
            z.n46i,
            z.n46j,
            z.n46k,
            z.n46l,
            z.n46m,
            z.n46n,
            z.n46o,
            z.n46p,
        ])

        self.writerow([
            z.n47,
            z.n48,
            z.n49,
            z.n50,
            z.n51,
            z.n52,
            z.n53,
            z.n54,
            z.n55,
            z.n56,
            z.n57,
            z.n58,
            z.n59,
            z.n60,
            z.n61,
            z.n62,
        ])

        self.writerow([
            z.n63,
            z.n64,
            z.n65,
            z.n66,
            z.n66b,
            z.n67,
            z.n68,
            z.n68b,
            z.n69,
            z.n69b,
            z.n69c,
            z.n70,
            z.n70b,
        ])

        self.writerow([
            z.n71,
            z.n71b,
            z.n72,
            z.n73,
            z.n74,
            z.n74b,
            z.n75,
            z.n76,
            z.n76b,
            z.n77,
            z.n77b,
            z.n77c,
            z.n78,
            z.n78b,
        ])

        self.writerow([
            z.n79,
            z.n79b,
            z.n79c,
            z.n80,
            z.n81,
            z.n82,
            z.n82b,
            z.n83,
            z.n84,
            z.n84b,
            z.n85,
            z.n85b,
            z.n85c,
            z.n85d,
            z.n85e,
            z.n85f,
            z.n85g,
        ])

        self.writerow([
            z.n85h,
            z.n85i,
            z.n85j,
            z.n85k,
            z.n85l,
            z.n85m,
            z.n85n,
            z.n85o,
            z.n85p,
            z.n85q,
            z.n85r,
            z.n85s,
            z.n85t,
            z.n85u,
            z.n85v,
        ])

        self.writerow([
            z.n86,
            z.n87,
            z.n88,
            z.n89,
            z.n90,
            z.n91,
            z.n92,
            z.n93,
            z.n94,
            z.n95,
            z.n95b,
            z.n95c,
            z.n95d,
            z.n95e,
        ])

        self.writerow([
            z.n96,
            z.n97,
            z.n98,
            z.n99,
            z.n99b,
            z.n99c,
            z.n99d,
            z.n99e,
            z.n100,
            z.n101,
            z.n101b,
            z.n101c,
            z.n101d,
            z.n101e,
            z.n102,
            z.n103a,
            z.n103b,
            z.n103c,
            z.n103d,
        ])

        self.writerow([
            z.n104,
            z.n105,
            z.n106,
            z.n106b,
            z.n106c,
            z.n106d,
            z.n107,
            z.n107b,
            z.n107c,
            z.n107d,
            z.n107e,
            z.Storm,
            z.CSNAreaSim,
            z.CSNDevType,
        ])

        self.writerow([
            z.Qretention,
            z.FilterWidth,
            z.Capacity,
            z.BasinDeadStorage,
            z.BasinArea,
            z.DaysToDrain,
            z.CleanMon,
            z.PctAreaInfil,
            z.PctStrmBuf,
            z.UrbBankStab,
            z.ISRR[0],
            z.ISRA[0],
            z.ISRR[1],
            z.ISRA[1],
            z.ISRR[2],
            z.ISRA[2],
            z.ISRR[3],
            z.ISRA[3],
            z.ISRR[4],
            z.ISRA[4],
            z.ISRR[5],
            z.ISRA[5],
            z.SweepType,
            z.UrbSweepFrac,
        ])

        for i in range(12):
            self.writerow([z.StreetSweepNo[i]])

        self.writerow([z.OutName])

        self.writerow([
            z.n108,
            z.n109,
            z.n110,
        ])

        self.writerow([
            z.n111,
            z.n111b,
            z.n111c,
            z.n111d,
            z.n112,
            z.n112b,
            z.n112c,
            z.n112d,
            z.n113,
            z.n113b,
            z.n113c,
            z.n113d,
        ])

        self.writerow([
            z.n114,
            z.n115,
            z.n115b,
            z.n116,
            z.n116b,
        ])

        self.writerow([
            z.n117,
            z.n118,
            z.n119,
        ])

        self.writerow([
            z.n120,
            z.n121,
        ])

        self.writerow([
            z.n122,
            z.n123,
        ])

        self.writerow([
            z.n124,
            z.n125,
        ])

        self.writerow([
            z.n126,
            z.n127,
            z.n128,
        ])

        self.writerow([
            z.n129,
            z.n130,
            z.n131,
        ])

        self.writerow([
            z.n132,
            z.n133,
            z.n134,
            z.n135,
            z.n136,
            z.n137,
            z.n138,
            z.n139,
            z.n140,
        ])

        self.writerow([
            z.n141,
            z.n142,
            z.n143,
            z.n144,
            z.n145,
            z.n146,
            z.n147,
            z.n148,
            z.n149,
            z.n150,
            z.n151,
        ])

        self.writerow([
            InitNgN,
            z.InitNgP,
            z.InitNgFC,
            z.NGAppSum,
            z.NGBarnSum,
            z.NGTotSum,
            InitGrN,
            z.InitGrP,
            z.InitGrFC,
            z.GRAppSum,
            z.GRBarnSum,
            z.GRTotSum,
            YesOrNo.intval(z.AnimalFlag),
        ])

        self.writerow([
            z.WildOrgsDay,
            z.WildDensity,
            z.WuDieoff,
            z.UrbEMC,
            z.SepticOrgsDay,
            z.SepticFailure,
            z.WWTPConc,
            z.InstreamDieoff,
            z.AWMSGrPct,
            z.AWMSNgPct,
            z.RunContPct,
            z.PhytasePct,
        ])

        for i in range(z.NAnimals):
            self.writerow([
                z.AnimalName[i],
                z.NumAnimals[i],
                GrazingAnimal_0[i],
                z.AvgAnimalWt[i],
                z.AnimalDailyN[i],
                z.AnimalDailyP[i],
                z.FCOrgsPerDay[i],
            ])

        for i in range(12):
            self.writerow([
                z.Month[i],
                z.NGPctManApp[i],
                z.NGAppNRate[i],
                z.NGAppPRate[i],
                z.NGAppFCRate[i],
                z.NGPctSoilIncRate[i],
                z.NGBarnNRate[i],
                z.NGBarnPRate[i],
                z.NGBarnFCRate[i],
            ])

        for i in range(12):
            self.writerow([
                z.Month[i],
                z.PctGrazing[i],
                z.PctStreams[i],
                z.GrazingNRate[i],
                z.GrazingPRate[i],
                z.GrazingFCRate[i],
                z.GRPctManApp[i],
                z.GRAppNRate[i],
                z.GRAppPRate[i],
                z.GRAppFCRate[i],
                z.GRPctSoilIncRate[i],
                z.GRBarnNRate[i],
                z.GRBarnPRate[i],
                z.GRBarnFCRate[i],
            ])

        self.writerow([
            z.ShedAreaDrainLake,
            z.RetentNLake,
            z.RetentPLake,
            z.RetentSedLake,
            z.AttenFlowDist,
            z.AttenFlowVel,
            z.AttenLossRateN,
            z.AttenLossRateP,
            z.AttenLossRateTSS,
            z.AttenLossRatePath,
            z.StreamFlowVolAdj,
        ])

        for year in range(z.WxYrs):
            for month in range(12):
                self.writerow([
                    z.DaysMonth[year][month],
                    z.WxMonth[year][month],
                    z.WxYear[year][month],
                ])
                for day in range(z.DaysMonth[year][month]):
                    self.writerow([
                        z.Temp[year][month][day],
                        z.Prec[year][month][day],
                    ])

        self.writerow([
            z.NumUAs,
            z.UABasinArea,
        ])

        for i in range(z.NumUAs):
            self.writerow([
                z.UAId[i],
                z.UAName[i],
                z.UAArea[i],
            ])

            # +1 for "Water"
            for l in range(z.NLU + 1):
                self.writerow([
                    z.UALU[i][l],
                    z.UALUArea[i][l],
                ])

            self.writerow([
                z.UAfa[i],
                z.UAfaAreaFrac[i],
            ])

            self.writerow([
                z.UATD[i],
                z.UATDAreaFrac[i],
            ])

            self.writerow([
                z.UASB[i],
                z.UASBAreaFrac[i],
            ])

            self.writerow([
                z.UAGW[i],
                z.UAGWAreaFrac[i],
            ])

            self.writerow([
                z.UAPS[i],
                z.UAPSAreaFrac[i],
            ])

            self.writerow([
                z.UASS[i],
                z.UASSAreaFrac[i],
            ])

    def writerow(self, row):
        self.fp.writerow([self.serialize_value(col) for col in row])

    def serialize_value(self, value):
        if isinstance(value, str):
            return self.serialize_enum(value)
        return value

    def serialize_enum(self, value):
        # Find the first valid enum that can parse this value.
        for enm in self.ENUMS:
            try:
                return enm.gmsval(value)
            except ValueError:
                pass
        return value
