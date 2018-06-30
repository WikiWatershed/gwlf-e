from gwlfe.Memoization import memoize
from gwlfe.enums import YesOrNo


@memoize
def GrazingAnimal(GrazingAnimal_0):
    return GrazingAnimal_0


@memoize
def GrazingAnimal_f(GrazingAnimal_0):
    return GrazingAnimal_0 == YesOrNo.YES
