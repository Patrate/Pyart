from PIL import Image, ImageDraw
from PIL.PngImagePlugin import PngImageFile, PngInfo
import math
import sys, getopt
from random import randint as rint, seed

def colorPatch(text, size=256, method=Image.ANTIALIAS):
	wl = round(math.sqrt(len(text)) + .5)
	img = Image.new("RGB", (wl, wl), color = "white")
	pixels = img.load()
	
	valArray = []
	
	for c in text:
		seed(ord(c))
		for i in range(3):
			valArray.append(rint(0, 255))
	
	sh = 0
	while len(valArray)/3 < (wl * wl):
		sh += 1
		valArray.append(255)
	#sh = sh/3
	
	k = 0
	for i in range(img.size[0]): # for every pixel:
		for j in range(img.size[1]):
			pixels[i, j] = (valArray[k], valArray[k+1], valArray[k+2])
			k += 3
	#HAMMING or BICUBIC
	img = img.resize((size, size), Image.BICUBIC)#method)
	
	pixels = img.load()
	step = int(img.size[0]/(wl))
	
	k=0
	for i in range(int(step/2), img.size[0], step): # for every pixel:
		if(len(valArray) <= k):
			break
		for j in range(int(step/2), img.size[1], step):
			if(len(valArray) <= k):
				break
			pixels[i, j] = (valArray[k], valArray[k+1], valArray[k+2])
			k += 3
	print(wl)
	return img