#!/usr/bin/env python

'''This python code is for use alongside the QRStream app, available in F-Droid
or for creating a qrstream to be transferred to another device.
It is useful for transferring text between devices which are air-gapped for
security purposes (eg. a 4096 byte key from computer to smartphone)
This version of the script displays the qrstream backwards so that the qrcodes
can be scanned and then closed in the correct order'''

from __future__ import print_function
import qrcode
from PIL import Image

import sys
if len(sys.argv) < 2:
	print("USAGE: ./thisscript.py <text file>")	
	import os
	os._exit(1)

FILE_LOCATION = sys.argv[1]

with open(FILE_LOCATION, 'r') as file:
    TEXT = file.read()

MAX_QRCODE_LENGTH = 2567  #QRCodes can hold a maximum of 2593 bytes, but more than 2567 and python returns "qrcode.exceptions.DataOverflowError". Is it sending secret messages?! :D

ARRAY = [TEXT[i:i+MAX_QRCODE_LENGTH] for i in range(0, len(TEXT), MAX_QRCODE_LENGTH)] #create the array <- useless comment :D

for INDEX, CHUNK in reversed(list(enumerate(ARRAY))):   #cycle backwards through the array elements <- useless comment
        print(str(CHUNK) )                              #print the array elements as they are processed (somewhat for debugging purposes)
        qr = qrcode.QRCode(                             #specifies variables for qrcode creation
            version = None,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 3.5,                     	#default was set to 4 but this was reduced so that QRcode would fit on a smaller screen size
            border = 4,
                )
        qr.add_data(CHUNK)                              #inputs text segments to the qrcode object (qr) <- useless comment
        qr.make(fit=True)                               #fits qrcode to text
        img = qr.make_image()                           #makes image file and assigns it to 'img' <- useless comment
        img.show()                                      #shows the made image file <- useless comment
