import math 
import numpy as np

class Vec3:
    def __init__(self, e0, e1, e2):
        self.vector = np.array([e0,e1,e2])

        self.x = self.vector[0]
        self.y = self.vector[1]
        self.z = self.vector[2]

        self.r = self.vector[0]
        self.g = self.vector[1]
        self.b = self.vector[2]

        self.length_squared= np.sum(np.square(self.vector))
        self.length = math.sqrt(self.length_squared)

    def unit_vector(self):
        return self.vector/self.length

    def __add__(self, v2):
        self.vector += v2.vector

    def __sub__(self, v2):
        self.vector -= v2.vector  

    def __mul__(self, n):
        self.vector = n * vector

    def mul(self, v2):
        self.vector = v2.vector * self.vector

    def __truediv__(self, n):
        self.vector = self.vector/n


def dot(v1: Vec3, v2: Vec3) -> int:
    dot = v1 * v2
    return Vec3(dot[0] , dot[1] , dot[2])

def cross(v1: Vec3, v2: Vec3) -> Vec3:
    cross = np.cross(v1.vector,v2.vector)
    return Vec3(cross[0], cross[1], cross[2])

def unit_vector(v: Vec3):
    unit = v1/v1.length
    return Vec3(unit[0], unit[1], unit[2])
