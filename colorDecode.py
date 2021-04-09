from PIL import Image, ImageDraw
from PIL.PngImagePlugin import PngImageFile, PngInfo
import math
import sys, getopt
from random import randint as rint, seed

dic = {}
for i in range(0, 999):
	seed(i)
	tmp = []
	for _ in range(3):
		tmp.append(rint(0, 255))
	dic[i] = tmp

def colorDecode(file, size):
	img = Image.open(file)
	pixels = img.load()
	
	step = int(img.size[0]/size)
	
	#print("STEP = ", step)
	
	importantPixels = []
	for i in range(int(step/2), img.size[0], step): # for every pixel:
		for j in range(int(step/2), img.size[1], step):
			importantPixels.append(pixels[i, j])
	
	#print(importantPixels)
	
	txtbck = ""
	for pix in importantPixels:
		for c in dic:
			if dic[c][0] == pix[0] and dic[c][1] == pix[1] and dic[c][2] == pix[2]:
				txtbck += chr(c)
				break
	print(txtbck)

if __name__ == "__main__":
	colorDecode(sys.argv[1], int(sys.argv[2]))