# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import re
import csv
import logging

import numpy as np

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

        z.ImpervAccum = np.zeros(16)
        z.PervAccum = np.zeros(16)
        z.QrunI = np.zeros(16)
        z.QrunP = np.zeros(16)
        z.WashPerv = np.zeros(16)
        z.NetDisLoad = np.zeros(3)

        z.AvGRStreamFC = 0
        z.AvGRStreamN = 0
        z.AvGRStreamP = 0
        z.AvTileDrain = np.zeros(12)
        z.RurAreaTotal = 0
        z.UrbAreaTotal = 0
        z.d = np.zeros(12)
        z.KVD = np.zeros(12)
        z.CV = np.zeros(12)
        z.AreaE = np.zeros(16)
        z.KLSCP = np.zeros(16)
        z.UrbanNitr = np.zeros(16)
        z.UrbanPhos = np.zeros(16)
        z.AvStreamFlow = np.zeros(12)
        z.AvPrecipitation = np.zeros(12)
        z.AvEvapoTrans = np.zeros(12)
        z.AvGroundWater = np.zeros(12)
        z.AvRunoff = np.zeros(12)
        z.AvErosion = np.zeros(12)
        z.AvSedYield = np.zeros(12)
        z.AFON = np.zeros(12)
        z.AFOP = np.zeros(12)
        z.AvLoad = np.zeros((12, 3))
        z.AvLuLoad = np.zeros((16, 3))
        z.AvDisLoad = np.zeros((16, 3))
        z.AvLuDisLoad = np.zeros((16, 3))
        z.UrbSedLoad = np.zeros((16, 12))
        z.AvGroundNitr = np.zeros(12)
        z.AvGroundPhos = np.zeros(12)
        z.AvDisNitr = np.zeros(12)
        z.AvTotNitr = np.zeros(12)
        z.AvDisPhos = np.zeros(12)
        z.AvTotPhos = np.zeros(12)
        z.AvLuRunoff = np.zeros(16)
        z.AvLuErosion = np.zeros(16)
        z.AvLuSedYield = np.zeros(16)
        z.AvLuDisNitr = np.zeros(16)
        z.AvLuTotNitr = np.zeros(16)
        z.AvLuDisPhos = np.zeros(16)
        z.AvLuTotPhos = np.zeros(16)
        z.BSed = np.zeros(16)
        z.UrbanSed = np.zeros(16)
        z.UrbanErosion = np.zeros(16)
        z.ErosWashoff = np.zeros((16, 12))
        z.QRunoff = np.zeros((16, 12))
        z.AgQRunoff = np.zeros((16, 12))
        z.RurQRunoff = np.zeros((16, 12))
        z.UrbQRunoff = np.zeros((16, 12))
        z.DailyLoad = np.zeros((50, 12, 31))
        z.SepticsDay = np.zeros(12)
        z.MonthlyLoad = np.zeros((12, 31))

        # Declare the daily values as ReDimensional arrays in
        # to Pesticide components
        z.DayPondNitr = np.zeros((12, 31))
        z.DayPondPhos = np.zeros((12, 31))
        z.DayNormNitr = np.zeros((12, 31))
        z.DayNormPhos = np.zeros((12, 31))
        z.WashImperv = np.zeros(16)
        z.NetSolidLoad = np.zeros(3)
        z.DayShortNitr = np.zeros((12, 31))
        z.DayShortPhos = np.zeros((12, 31))
        z.DayDischargeNitr = np.zeros((12, 31))
        z.DayDischargePhos = np.zeros((12, 31))
        z.PestAppMonth1 = np.zeros(16)
        z.PestAppYear1 = np.zeros(16)
        z.PestAppDate1 = np.zeros(16)
        z.PestAppMonth2 = np.zeros(16)
        z.PestAppYear2 = np.zeros(16)
        z.PestAppDate2 = np.zeros(16)
        z.PestShedName = np.zeros(12)
        z.PestCropArea = np.zeros(12)
        z.PestSoilBd = np.zeros(12)
        z.PestSoilAwc = np.zeros(12)
        z.PestSoilOm = np.zeros(12)
        z.PestCropName = np.zeros(12)
        z.PestName1 = np.zeros(16)
        z.PestRate1 = np.zeros(31)
        z.PestParamCarbon1 = np.zeros(16)
        z.PestParamWater1 = np.zeros(16)
        z.PestDecay1 = np.zeros(16)
        z.PestHalfLife1 = np.zeros(16)
        z.PestName2 = np.zeros(16)
        z.PestRate2 = np.zeros(31)
        z.PestParamCarbon2 = np.zeros(16)
        z.PestParamWater2 = np.zeros(16)
        z.PestDecay2 = np.zeros(16)
        z.PestHalfLife2 = np.zeros(16)
        z.AvStreamBankEros = np.zeros(12)
        z.AvStreamBankN = np.zeros(12)
        z.AvStreamBankP = np.zeros(12)
        z.CropPercent = np.zeros(12)
        z.PestSoilAwcCm = np.zeros(12)

        # Tile Drainage and Flow Variables
        z.AvTileDrain = np.zeros(12)
        z.AvWithdrawal = np.zeros(12)
        z.AvTileDrainN = np.zeros(12)
        z.AvTileDrainP = np.zeros(12)
        z.AvTileDrainSed = np.zeros(12)
        z.AvPtSrcFlow = np.zeros(12)

        # Calculated Values for Animal Feeding Operations
        z.NGLoadN = np.zeros(9)
        z.NGLoadP = np.zeros(9)
        z.NGLoadFC = np.zeros(9)
        z.NGAccManAppN = np.zeros(12)
        z.NGAccManAppP = np.zeros(12)
        z.NGAccManAppFC = np.zeros(12)
        z.NGAppManN = np.zeros(12)
        z.NGInitBarnN = np.zeros(12)
        z.NGAppManP = np.zeros(12)
        z.NGInitBarnP = np.zeros(12)
        z.NGAppManFC = np.zeros(12)
        z.NGInitBarnFC = np.zeros(12)

        z.GRLoadN = np.zeros(9)
        z.GRLoadP = np.zeros(9)
        z.GRLoadFC = np.zeros(9)
        z.GRAccManAppN = np.zeros(12)
        z.GRAccManAppP = np.zeros(12)
        z.GRAccManAppFC = np.zeros(12)
        z.GRAppManN = np.zeros(12)
        z.GRInitBarnN = np.zeros(12)
        z.GRAppManP = np.zeros(12)
        z.GRInitBarnP = np.zeros(12)
        z.GRAppManFC = np.zeros(12)
        z.GRInitBarnFC = np.zeros(12)
        z.GrazingN = np.zeros(12)
        z.GrazingP = np.zeros(12)
        z.GrazingFC = np.zeros(12)
        z.GRStreamN = np.zeros(12)
        z.GRStreamP = np.zeros(12)
        z.GRStreamFC = np.zeros(12)
        z.AvAnimalN = np.zeros(12)
        z.AvAnimalP = np.zeros(12)
        z.AvAnimalFC = np.zeros(12)
        z.AvWWOrgs = np.zeros(12)
        z.AvSSOrgs = np.zeros(12)
        z.AvUrbOrgs = np.zeros(12)
        z.AvWildOrgs = np.zeros(12)
        z.AvTotalOrgs = np.zeros(12)
        z.AvCMStream = np.zeros(12)
        z.AvOrgConc = np.zeros(12)
        z.AvGRLostBarnN = np.zeros(12)
        z.AvGRLostBarnP = np.zeros(12)
        z.AvNGLostBarnN = np.zeros(12)
        z.AvNGLostBarnP = np.zeros(12)
        z.AvNGLostManP = np.zeros(12)
        z.AvNGLostBarnFC = np.zeros(12)
        z.AvGRLostBarnFC = np.zeros(12)
        z.SweepFrac = np.zeros(12)

        z.q = 0
        z.k = 0
        z.FilterEff = 0
        z.OutFiltWidth = 0
        z.Clean = 0
        z.CleanSwitch = 0
        z.OutletCoef = 0
        z.BasinVol = 0
        z.Volume = 0
        z.ActiveVol = 0
        z.DetentFlow = 0
        z.AnnDayHrs = 0
        z.AreaTotal = 0
        z.FrozenPondNitr = 0
        z.FrozenPondPhos = 0
        z.AvSeptNitr = 0
        z.AvSeptPhos = 0
        z.AgAreaTotal = 0
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

        z.NLU = z.NRur + z.NUrb

        # This is hard-coded to 9 in the original GWLF-E code.
        z.NAnimals = 9

        # Line 2:
        z.TranVersionNo = self.next(str)  # GWLF-E Version
        z.RecessionCoef = self.next(float)  # Recession Coefficient
        z.SeepCoef = self.next(float)  # Seepage Coefficient
        z.UnsatStor = self.next(float)  # Unsaturated Storage
        z.SatStor = self.next(float)  # Saturated Storage
        z.InitSnow = self.next(int)  # Initial Snow Days
        z.SedDelivRatio = self.next(float)  # Sediment Delivery Ratio
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
        z.SedAFactor = self.next(float)  # Sediment A Factor
        z.TotArea = self.next(float)  # Total Basin Area (Ha)
        z.TileDrainRatio = self.next(float)  # Tile Drain Ratio
        z.TileDrainDensity = self.next(float)  # Tile Drain Density
        z.ETFlag = self.next(ETflag.parse)  # ET Flag
        z.AvKF = self.next(float)  # Average K Factor
        self.next(EOL)

        z.NYrs = z.WxYrs
        # TODO: Remove DimYrs
        z.DimYrs = z.WxYrs

        z.Load = np.zeros((z.DimYrs, 12, 3))
        z.DisLoad = np.zeros((z.DimYrs, 12, 3))
        z.LuLoad = np.zeros((z.DimYrs, 16, 3))
        z.LuDisLoad = np.zeros((z.DimYrs, 16, 3))
        z.UplandN = np.zeros((z.DimYrs, 12))
        z.UplandP = np.zeros((z.DimYrs, 12))
        z.UrbRunoffCm = np.zeros((z.DimYrs, 12))
        z.UrbRunoffLiter = np.zeros((z.DimYrs, 12))
        z.DailyFlow = np.zeros((z.DimYrs, 12, 31))
        z.DailyFlowMGD = np.zeros((z.DimYrs, 12, 31))
        z.DailyFlowGPM = np.zeros((z.DimYrs, 12, 31))
        z.DailyPtSrcFlow = np.zeros((z.DimYrs, 12, 31))

        # Declare the daily values as ReDimensional arrays in
        # to Pesticide components
        z.DailyUplandSed = np.zeros((z.DimYrs, 12, 31))
        z.DailyUplandN = np.zeros((z.DimYrs, 12, 31))
        z.DailyUplandP = np.zeros((z.DimYrs, 12, 31))
        z.DailyTileDrainN = np.zeros((z.DimYrs, 12, 31))
        z.DailyTileDrainP = np.zeros((z.DimYrs, 12, 31))
        z.DailyStrmSed = np.zeros((z.DimYrs, 12, 31))
        z.DailySepticN = np.zeros((z.DimYrs, 12, 31))
        z.DailySepticP = np.zeros((z.DimYrs, 12, 31))
        z.DailyStrmN = np.zeros((z.DimYrs, 12, 31))
        z.DailyStrmP = np.zeros((z.DimYrs, 12, 31))
        z.DailyGroundN = np.zeros((z.DimYrs, 12, 31))
        z.DailyGroundP = np.zeros((z.DimYrs, 12, 31))
        z.DayGroundNitr = np.zeros((z.DimYrs, 12, 31))
        z.DayGroundPhos = np.zeros((z.DimYrs, 12, 31))
        z.DayDisPhos = np.zeros((z.DimYrs, 12, 31))
        z.DayDisNitr = np.zeros((z.DimYrs, 12, 31))
        z.DayTotNitr = np.zeros((z.DimYrs, 12, 31))
        z.DailyPointN = np.zeros((z.DimYrs, 12, 31))
        z.DailyPointP = np.zeros((z.DimYrs, 12, 31))
        z.DayTotPhos = np.zeros((z.DimYrs, 12, 31))
        z.DayLuTotN = np.zeros((16, z.DimYrs, 12, 31))
        z.DayLuTotP = np.zeros((16, z.DimYrs, 12, 31))
        z.DayLuDisN = np.zeros((16, z.DimYrs, 12, 31))
        z.DayLuDisP = np.zeros((16, z.DimYrs, 12, 31))
        z.DayErWashoff = np.zeros((16, z.DimYrs, 12, 31))
        z.Perc = np.zeros((z.DimYrs, 12, 31))
        z.DeepFlow = np.zeros((z.DimYrs, 12, 31))
        z.DayQRunoff = np.zeros((z.DimYrs, 12, 31))
        z.SdYld = np.zeros((z.DimYrs, 12, 31))
        z.Erosn = np.zeros((z.DimYrs, 12, 31))
        z.DayErosion = np.zeros((z.DimYrs, 12, 31))
        z.DayLuErosion = np.zeros((16, z.DimYrs, 12, 31))
        z.DaySed = np.zeros((z.DimYrs, 12, 31))
        z.DayLuSed = np.zeros((16, z.DimYrs, 12, 31))
        z.DayRunoff = np.zeros((z.DimYrs, 12, 31))
        z.DayLuRunoff = np.zeros((16, z.DimYrs, 12, 31))
        z.MeltPest = np.zeros((z.DimYrs, 12, 31))
        z.PrecPest = np.zeros((z.DimYrs, 12, 31))
        z.DailyGrFlow = np.zeros((z.DimYrs, 12, 31))
        z.DailyETCm = np.zeros((z.DimYrs, 12, 31))
        z.DailyETShal = np.zeros((z.DimYrs, 12, 31))
        z.PercCm = np.zeros((z.DimYrs, 12, 31))
        z.PercShal = np.zeros((z.DimYrs, 12, 31))
        z.DailyUnsatStorCm = np.zeros((z.DimYrs, 12, 31))
        z.DailyUnsatStorShal = np.zeros((z.DimYrs, 12, 31))
        z.DailyET = np.zeros((z.DimYrs, 12, 31))
        z.DailyRetent = np.zeros((z.DimYrs, 12, 31))
        z.SatStorPest = np.zeros((z.DimYrs, 12, 31))
        z.UrbanRunoff = np.zeros((z.DimYrs, 12))
        z.RuralRunoff = np.zeros((z.DimYrs, 12))
        z.DailyInfilt = np.zeros((z.DimYrs, 12, 31))
        z.StreamFlowVol = np.zeros((z.DimYrs, 12))
        z.DailyCN = np.zeros((z.DimYrs, 12, 31))
        z.DailyWater = np.zeros((z.DimYrs, 12, 31))
        z.LE = np.zeros((z.DimYrs, 12))
        z.StreamBankEros = np.zeros((z.DimYrs, 12))
        z.StreamBankN = np.zeros((z.DimYrs, 12))
        z.StreamBankP = np.zeros((z.DimYrs, 12))
        z.DailyAMC5 = np.zeros((z.DimYrs, 12, 31))
        z.MonthFlow = np.zeros((z.DimYrs, 12))
        z.LuGrFlow = np.zeros((16, z.DimYrs, 12, 31))
        z.LuDeepSeep = np.zeros((16, z.DimYrs, 12, 31))
        z.LuInfiltration = np.zeros((16, z.DimYrs, 12, 31))
        z.PestTemp = np.zeros((z.DimYrs, 12, 31))
        z.PestPrec = np.zeros((z.DimYrs, 12, 31))

        # Tile Drainage and Flow Variables
        z.TileDrainN = np.zeros((z.DimYrs, 12))
        z.TileDrainP = np.zeros((z.DimYrs, 12))
        z.TileDrainSed = np.zeros((z.DimYrs, 12))
        z.TileDrain = np.zeros((z.DimYrs, 12))
        z.TileDrainRO = np.zeros((z.DimYrs, 12))
        z.TileDrainGW = np.zeros((z.DimYrs, 12))
        z.GwAgLE = np.zeros((z.DimYrs, 12))
        z.Withdrawal = np.zeros((z.DimYrs, 12))
        z.PtSrcFlow = np.zeros((z.DimYrs, 12))
        z.StreamFlow = np.zeros((z.DimYrs, 12))
        z.StreamFlowLE = np.zeros((z.DimYrs, 12))
        z.Precipitation = np.zeros((z.DimYrs, 12))
        z.Evapotrans = np.zeros((z.DimYrs, 12))
        z.GroundWatLE = np.zeros((z.DimYrs, 12))
        z.AgRunoff = np.zeros((z.DimYrs, 12))
        z.Runoff = np.zeros((z.DimYrs, 12))
        z.Erosion = np.zeros((z.DimYrs, 12))
        z.SedYield = np.zeros((z.DimYrs, 12))
        z.GroundNitr = np.zeros((z.DimYrs, 12))
        z.GroundPhos = np.zeros((z.DimYrs, 12))
        z.DisNitr = np.zeros((z.DimYrs, 12))
        z.SepticN = np.zeros((z.DimYrs, 12))
        z.SepticP = np.zeros((z.DimYrs, 12))
        z.TotNitr = np.zeros((z.DimYrs, 12))
        z.DisPhos = np.zeros((z.DimYrs, 12))
        z.TotPhos = np.zeros((z.DimYrs, 12))
        z.LuRunoff = np.zeros((z.DimYrs, 16))
        z.LuErosion = np.zeros((z.DimYrs, 16))
        z.LuSedYield = np.zeros((z.DimYrs, 16))
        z.LuDisNitr = np.zeros((z.DimYrs, 16))
        z.LuTotNitr = np.zeros((z.DimYrs, 16))
        z.LuDisPhos = np.zeros((z.DimYrs, 16))
        z.LuTotPhos = np.zeros((z.DimYrs, 16))
        z.SedTrans = np.zeros((z.DimYrs, 16))
        z.SepticNitr = np.zeros(z.DimYrs)
        z.SepticPhos = np.zeros(z.DimYrs)

        # ANIMAL FEEDING OPERATIONS VARIABLES
        z.DailyAnimalN = np.zeros((z.DimYrs, 12, 31))
        z.DailyAnimalP = np.zeros((z.DimYrs, 12, 31))

        # Calculated Values for Animal Feeding Operations
        z.NGLostManN = np.zeros((z.DimYrs, 12))
        z.NGLostBarnN = np.zeros((z.DimYrs, 12))
        z.NGLostManP = np.zeros((z.DimYrs, 12))
        z.NGLostBarnP = np.zeros((z.DimYrs, 12))
        z.NGLostManFC = np.zeros((z.DimYrs, 12))
        z.NGLostBarnFC = np.zeros((z.DimYrs, 12))

        z.GRLostManN = np.zeros((z.DimYrs, 12))
        z.GRLostBarnN = np.zeros((z.DimYrs, 12))
        z.GRLossN = np.zeros((z.DimYrs, 12))
        z.GRLostManP = np.zeros((z.DimYrs, 12))
        z.GRLostBarnP = np.zeros((z.DimYrs, 12))
        z.GRLossP = np.zeros((z.DimYrs, 12))
        z.GRLostManFC = np.zeros((z.DimYrs, 12))
        z.GRLostBarnFC = np.zeros((z.DimYrs, 12))
        z.GRLossFC = np.zeros((z.DimYrs, 12))
        z.LossFactAdj = np.zeros((z.DimYrs, 12))
        z.AnimalN = np.zeros((z.DimYrs, 12))
        z.AnimalP = np.zeros((z.DimYrs, 12))
        z.AnimalFC = np.zeros((z.DimYrs, 12))
        z.WWOrgs = np.zeros((z.DimYrs, 12))
        z.SSOrgs = np.zeros((z.DimYrs, 12))
        z.UrbOrgs = np.zeros((z.DimYrs, 12))
        z.WildOrgs = np.zeros((z.DimYrs, 12))
        z.TotalOrgs = np.zeros((z.DimYrs, 12))
        z.CMStream = np.zeros((z.DimYrs, 12))
        z.OrgConc = np.zeros((z.DimYrs, 12))

        z.StreamBankNSum = np.zeros(z.WxYrs)
        z.StreamBankPSum = np.zeros(z.WxYrs)
        z.StreamBankErosSum = np.zeros(z.WxYrs)
        z.StreamBankNSum = np.zeros(z.WxYrs)
        z.StreamBankPSum = np.zeros(z.WxYrs)
        z.GroundNitrSum = np.zeros(z.WxYrs)
        z.GroundPhosSum = np.zeros(z.WxYrs)
        z.TileDrainSum = np.zeros(z.WxYrs)
        z.TileDrainNSum = np.zeros(z.WxYrs)
        z.TileDrainPSum = np.zeros(z.WxYrs)
        z.TileDrainSedSum = np.zeros(z.WxYrs)
        z.AnimalNSum = np.zeros(z.WxYrs)
        z.AnimalPSum = np.zeros(z.WxYrs)
        z.AnimalFCSum = np.zeros(z.WxYrs)
        z.WWOrgsSum = np.zeros(z.WxYrs)
        z.SSOrgsSum = np.zeros(z.WxYrs)
        z.UrbOrgsSum = np.zeros(z.WxYrs)
        z.WildOrgsSum = np.zeros(z.WxYrs)
        z.TotalOrgsSum = np.zeros(z.WxYrs)
        z.GRLostBarnNSum = np.zeros(z.WxYrs)
        z.GRLostBarnPSum = np.zeros(z.WxYrs)
        z.GRLostBarnFCSum = np.zeros(z.WxYrs)
        z.NGLostBarnNSum = np.zeros(z.WxYrs)
        z.NGLostBarnPSum = np.zeros(z.WxYrs)
        z.NGLostBarnFCSum = np.zeros(z.WxYrs)
        z.NGLostManPSum = np.zeros(z.WxYrs)
        z.TotNitrSum = np.zeros(z.WxYrs)
        z.TotPhosSum = np.zeros(z.WxYrs)

        # Set the Total AEU to the value from the Animal Density layer
        if not self.version_match(z.TranVersionNo, '1.[0-9].[0-9]'):
            raise Exception('Input data file is not in the correct format or is no longer supported')

        # Lines 3 - 7: (each line represents 1 day)
        # Antecedent Rain + Melt Moisture Condition for Days 1 to 5
        z.AntMoist = np.zeros(5)

        for i in range(5):
            z.AntMoist[i] = self.next(float)
            self.next(EOL)

        # Lines 8 - 19: (each line represents 1 month)
        z.Month = np.zeros(12, dtype=object)
        z.KV = np.zeros(12)
        z.DayHrs = np.zeros(12)
        z.Grow = np.zeros(12, dtype=object)
        z.Acoef = np.zeros(12)
        z.StreamWithdrawal = np.zeros(12)
        z.GroundWithdrawal = np.zeros(12)
        z.PcntET = np.zeros(12)

        for i in range(12):
            z.Month[i] = self.next(str)  # Month (Jan - Dec)
            z.KV[i] = self.next(float)  # KET (Flow Factor)
            z.DayHrs[i] = self.next(float)  # Day Length (hours)
            z.Grow[i] = self.next(GrowFlag.parse)  # Growing season flag
            z.Acoef[i] = self.next(float)  # Erosion Coefficient
            z.StreamWithdrawal[i] = self.next(float)  # Surface Water Withdrawal/Extraction
            z.GroundWithdrawal[i] = self.next(float)  # Groundwater Withdrawal/Extraction
            z.PcntET[i] = self.next(float)  # Percent monthly adjustment for ET calculation
            self.next(EOL)

        # Lines 20 - 29: (for each Rural Land Use Category)
        z.Landuse = np.zeros(z.NLU, dtype=object)
        z.Area = np.zeros(z.NLU)
        z.CN = np.zeros(z.NLU)
        z.KF = np.zeros(z.NLU)
        z.LS = np.zeros(z.NLU)
        z.C = np.zeros(z.NLU)
        z.P = np.zeros(z.NLU)

        for i in range(z.NRur):
            z.Landuse[i] = self.next(LandUse.parse)  # Rural Land Use Category
            z.Area[i] = self.next(float)  # Area (Ha)
            z.CN[i] = self.next(float)  # Curve Number
            z.KF[i] = self.next(float)  # K Factor
            z.LS[i] = self.next(float)  # LS Factor
            z.C[i] = self.next(float)   # C Factor
            z.P[i] = self.next(float)   # P Factor
            self.next(EOL)

        # Lines 30 - 35: (for each Urban Land Use Category)
        z.Imper = np.zeros(z.NLU)
        z.TotSusSolids = np.zeros(z.NLU)

        z.CNI = np.zeros((3, z.NLU))
        z.CNP = np.zeros((3, z.NLU))
        z.NewCN = np.zeros((3, z.NLU))

        for i in range(z.NRur, z.NLU):
            z.Landuse[i] = self.next(LandUse.parse)  # Urban Land Use Category
            z.Area[i] = self.next(float)  # Area (Ha)
            z.Imper[i] = self.next(float)  # Impervious Surface %
            z.CNI[1][i] = self.next(float)  # Curve Number(Impervious Surfaces)
            z.CNP[1][i] = self.next(float)  # Curve Number(Pervious Surfaces)
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
        z.NitrConc = np.zeros(16)
        z.PhosConc = np.zeros(16)

        for i in range(z.NRur):
            z.NitrConc[i] = self.next(float)  # Dissolved Runoff Coefficient: N (mg/l)
            z.PhosConc[i] = self.next(float)  # Dissolved Runoff Coefficient: P (mg/l)
            self.next(EOL)

        # Line 49:
        z.Nqual = self.next(int)  # Number of Contaminants (Default = 3; Nitrogen, Phosphorus, Sediment)
        self.next(EOL)

        # Lines 50 - 52:
        z.Contaminant = np.zeros(z.Nqual, dtype=object)
        z.SolidBasinMass = np.zeros(z.Nqual)
        z.DisBasinMass = np.zeros(z.Nqual)

        for i in range(z.Nqual):
            z.Contaminant[i] = self.next(str)
            self.next(EOL)

        # Lines 53 - 58 (for each Urban Land Use Category, Nitrogen Contaminant)
        # Lines 59 - 64: (for each Urban Land Use Category, Phosphorus Contaminant)
        # Lines 65 - 70: (for each Urban Land Use Category, Sediment Contaminant)
        z.LoadRateImp = np.zeros((z.NLU, z.Nqual))
        z.LoadRatePerv = np.zeros((z.NLU, z.Nqual))
        z.DisFract = np.zeros((z.NLU, z.Nqual))
        z.UrbBMPRed = np.zeros((z.NLU, z.Nqual))

        for u in range(z.NRur, z.NLU):
            for q in range(z.Nqual):
                z.LoadRateImp[u][q] = self.next(float)  # Loading Rate Impervious Surface
                z.LoadRatePerv[u][q] = self.next(float)  # Loading Rate Pervious Surface
                z.DisFract[u][q] = self.next(float)  # Dissolved Fraction
                z.UrbBMPRed[u][q] = self.next(float)  # Urban BMP Reduction
                self.next(EOL)

        z.ManNitr = np.zeros(z.ManuredAreas)
        z.ManPhos = np.zeros(z.ManuredAreas)

        # Lines 71 - 72: (for the 2 Manure Spreading Periods)
        for i in range(z.ManuredAreas):
            z.ManNitr[i] = self.next(float)  # Manured N Concentration
        self.next(EOL)

        for i in range(z.ManuredAreas):
            z.ManPhos[i] = self.next(float)  # Manured P Concentration
        self.next(EOL)

        # Lines 73 - 84: (Point Source data for each Month)
        z.PointNitr = np.zeros(12)
        z.PointPhos = np.zeros(12)
        z.PointFlow = np.zeros(12)

        for i in range(12):
            z.PointNitr[i] = self.next(float)  # N Load (kg)
            z.PointPhos[i] = self.next(float)  # P Load (kg)
            z.PointFlow[i] = self.next(float)  # Discharge (Millions of Gallons per Day)
            self.next(EOL)

        # Line 85:
        z.SepticFlag = self.next(YesOrNo.parse)  # Flag: Septic Systems Layer Detected (0 No; 1 Yes)
        self.next(EOL)

        # Lines 86 - 97: (Septic System data for each Month)
        z.NumNormalSys = np.zeros(12)
        z.NumPondSys = np.zeros(12)
        z.NumShortSys = np.zeros(12)
        z.NumDischargeSys = np.zeros(12)
        z.NumSewerSys = np.zeros(12)

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
        z.n7b = self.next(float)  # Farm Animals
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
        z.GRLBN = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        z.NGLBN = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Nitrogen
        z.GRLBP = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        z.NGLBP = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Phosphorus
        z.NGLManP = self.next(float)  # Average Non-Grazing Animal Loss Rate (Manure Spreading): Phosphorus
        z.NGLBFC = self.next(float)  # Average Non-Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        z.GRLBFC = self.next(float)  # Average Grazing Animal Loss Rate (Barnyard/Confined Area): Fecal Coliform
        z.GRSFC = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Fecal Coliform
        z.GRSN = self.next(float)  # Average Grazing Animal Loss Rate (Spent in Streams): Nitrogen
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
        z.n104 = self.next(float)  # BMP Costs $: Conversion of Septic Systems to Centralized Sewage Treatment (per home)
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

        z.ISRR = np.zeros(6)
        z.ISRA = np.zeros(6)
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
        z.StreetSweepNo = np.zeros(12)

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
        z.InitNgN = self.next(float)  # Initial Non-Grazing Animal Totals: Nitrogen (kg/yr)
        z.InitNgP = self.next(float)  # Initial Non-Grazing Animal Totals: Phosphorus (kg/yr)
        z.InitNgFC = self.next(float)  # Initial Non-Grazing Animal Totals: Fecal Coliforms (orgs/yr)
        z.NGAppSum = self.next(float)  # Non-Grazing Manure Data Check: Land Applied (%)
        z.NGBarnSum = self.next(float)  # Non-Grazing Manure Data Check: In Confined Areas (%)
        z.NGTotSum = self.next(float)  # Non-Grazing Manure Data Check: Total (<= 1)
        z.InitGrN = self.next(float)  # Initial Grazing Animal Totals: Nitrogen (kg/yr)
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
        z.AnimalName = np.zeros(z.NAnimals, dtype=object)
        z.NumAnimals = np.zeros(z.NAnimals)
        z.GrazingAnimal = np.zeros(z.NAnimals, dtype=object)
        z.AvgAnimalWt = np.zeros(z.NAnimals)
        z.AnimalDailyN = np.zeros(z.NAnimals)
        z.AnimalDailyP = np.zeros(z.NAnimals)
        z.FCOrgsPerDay = np.zeros(z.NAnimals)

        for i in range(z.NAnimals):
            z.AnimalName[i] = self.next(str)  # Animal Name
            z.NumAnimals[i] = self.next(int)  # Number of Animals
            z.GrazingAnimal[i] = self.next(YesOrNo.parse)  # Flag: Grazing Animal (“N” No, “Y” Yes)
            z.AvgAnimalWt[i] = self.next(float)  # Average Animal Weight (kg)
            z.AnimalDailyN[i] = self.next(float)  # Animal Daily Loads: Nitrogen (kg/AEU)
            z.AnimalDailyP[i] = self.next(float)  # Animal Daily Loads: Phosphorus (kg/AEU)
            z.FCOrgsPerDay[i] = self.next(float)  # Fecal Coliforms (orgs/day)
            self.next(EOL)

        # Line 157-168: (For each month: Non-Grazing Animal Worksheet values)
        z.NGPctManApp = np.zeros(12)
        z.NGAppNRate = np.zeros(12)
        z.NGAppPRate = np.zeros(12)
        z.NGAppFCRate = np.zeros(12)
        z.NGPctSoilIncRate = np.zeros(12)
        z.NGBarnNRate = np.zeros(12)
        z.NGBarnPRate = np.zeros(12)
        z.NGBarnFCRate = np.zeros(12)

        for i in range(12):
            # Month is already populated on lines 8 - 19
            self.next(str)  # Month (Jan-Dec)
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
        z.PctGrazing = np.zeros(12)
        z.PctStreams = np.zeros(12)
        z.GrazingNRate = np.zeros(12)
        z.GrazingPRate = np.zeros(12)
        z.GrazingFCRate = np.zeros(12)
        z.GRPctManApp = np.zeros(12)
        z.GRAppNRate = np.zeros(12)
        z.GRAppPRate = np.zeros(12)
        z.GRAppFCRate = np.zeros(12)
        z.GRPctSoilIncRate = np.zeros(12)
        z.GRBarnNRate = np.zeros(12)
        z.GRBarnPRate = np.zeros(12)
        z.GRBarnFCRate = np.zeros(12)

        for i in range(12):
            # Month is already populated on lines 8 - 19
            self.next(str)  # Month (Jan-Dec)
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
        z.ShedAreaDrainLake = self.next(float)  # Percentage of watershed area that drains into a lake or wetlands: (0 - 1)
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
        z.DaysMonth = np.zeros((z.WxYrs, 12), dtype=int)
        z.WxMonth = np.zeros((z.WxYrs, 12), dtype=object)
        z.WxYear = np.zeros((z.WxYrs, 12))
        z.Temp = np.zeros((z.WxYrs, 12, 31))
        z.Prec = np.zeros((z.WxYrs, 12, 31))

        for year in range(z.WxYrs):
            for month in range(12):
                num_days = self.next(int)

                z.DaysMonth[year][month] = num_days  # Days
                z.WxMonth[year][month] = self.next(str)  # Month (Jan-Dec)
                z.WxYear[year][month] = self.next(int)  # Year
                self.next(EOL)

                for day in range(num_days):
                    z.Temp[year][month][day] = self.next(int)  # Average Temperature (C)
                    z.Prec[year][month][day] = self.next(float)  # Precipitation (cm)
                    self.next(EOL)

        # Line Beginning After Weather: (Urban Area data)
        z.NumUAs = self.next(int)  # Number of Urban Areas
        z.UABasinArea = self.next(float)  # Urban Area Basin Area (Ha)
        self.next(EOL)

        z.UAId = np.zeros(z.NumUAs)
        z.UAName = np.zeros(z.NumUAs, dtype=object)
        z.UAArea = np.zeros(z.NumUAs)
        z.UAfa = np.zeros(z.NumUAs, dtype=object)
        z.UAfaAreaFrac = np.zeros(z.NumUAs)
        z.UATD = np.zeros(z.NumUAs, dtype=object)
        z.UATDAreaFrac = np.zeros(z.NumUAs)
        z.UASB = np.zeros(z.NumUAs, dtype=object)
        z.UASBAreaFrac = np.zeros(z.NumUAs)
        z.UAGW = np.zeros(z.NumUAs, dtype=object)
        z.UAGWAreaFrac = np.zeros(z.NumUAs)
        z.UAPS = np.zeros(z.NumUAs, dtype=object)
        z.UAPSAreaFrac = np.zeros(z.NumUAs)
        z.UASS = np.zeros(z.NumUAs, dtype=object)
        z.UASSAreaFrac = np.zeros(z.NumUAs)

        # +1 for "Water"
        z.UALU = np.zeros((z.NumUAs, z.NLU + 1), dtype=object)
        z.UALUArea = np.zeros((z.NumUAs, z.NLU + 1))

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

    def version_match(self, TranVersionNo, VersionPatternRegex):
        pattern = '^{}$'.format(VersionPatternRegex)
        return re.match(pattern, TranVersionNo)
