from PIL import Image, ImageDraw
from PIL.PngImagePlugin import PngImageFile, PngInfo
import math
import sys, getopt
from random import randint as rint

def colorGradient(img):
	draw = ImageDraw.Draw(img)
	width = img.width
	height = img.height

	colors = []
	for i in range(0, 12):
		colors.append((rint(0,255), rint(0,255), rint(0,255)))
	
	partSize = int(width/(len(colors) - 1) + 1)
	for i in range(0, len(colors) - 1 ):
		r, g, b = colors[i][0], colors[i][1], colors[i][2]
		rDif = (colors[i+1][0] - colors[i][0]) / partSize
		gDif = (colors[i+1][1] - colors[i][1]) / partSize
		bDif = (colors[i+1][2] - colors[i][2]) / partSize
		for j in range(partSize):
			r, g, b = r + rDif, g + gDif, b + bDif
			
			draw.line((j + partSize * i,0,j + partSize * i,height), fill=(int(r),int(g),int(b)))