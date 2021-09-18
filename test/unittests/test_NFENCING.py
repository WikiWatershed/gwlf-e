import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NFENCING


class TestNFENCING(VariableUnitTest):
    def test_NFENCING(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NFENCING.NFENCING_f(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                z.AnimalDailyN, z.n42, z.n45, z.n69),
            NFENCING.NFENCING(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                              z.AnimalDailyN, z.n42, z.n45, z.n69), decimal=7)
