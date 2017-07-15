#
#   This make Mandelbrot set and save it as picture
#
#         - normal way - counting the interaction to bail out to  infinity
#         - showing the dark side - making a density map
#
#    Edit the constants to map to your enviroments
#
# INSTALLATION
#
#     - you need a python
#     - python modules python and PIL
#
#
#   Autor: Vesselin Tzvetkov 2017
#   Licence: Apache 2.0
#
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# consts
picWidth,picHeight= 500, 500
reMin, reMax = -2,1
imMin, imMax = -1,1
filenameInteraction = "output/mandelbrotNormal.bmp"
filenameDensity = "output/mandelbrotDensity.bmp"


# global variable

data = np.ones((picWidth,picHeight)) * 0
dataDensity = np.ones((picWidth,picHeight)) * 0

# here we store all points. One dimensional array with complex numbers
points = []



def evaluate(re,im):
# evaluates if the point is finite
    c = complex(re,im)
    i=0
    z=complex(0,0)
    while (abs(z)<3) and (i<500):
        points.append(z)
        z=z*z + c
        i=i+1
    return i

def generateDensityMap ():
# this generate density map
# the bin siye of the histogram is the picture point
    for i in range(len(points)):
        # generate from complex number the coordinates in the pic
        picX =int( (-reMin+points[i].real) * picWidth / (-reMin+reMax) )
        picY =int( (-imMin+points[i].imag) * picHeight / (-imMin+imMax) )

        if (picX<picWidth) and (picY<picHeight):
            dataDensity[picX][picY] += 1


for x in range(0, picWidth):
    for y in range(0, picHeight):
        # generate from point in the pic them complex number
        reX=reMin + x * (-reMin + reMax ) / picWidth
        reY=imMin + y * (-imMin + imMax ) / picHeight
        color=evaluate(reX,reY)*10
        data [x][y]=color
# TBD 

# Interaction map
im = Image.fromarray(data)
im = im.convert("RGB")
im.save(filenameInteraction)
im.show()

# generate and show the density map
generateDensityMap()
imDensity = Image.fromarray(dataDensity)
imDensity = imDensity.convert("RGB")
imDensity.save(filenameDensity)
imDensity.show()
