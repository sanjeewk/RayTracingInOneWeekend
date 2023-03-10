import os
from vector import *
from ray import Ray
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord
import sys

# def hit_sphere(center: Vec3, radius: float, ray: Ray):
#     oc = ray.origin - center
#     a = dot(ray.direction, ray.direction)
#     b =  dot(ray.direction, oc) * 2.0
#     c = dot(oc, oc) - radius*radius
#     discriminant = b*b - 4*a*c
#     if discriminant < 0:
#         return -1.0
#     else:
#         return float((-b - math.sqrt(discriminant))/(2*a))

def colour(r: Ray, world):
    hit_record = HitRecord()
    if world.hit(r, 0.0, sys.float_info.max, hit_record):
        return Vec3(hit_record.normal.x + 1.0, hit_record.normal.y + 1.0, hit_record.normal.z + 1.0)*0.5
    else:
        unit_direction = unit_vector(r.direction)
        # Graphics trick of scaling it to 0.0 < y < 1.0
        t = 0.5 * (unit_direction.y + 1.0)
        # Lerping between (255, 255, 255) which is white to a light shade blue (128, 255*0.7, 255)
        return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

    # t = hit_sphere(Vec3(0.0, 0.0, -1.0), 0.5, r)
    # if t > 0.0:
    #     N = unit_vector(r.point(t) - Vec3(0.0, 0.0, -1.0))
    #     return Vec3(N.x + 1.0, N.y + 1.0, N.z + 1.0) * 0.5    

    # unit_direction = unit_vector(r.direction)
    # t = 0.5*(unit_direction.y + 1.0)
    # return Vec3(1.0, 1.0, 1.0)*(1.0-t) + Vec3(0.5, 0.7, 1.0)*t

def main():
    path = os.path.join(os.path.dirname(__file__), "images/ppm/", "step5.ppm")
    ppm_image = open(path, 'wt')
    # Image
    image_width = 400
    image_height = 200
    
    title = (f"P3\n{image_width} {image_height}\n255\n")
    lower_left_corner = Vec3(-2.0, -1.0, -1.0)
    horizontal = Vec3(4.0, 0.0, 0.0)
    vertical = Vec3(0.0, 2.0, 0.0)

    ppm_image.write(title)

    object_list = [Sphere(Vec3(0.0, 0.0, -1.0), 0.5), Sphere(Vec3(0.0, -100.5, -1.0), 100.0)]
    world = Hittable_List(object_list)

    for j in range(image_height-1, -1, -1):
        for i in range(0, image_width, 1):
            u = float(i)/float(image_width)
            v = float(j)/float(image_height)
            r = Ray(Vec3(0.0, 0.0, 0.0), lower_left_corner + horizontal*u + vertical*v)
            col = colour(r, world)
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()


if __name__ == '__main__':
    main()