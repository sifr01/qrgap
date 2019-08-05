import qrcode
import Image
import os

FILE_LOCATION = raw_input("Specify directory of text file (eg. /tmp/key.asc): ")
FILE_LOCATION = torproject.asc
FILE = open(FILE_LOCATION,"r")
print("Name of the file: ", FILE.name)

qr = 1
COUNT = 100
img = 1
a = 0

while True:
    COUNT -= 1
    TEXT = FILE.read(2000)
    if TEXT == '': 
        break
    if COUNT == 0:
        break
    print(TEXT)
    qr = qrcode.QRCode(
        version = None,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 4,
        border = 4,
        )
    qr.add_data(TEXT)
    qr.make(fit=True)            #
    a + img[qr.make_image()]            #
#    img[a].show()                #shows the made image file





#x=10
#while(x>0):
#    print(x)
#    x -=1
#else:
#    print("count value reached %d" %(x))

