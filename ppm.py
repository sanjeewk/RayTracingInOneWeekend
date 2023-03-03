import os
from vector import *

def main():
    image_width = 256
    image_height = 256
    image_path = os.path.join(os.path.dirname(__file__),"images/ppm","part1.ppm")
    ppm_image = open(image_path, "wt")
    ppm_image.write(f"P3\n{image_width} {image_height}\n255\n")
    for j in range(image_height, -1, -1):
        for i in range(0, image_width, 1):
            colour = Vec3(float(i)/float(image_height), float(j)/float(image_width), 0.2)
            ir = int(255.99*colour.r)
            ig = int(255.99*colour.g)
            ib = int(255.99*colour.b)
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()

if __name__ == "__main__":
    main()