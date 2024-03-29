import os
import random
import sys
import time 

from vector import *
from ray import Ray
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord
from camera import Camera
from material import *

# def random_in_unit_sphere():
#     p = Vec3(random.random(), random.random(), random.random())*2 - Vec3(1.0, 1.0, 1.0)
#     while p.length_squared >= 1.0:
#         p = Vec3(random.random(), random.random(), random.random())*2 - Vec3(1.0, 1.0, 1.0)
#     return p

def colour(r: Ray, world, depth):
    hit_record = HitRecord()
    
    if world.hit(r, 0.001, sys.float_info.max, hit_record):
        scattered = Ray(origin=Vec3(0.0, 0.0, 0.0), direction=Vec3(0.0, 0.0, 0.0))
        hit = hit_record.material.scatter(r, hit_record, scattered)
        if depth >= 0 and hit[0]:
            return colour(scattered, world, depth-1).mul(hit[1])
        else:
            return Vec3(0.0, 0.0, 0.0)
    else:
        unit_direction = unit_vector(r.direction)
        t = 0.5 * (unit_direction.y + 1.0)
        # Lerping 
        return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t


def main():
    path = os.path.join(os.path.dirname(__file__), "images/ppm/", "step8.ppm")
    ppm_image = open(path, 'wt')
    # Image
    image_width = 400
    image_height = 200
    samples_per_pixel = 100
    max_depth = 50  # max depth for recursion

    title = (f"P3\n{image_width} {image_height}\n255\n")
    ppm_image.write(title)
    camera = Camera()

    object_list = [Sphere(Vec3(0.0, 0.0, -1.0), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3))),
                   Sphere(Vec3(0.0, -100.5, -1.0), 100.0, Lambertian(Vec3(0.8, 0.8, 0))),
                   Sphere(Vec3(1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.6, 0.2), fuzz=1.0)),
                   Sphere(Vec3(-1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.8, 0.8), fuzz=0.3))]
    world = Hittable_List(object_list)

    for j in range(image_height-1, -1, -1):
        print(j)
        for i in range(0, image_width, 1):
            col = Vec3(0.0, 0.0, 0.0)
            for s in range(0, samples_per_pixel):
                u = float(i + + random.random())/float(image_width)
                v = float(j + + random.random())/float(image_height)
                r = camera.get_ray(u, v)
                col += colour(r, world, max_depth)

            col /= samples_per_pixel
            scale = 1.0 / samples_per_pixel
            col = Vec3(math.sqrt( col.r), math.sqrt( col.g), math.sqrt( col.b))
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            # print(f"{ir} {ig} {ib}\n")
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()


if __name__ == '__main__':
    main()