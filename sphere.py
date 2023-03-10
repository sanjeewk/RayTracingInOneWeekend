from hittable import Hittable
import math
from vector import *
from ray import Ray


class Sphere(Hittable):

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, ray, t_min, t_max, hit_record):
        oc = ray.origin - self.center
        a = dot(ray.direction, ray.direction)
        b = dot(oc, ray.direction)
        c = dot(oc, oc) - self.radius*self.radius
        discriminant = b*b - a*c
        if discriminant > 0.0:
            temp = (-b - math.sqrt(discriminant))/a
            if t_min < temp < t_max:
                hit_record.t = temp
                hit_record.p = ray.point(hit_record.t)
                hit_record.normal = (hit_record.p - self.center)/self.radius
                return True
            temp = (-b + math.sqrt(discriminant))/a
            if t_min < temp < t_max:
                hit_record.t = temp
                hit_record.p = ray.point(hit_record.t)
                hit_record.normal = (hit_record.p - self.center)/self.radius
                return True
        else:
            return False