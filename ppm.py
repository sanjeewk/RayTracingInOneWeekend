import os

def main():
    image_width = 256
    image_height = 256
    image_path = os.path.join(os.path.dirname(__file__),"images","part1.ppm")
    ppm_image = open(image_path, "wt")
    ppm_image.write(f"P3\n{image_width} {image_height}\n255\n")
    for j in range(image_height, -1, -1):
        for i in range(0, image_width, 1):
            r = float(i) / (image_width - 1)
            g = float(j) / (image_height - 1) 
            b = 0.25

            ir = int(255.99*r)
            ig = int(255.99*g)
            ib = int(255.99*b)
            ppm_image.write(f"{ir} {ig} {ib}\n")
    ppm_image.close()

if __name__ == "__main__":
    main()