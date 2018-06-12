from random import randint

from numpy import asarray
from numpy import ndarray


class HashableArray(ndarray):
    def __new__(cls, input_array):
        obj = asarray(input_array).view(cls)
        obj.hash = randint(100, 999)
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.hash = getattr(obj, 'info', None)

    def __hash__(self):
        return self.hash

    def __repr__(self):
        return str(self.hash)

    # def __getitem__(self, item):
    #     # print(self.name + "[" + str(item) + "]")
    #     attr = np.ndarray.__getitem__(self, item)
    #     if issubclass(type(attr), np.ndarray):  # handle multi dimensional arrays
    #         return ArraySpy(attr, self.name, self.gets, self.sets)
    #     else:
    #         caller = inspect.currentframe().f_back
    #         object.__getattribute__(self, "gets").append(
    #             [self.name, caller.f_code.co_filename.split("\\")[-1], str(caller.f_lineno)])
    #         return attr
    #
    # def __setitem__(self, key, value):
    #     # print(self.name,value)
    #     caller = inspect.currentframe().f_back
    #     self.sets.append(
    #         [self.name, type(value).__name__, caller.f_code.co_filename.split("\\")[-1], caller.f_lineno])
    #     np.ndarray.__setitem__(self, key, value)