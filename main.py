import os
from vector import *
from ray import Ray


def colour(r: Ray):
    unit_direction = unit_vector(r.direction)
    t = 0.5*(unit_direction.y + 1.0)
    return Vec3(1.0, 1.0, 1.0)*(1.0-t) + Vec3(0.0, 0.0, 1.0)*t

def main():
    path = os.path.join(os.path.dirname(__file__), "images/ppm/", "step3.ppm")
    ppm_image = open(path, 'wt')
    # Image
    image_width = 400
    image_height = 225
    
    title = (f"P3\n{image_width} {image_height}\n255\n")
    lower_left_corner = Vec3(-2.0, -1.0, -1.0)
    horizontal = Vec3(4.0, 0.0, 0.0)
    vertical = Vec3(0.0, 2.0, 0.0)

    ppm_image.write(title)

    for j in range(image_height-1, -1, -1):
        for i in range(0, image_width, 1):
            u = float(i)/float(image_width)
            v = float(j)/float(image_height)
            r = Ray(Vec3(0.0, 0.0, 0.0), lower_left_corner + horizontal*u + vertical*v)
            col = colour(r)
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()


if __name__ == '__main__':
    main()