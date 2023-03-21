
from abc import ABC, abstractmethod
from vector import *
import random
from ray import Ray

# get a random point inside a unit radius sphere centred at origin
def random_in_unit_sphere():

    p = Vec3(random.random(), random.random(), random.random())*2 - Vec3(1.0, 1.0, 1.0)
    while p.length_squared >= 1.0:
        p = Vec3(random.random(), random.random(), random.random())*2 - Vec3(1.0, 1.0, 1.0)
    return p


def reflect(in_vector, normal):

    return in_vector - normal * (dot(in_vector, normal) * 2)


class Material(ABC):
    @abstractmethod
    def scatter(self, ray_in, hit_record, scattered):
        pass


class Lambertian(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit_record, scattered):
        target = hit_record.p + hit_record.normal + random_in_unit_sphere()
        scattered.origin = hit_record.p
        scattered.direction = target - hit_record.p
        return True, self.albedo


class Metal(Material):

    def __init__(self, albedo, fuzz):
        self.albedo = albedo
        if fuzz < 1: self.fuzz = fuzz
        else: self.fuzz = 1

    def scatter(self, ray_in, hit_record, scattered):
        reflected = reflect(unit_vector(ray_in.direction), hit_record.normal)
        scattered.origin = hit_record.p
        scattered.direction = reflected + random_in_unit_sphere() * self.fuzz
        return dot(scattered.direction, hit_record.normal) > 0, self.albedo