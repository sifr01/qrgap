#!/usr/bin/env python

'''This python code is for use alongside the QRStream app, available in F-Droid
or for creating a qrstream to be transferred to another device.
It is useful for transferring text between devices which are air-gapped for
security purposes (eg. a 4096 byte key from computer to smartphone)
This version of the script displays the qrstream backwards so that the qrcodes
can be scanned and then closed in the correct order'''

# this seems to be written for python2 but you use print as if it's a function hence:
from __future__ import print_function
import qrcode
# needed to change it to below for newer versions of Pillow?
from PIL import Image

# general comment: it's common to use lowercase for variables and uppercase for constants (variables that never change)


# FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
# raw_input is annoying, also was renamed to just input in python3
# I would suggest:
import sys
import os
if sys.argv < 2:
    print('USAGE: ./heniciyuhe <text file>')
    os.exit(1)
FILE_LOCATION = sys.argv[1]

# It's bad practice to leave commented out code, even for debugging
# FILE_LOCATION = "/home/amnesia/Persistent/keys/o.asc"          #for debugging purposes
#FILE = open(FILE_LOCATION,"r")
#print "Name of the file: ", FILE.name                          #for debugging purposes
#TEXT = FILE.read()
# normally in python you do
with open(FILE_LOCATION, 'r') as file:
    TEXT = file.read()
# which will close the file for you, you can also close it with file.close() instead
MAX_QRCODE_LENGTH = 2567  #QRCodes can hold a maximum of 2593 bytes, but more than 2567 and python returns "qrcode.exceptions.DataOverflowError". Is it sending secret messages?! :D

ARRAY = [TEXT[i:i+MAX_QRCODE_LENGTH] for i in range(0, len(TEXT), MAX_QRCODE_LENGTH)] #create the array <- useless comment :D

# i don't think you make use of INDEX so you can leave off `enumerate` and `list`
for INDEX, CHUNK in reversed(list(enumerate(ARRAY))):   #cycle backwards through the array elements <- useless comment
#for (INDEX,CHUNK) in enumerate(ARRAY):                 #cycle forwards through the array elements <- commented out code
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
