# from Timer import time_function
from numpy import sum

@time_function
def old_way(z):
    for Y in range(z.NYrs):
        for i in range(12):
            z.AvDisNitr[i] += z.DisNitr[Y][i] / z.NYrs
            z.AvTotNitr[i] += z.TotNitr[Y][i] / z.NYrs
            z.AvDisPhos[i] += z.DisPhos[Y][i] / z.NYrs
            z.AvTotPhos[i] += z.TotPhos[Y][i] / z.NYrs
            z.AvGroundNitr[i] += z.GroundNitr[Y][i] / z.NYrs
            z.AvGroundPhos[i] += z.GroundPhos[Y][i] / z.NYrs
            z.AvAnimalN[i] += z.AnimalN[Y][i] / z.NYrs
            z.AvAnimalP[i] += z.AnimalP[Y][i] / z.NYrs

            z.AvGRLostBarnN[i] += z.GRLostBarnN[Y][i] / z.NYrs
            z.AvGRLostBarnP[i] += z.GRLostBarnP[Y][i] / z.NYrs
            z.AvGRLostBarnFC[i] += z.GRLostBarnFC[Y][i] / z.NYrs

            z.AvNGLostBarnN[i] += z.NGLostBarnN[Y][i] / z.NYrs
            z.AvNGLostBarnP[i] += z.NGLostBarnP[Y][i] / z.NYrs
            z.AvNGLostBarnFC[i] += z.NGLostBarnFC[Y][i] / z.NYrs

            z.AvNGLostManP[i] += z.NGLostManP[Y][i] / z.NYrs

            # Average pathogen totals
            z.AvAnimalFC[i] += z.AnimalFC[Y][i] / z.NYrs
            z.AvWWOrgs[i] += z.WWOrgs[Y][i] / z.NYrs
            z.AvSSOrgs[i] += z.SSOrgs[Y][i] / z.NYrs
            z.AvUrbOrgs[i] += z.UrbOrgs[Y][i] / z.NYrs
            z.AvWildOrgs[i] += z.WildOrgs[Y][i] / z.NYrs
            z.AvTotalOrgs[i] += z.TotalOrgs[Y][i] / z.NYrs


@time_function
def numpy1(z):
    z.AvDisNitr = sum(z.DisNitr, axis=0) / z.NYrs
    z.AvTotNitr = sum(z.TotNitr, axis=0) / z.NYrs
    z.AvDisPhos = sum(z.DisPhos, axis=0) / z.NYrs
    z.AvTotPhos = sum(z.TotPhos, axis=0) / z.NYrs
    z.AvGroundNitr = sum(z.GroundNitr, axis=0) / z.NYrs
    z.AvGroundPhos = sum(z.GroundPhos, axis=0) / z.NYrs
    z.AvAnimalN = sum(z.AnimalN, axis=0) / z.NYrs
    z.AvAnimalP = sum(z.AnimalP, axis=0) / z.NYrs

    z.AvGRLostBarnN = sum(z.GRLostBarnN, axis=0) / z.NYrs
    z.AvGRLostBarnP = sum(z.GRLostBarnP, axis=0) / z.NYrs
    z.AvGRLostBarnFC = sum(z.GRLostBarnFC, axis=0) / z.NYrs

    z.AvNGLostBarnN = sum(z.NGLostBarnN, axis=0) / z.NYrs
    z.AvNGLostBarnP = sum(z.NGLostBarnP, axis=0) / z.NYrs
    z.AvNGLostBarnFC = sum(z.NGLostBarnFC, axis=0) / z.NYrs

    z.AvNGLostManP = sum(z.NGLostManP, axis=0) / z.NYrs

    # Average pathogen totals
    z.AvAnimalFC = sum(z.AnimalFC, axis=0) / z.NYrs
    z.AvWWOrgs = sum(z.WWOrgs, axis=0) / z.NYrs
    z.AvSSOrgs = sum(z.SSOrgs, axis=0) / z.NYrs
    z.AvUrbOrgs = sum(z.UrbOrgs, axis=0) / z.NYrs
    z.AvWildOrgs = sum(z.WildOrgs, axis=0) / z.NYrs
    z.AvTotalOrgs = sum(z.TotalOrgs, axis=0) / z.NYrs


@time_function
def numpy2(z):
    temp = vstack((z.DisNitr, z.TotNitr, z.DisPhos, z.TotPhos, z.GroundNitr, z.GroundPhos, z.AnimalN, z.AnimalP,
                      z.GRLostBarnN, z.GRLostBarnP, z.GRLostBarnFC, z.NGLostBarnN, z.NGLostBarnP, z.NGLostBarnFC,
                      z.NGLostManP, z.AnimalFC, z.WWOrgs, z.SSOrgs, z.UrbOrgs, z.WildOrgs, z.TotalOrgs))
    temp2 = sum(temp.reshape(-1, 15, 12), axis=1) / z.NYrs
    z.AvDisNitr = temp2[0]
    z.AvTotNitr = temp2[1]
    z.AvDisPhos = temp2[2]
    z.AvTotPhos = temp2[3]
    z.AvGroundNitr = temp2[4]
    z.AvGroundPhos = temp2[5]
    z.AvAnimalN = temp2[6]
    z.AvAnimalP = temp2[7]

    z.AvGRLostBarnN = temp2[8]
    z.AvGRLostBarnP = temp2[9]
    z.AvGRLostBarnFC = temp2[10]

    z.AvNGLostBarnN = temp2[11]
    z.AvNGLostBarnP = temp2[12]
    z.AvNGLostBarnFC = temp2[13]

    z.AvNGLostManP = temp2[14]

    # Average pathogen totals
    z.AvAnimalFC = temp2[15]
    z.AvWWOrgs = temp2[16]
    z.AvSSOrgs = temp2[17]
    z.AvUrbOrgs = temp2[18]
    z.AvWildOrgs = temp2[19]
    z.AvTotalOrgs = temp2[20]
