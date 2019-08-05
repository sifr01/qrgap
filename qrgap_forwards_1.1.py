'''This python code is for use alongside the QRStream app, available in F-Droid
or for creating a qrstream to be transferred to another device.
It is useful for transferring text between devices which are air-gapped for
security purposes (eg. a 4096 byte key from computer to smartphone)'''

import qrcode
import Image

#FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
FILE_LOCATION = "/home/amnesia/Persistent/keys/o.asc"		#for debugging purposes
FILE = open(FILE_LOCATION,"r")
#print "Name of the file: ", FILE.name				#for debugging purposes
TEXT = FILE.read()
LENGTH = 2567							#QRCodes can hold a maximum of 2593 bytes, but more than 2567 and python returns "qrcode.exceptions.DataOverflowError"

ARRAY = [TEXT[i:i+LENGTH] 
		for i in range(0, len(TEXT), LENGTH)
	]						#create the array

for (INDEX,CHUNK) in enumerate(ARRAY):			#cycle forwards through the array elements
	print(str(CHUNK) )				#print the array elements as they are processed (somewhat for debugging purposes)
	qr = qrcode.QRCode(				#specifies variables for qrcode creation
	    version = None,
	    error_correction = qrcode.constants.ERROR_CORRECT_L,
	    box_size = 3.5,			#default was set to 4 but this was reduced so that QRcode would fit on a smaller screen size
	    border = 4,
		)				
	qr.add_data(CHUNK)				#inputs text segments to the qrcode object (qr)
	qr.make(fit=True)				#fits qrcode to text
	img = qr.make_image()				#makes image file and assigns it to 'img'
	img.show()					#shows the made image file
