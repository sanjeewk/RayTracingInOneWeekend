import numpy as np

class C(np.ndarray):
    def __new__(cls, *args, **kwargs):
        print ('In __new__ with class %s' % cls)
        return np.ndarray.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        # in practice you probably will not need or want an __init__
        # method for your subclass
        print ('In __init__ with class %s' % self.__class__)

    def __array_finalize__(self, obj):
        print ('In array_finalize:')
        print ('   self type is %s' % type(self))
        print ('   obj type is %s' % type(obj))
    

t = C(1,2,3)
print(t)