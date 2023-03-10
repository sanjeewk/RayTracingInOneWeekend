import os
import random
import sys

from vector import *
from ray import Ray
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord
from camera import Camera



def colour(r: Ray, world):
    hit_record = HitRecord()
    if world.hit(r, 0.0, sys.float_info.max, hit_record):
        return Vec3(hit_record.normal.x + 1.0, hit_record.normal.y + 1.0, hit_record.normal.z + 1.0)*0.5
    else:
        unit_direction = unit_vector(r.direction)
        t = 0.5 * (unit_direction.y + 1.0)
        # Lerping 
        return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t


def main():
    path = os.path.join(os.path.dirname(__file__), "images/ppm/", "step6.ppm")
    ppm_image = open(path, 'wt')
    # Image
    image_width = 400
    image_height = 200
    samples_per_pixel = 100
    
    title = (f"P3\n{image_width} {image_height}\n255\n")

    ppm_image.write(title)
    camera = Camera()

    object_list = [Sphere(Vec3(0.0, 0.0, -1.0), 0.5), Sphere(Vec3(0.0, -100.5, -1.0), 100.0)]
    world = Hittable_List(object_list)

    for j in range(image_height-1, -1, -1):
        print(j)
        for i in range(0, image_width, 1):
            col = Vec3(0.0, 0.0, 0.0)
            for s in range(0, samples_per_pixel):
                u = float(i + + random.random())/float(image_width)
                v = float(j + + random.random())/float(image_height)
                r = camera.get_ray(u, v)
                col += colour(r, world)

            col /= samples_per_pixel
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            # print(f"{ir} {ig} {ib}\n")
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()


if __name__ == '__main__':
    main()