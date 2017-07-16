#
#   This make Mandelbrot set and save it as picture
#
#         - normal way - counting the interaction to bail out to  infinity
#         - showing the dark side - making a density map
#         - making overlay of normal and density map
#
#    Edit the constants to map to your enviroments
#
# INSTALLATION
#
#     - you need a python
#     - python modules python and PIL
#
#   TBD: nice heat map
#
#   Autor: Vesselin Tzvetkov 2017
#   Licence: Apache 2.0
#
import numpy as np
from PIL import Image
from PIL import ImageOps


# consts
picWidth,picHeight= 500, 500
reMin, reMax = -2,1
imMin, imMax = -1,1
filenameInteraction = "output/mandelbrotNormal.bmp"

filenameDensity = "output/mandelbrotDensity.bmp"
filenameOverlay = "output/mandelbrotOverlay.bmp"


# global variable

data = np.ones((picWidth,picHeight)) * 0
# TBD not used for now, but nice colors are always good
dataRGB = np.ones((picWidth,picHeight,3), 'uint8') * 0

dataDensity = np.ones((picWidth,picHeight)) * 1

# here we store all points. One dimensional array with complex numbers
points = []
tmp=[]


def evaluate(re,im):
# evaluates if the point is finite
    c = complex(re,im)
    i,c1,c2,c3 =0,0,0,0
    z=complex(0,0)

    while (abs(z)<3) and (i<1000):
        if z!=complex(0,0):
            points.append(z)

        z=z*z + c
        i=i+1
    return i,c1,c2,c3

def generateDensityMap ():
# this generate density map
# the bin siye of the histogram is the picture point
    for i in range(len(points)):
        # generate from complex number the coordinates in the pic
        picX =int( (-reMin+points[i].real) * picWidth / (-reMin+reMax) )
        picY =int( (-imMin+points[i].imag) * picHeight / (-imMin+imMax) )

        if (picX<picWidth) and (picY<picHeight):
            dataDensity[picX][picY] *= 1.05


for x in range(0, picWidth):
    for y in range(0, picHeight):
        # generate from point in the pic them complex number
        reX=reMin + x * (-reMin + reMax ) / picWidth
        reY=imMin + y * (-imMin + imMax ) / picHeight
        color,c1,c2,c3 =evaluate(reX,reY)
        # TBD, to be scaled
        data [x][y]=color*7


# Interaction map
im = Image.fromarray(data).convert("RGB")
im = ImageOps.invert(im)
im.save(filenameInteraction)
im.show()


# generate and show the density map
generateDensityMap()
imDensity = Image.fromarray(dataDensity).convert("RGB")
imDensity = ImageOps.invert(imDensity)
imDensity.save(filenameDensity)
imDensity.show()

# make an overlay of normal and density
imOverlay = Image.blend(im, imDensity, 0.3)
imOverlay.show()
imOverlay.save(filenameOverlay)
