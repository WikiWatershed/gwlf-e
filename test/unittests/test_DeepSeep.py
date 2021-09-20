from .VariableUnitTest import VariableUnitTest


class TestDeepSeep(VariableUnitTest):
    pass
    #     input_file = open('unittests/input_4.gms', 'r')
    #     self.z = Parser.GmsReader(input_file).read()
    #
    #
    # def test_DeepSeep(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         DeepSeep.DeepSeep_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
    #                             z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
    #                             z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef),
    #         DeepSeep.DeepSeep(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
    #                             z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
    #                             z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef), decimal=7)
