import qrcode
import Image
import os

FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
FILE = open(FILE_LOCATION,"r")
print "Name of the file: ", FILE.name
COUNT = 100

qr = 1




while True:
#	COUNT = COUNT - 1
	FILE.seek(os.SEEK_END)	#start at the end of the file
        SEG = FILE.read(2000)
	if SEG == '': 
		break
	print SEG
	qr = qrcode.QRCode(
	    version = None,
	    error_correction = qrcode.constants.ERROR_CORRECT_L,
	    box_size = 4,
	    border = 4,
		)
	qr.add_data(SEG)
	qr.make(fit=True)			#
	img = qr.make_image()			#
	img.show()				#shows the made image file






