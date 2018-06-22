# from Timer import time_function
from gwlfe.enums import YesOrNo
from gwlfe.Memoization import memoize

@memoize
def GrazingAnimal(GrazingAnimal_0):
    return GrazingAnimal_0

@memoize
def GrazingAnimal_f(GrazingAnimal_0):
    return GrazingAnimal_0 == YesOrNo.YES
