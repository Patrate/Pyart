import sys, getopt
from PIL import Image
from PIL.PngImagePlugin import PngImageFile, PngInfo
import libs.color as colorScr
import libs.line as lineScr

scriptList = {
	"color": colorScr.colorPatch,
	"line": lineScr.lineText
}

def usage():
	print("python textToImage.py -t <text> -o <output> -s <script>\nAvailable scripts are:")
	print("\t- " + "\n\t- ".join(scriptList.keys()))

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "t:o:s:h", ["text=", "output=", "script=", "help"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print(err)  # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	output = None
	text = None
	script = None
	for o, a in opts:
		if o in ("-t", "--text"):
			text = a
		elif o in ("-o", "--output"):
			output = a
		elif o in ("-s", "--script"):
			script = a
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		else:
			assert False, "unhandled option"
	
	
	img = scriptList[script](text, method=Image.LANCZOS)
	
	metadata = PngInfo()
	metadata.add_itxt("Content", text)

	img.save(output, pnginfo = metadata)

if __name__ == "__main__":
	main()