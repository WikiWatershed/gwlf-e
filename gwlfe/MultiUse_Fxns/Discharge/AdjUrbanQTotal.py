# from Timer import time_function
from numpy import zeros

from gwlfe.Input.LandUse.AreaTotal import AreaTotal
from gwlfe.Input.LandUse.AreaTotal import AreaTotal_f
from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal
from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal_f
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal import UrbanQTotal
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal import UrbanQTotal_f

try:
    from .AdjUrbanQTotal_inner_compiled import AdjUrbanQTotal_inner
except ImportError:
    print("Unable to import compiled AdjUrbanQTotal_inner, using slower version")
    from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal_inner import AdjUrbanQTotal_inner


# @time_function
@memoize
# @time_function
def AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil):
    result = zeros((NYrs, 12, 31))
    adj_urban_q_total = 0  # used because this is a buffered variable
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urban_q_total = UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper, ISRR, ISRA)
    urb_area_total = UrbAreaTotal(NRur, NUrb, Area)
    area_total = AreaTotal(NRur, NUrb, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        ## z.adj_urban_q_total = get_value_for_yesterday(z.adj_urban_q_total_1,0,Y,i,j,z.NYrs,z.DaysMonth)
                        adj_urban_q_total *= urb_area_total / area_total
                        # pass
                    else:
                        adj_urban_q_total = urban_q_total[Y][i][j]
                        if Qretention > 0:
                            if urban_q_total[Y][i][j] > 0:
                                if urban_q_total[Y][i][j] <= Qretention * PctAreaInfil:
                                    adj_urban_q_total = 0
                                else:
                                    adj_urban_q_total = urban_q_total[Y][i][j] - Qretention * PctAreaInfil
                    # if urb_area_total > 0:
                    #     adj_urban_q_total = adj_urban_q_total * urb_area_total / area_total
                    # else:
                    #     adj_urban_q_total = 0
                else:
                    pass
                result[Y][i][j] = adj_urban_q_total
    return result


@memoize
def AdjUrbanQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                     ISRR, ISRA, Qretention, PctAreaInfil):
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urban_q_total = UrbanQTotal_f(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA)
    urb_area_total = UrbAreaTotal_f(NRur, NUrb, Area)
    area_total = AreaTotal_f(Area)
    return AdjUrbanQTotal_inner(NYrs, DaysMonth, Temp, Qretention, PctAreaInfil, water, urban_q_total, urb_area_total,
                                area_total)

# @jit
# def AdjUrbanQTotal_f_inner(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
#                    ISRR, ISRA, Qretention, PctAreaInfil,water,urban_q_total,urb_area_total,area_total):
#     result = np.zeros((NYrs, 12, 31))
#     adj_urban_q_total = 0
#     urban_q_total = DAC.ymd_to_daily(urban_q_total, DaysMonth)
#     Temp = DAC.ymd_to_daily(Temp, DaysMonth)
#     water = DAC.ymd_to_daily(water, DaysMonth)
#     for j in range(len(urban_q_total)):
#         if Temp[j] > 0 and water[j] > 0.01:
#             if water[j] <0.05:
#                 pass
#             else:
#                 adj_urban_q_total = urban_q_total[j]
#                 if Qretention > 0 and urban_q_total[j] > 0:
#                     if urban_q_total[j] <= Qretention * PctAreaInfil:
#                         adj_urban_q_total = 0
#                     else:
#                         adj_urban_q_total = urban_q_total[j] - Qretention * PctAreaInfil
#             if urb_area_total > 0:
#                 adj_urban_q_total = adj_urban_q_total * urb_area_total / area_total
#             else:
#                 adj_urban_q_total = 0
#         else:
#             pass
#         result[j] = adj_urban_q_total
#     return DAC.daily_to_ymd(result,NYrs, DaysMonth)
