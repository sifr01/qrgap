'''This python code is for use alongside the QRStream app, available in F-Droid
or for creating a qrstream to be transferred to another device.
It is useful for transferring text between devices which are air-gapped for 
security purposes (eg. a 4096 byte key from computer to smartphone)
This version of the script displays the qrstream backwards so that the qrcodes
can be scanned and then closed in the correct order'''

import qrcode
import Image

FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
#FILE_LOCATION = "/home/amnesia/Persistent/keys/o.asc"
FILE = open(FILE_LOCATION,"r")
print "Name of the file: ", FILE.name
TEXT = FILE.read()
LENGTH = 2000

qr = 1
img = 1
a = 0

ARRAY = [TEXT[i:i+LENGTH] 
		for i in range(0, len(TEXT), LENGTH)
	]					#create the array

COUNT = len(ARRAY)				#COUNT = number of elements in the array

while True:					#create a "while loop"
        COUNT -= 1				#one by one, count down through all the array elements
	if COUNT == -1:
		break				#once all the array elements are processed, finish/break
	print ARRAY[COUNT]			#print the array elements as they are processed
	qr = qrcode.QRCode(			#specifies variables for qrcode creation
	    version = None,
	    error_correction = qrcode.constants.ERROR_CORRECT_L,
	    box_size = 4,
	    border = 4,
		)				
	qr.add_data(ARRAY[COUNT])		#inputs text segments to the qrcode object (qr)
	qr.make(fit=True)			#fits qrcode to text
	img = qr.make_image()			#makes image file and assigns it to 'img'
	img.show()				#shows the made image file
