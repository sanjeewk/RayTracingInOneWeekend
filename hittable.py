from abc import ABC, abstractmethod
from vector import Vec3

class Hittable(ABC):
    @abstractmethod
    def hit(self, ray, t_min, t_max, hit_record):
        pass

class HitRecord:
    def __init__(self, t=0.0, p=Vec3(0.0, 0.0, 0.0), normal=Vec3(0.0, 0.0, 0.0)):
        self.t = t
        self.p = p
        self.normal = normal
        self.material = None