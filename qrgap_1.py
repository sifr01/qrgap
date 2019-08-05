import qrcode
import Image
import os

FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
FILE = open(FILE_LOCATION,"r")
print "Name of the file: ", FILE.name

qr = 1

while True:
        TEXT = FILE.read(2000)
        if TEXT == '': 
		break
	print TEXT
	qr = qrcode.QRCode(
	    version = None,
	    error_correction = qrcode.constants.ERROR_CORRECT_L,
	    box_size = 4,
	    border = 4,
		)
	qr.add_data(TEXT)
	qr.make(fit=True)			#
	img = qr.make_image()			#
	img.show()				#shows the made image file
