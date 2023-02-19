import os 
import cv2 
import sys
from glob import glob 

args = sys.argv
cwd = os.getcwd()
input = os.path.join(cwd, f"ppm/{args[1]}.ppm")    
output = os.path.join(cwd, f"png/{args[1]}.png")   

cv2.imwrite(output, cv2.imread(input))