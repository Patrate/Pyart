from PIL import Image, ImageDraw
from PIL.PngImagePlugin import PngImageFile, PngInfo
import math
import sys, getopt
from random import randint as rint
from libs.colorGradient import colorGradient

def lineText(text, factor = 64, method=Image.ANTIALIAS):
	minRange = 999999
	maxRange = 0
	for c in text:
		val = ord(c) * factor
		if val < minRange:
			minRange = val
		if val > maxRange:
			maxRange = val
	
	valArray = []
	
	for c in text:
		val = int(ord(c) * factor)
		valArray.append(val)
	vmax = len(valArray)
	
	wl = int(math.sqrt(maxRange) + 1)
	
	img = Image.new("RGB", (wl, wl), color = "white")
	colorGradient(img)
	#pixels = img.load()
	draw = ImageDraw.Draw(img)
	
	points = []
	for c in valArray:
		points.append((int(c/wl), int(c%wl)))
	
	draw.polygon(points, outline=(255, 255, 255))
	
	
	img = img.resize((factor*3, factor*3, method))
	return img