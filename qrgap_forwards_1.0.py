'''This python code is for use alongside the QRStream app, available in F-Droid
or for creating a qrstream to be transferred to another device.
It is useful for transferring text between devices which are air-gapped for
security purposes (eg. a 4096 byte key from computer to smartphone)'''

import qrcode
import Image

#FILE_LOCATION = "/home/amnesia/Persistent/keys/o.asc"
FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
FILE = open(FILE_LOCATION,"r")
print "Name of the file: ", FILE.name

while True:
	TEXT = FILE.read(2000)
        if TEXT == '': 
		break				#if there is no more text left to process then finish/break
	print TEXT				#print the text that is currently being processed
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
