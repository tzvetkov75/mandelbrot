#
#   This make Mandelbrot set and save it as pictire
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

# consts
picWidth,picHeight= 500, 500
reMin, reMax = -2,1
imMin, imMax = -1,1
filenameInteraction = "output/mandelbrotNormal.bmp"
fileNameDensity = "output/mandelbrotDensity.bmp"


data = np.ones((picWidth,picHeight)) * 0
dataDensity = np.ones((picWidth,picHeight)) * 0

def evaluate(re,im):
# evaluates if the point is finite
    c = complex(re,im)
    i=0
    z=complex(0,0)
    while (abs(z)<3) and (i<500):
        z=z*z + c
        i=i+1
    return i

for x in range(0, picWidth):
    for y in range(0, picHeight):
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

# density map
# TBD
#imDensity = Image.fromarray(dataDensity)
#imDensity = im.convert("RGB")
#imDensity.save(fileNameDensity)
#imDensity.show()
