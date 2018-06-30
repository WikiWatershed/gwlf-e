from numba.pycc import CC
from numpy import zeros

cc = CC('AdjUrbanQTotal_inner_compiled')


@cc.export('AdjUrbanQTotal_inner',
           '(int64, int64[:,::1], float64[:,:,::1], float64, float64, float64[:,:,::1], float64[:,:,::1], float64, float64)')
def AdjUrbanQTotal_inner(NYrs, DaysMonth, Temp, Qretention, PctAreaInfil, water, urban_q_total, urb_area_total,
                         area_total):
    result = zeros((NYrs, 12, 31))
    adj_urban_q_total = 0
    for Y in range(NYrs):
        for i in range(12):

            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        # z.adj_urban_q_total = get_value_for_yesterday(z.adj_urban_q_total_1,0,Y,i,j,z.NYrs,z.DaysMonth)
                        # pass
                        adj_urban_q_total *= urb_area_total / area_total
                    else:
                        adj_urban_q_total = urban_q_total[Y][i][j]
                        if Qretention > 0 and urban_q_total[Y][i][j] > 0:
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
