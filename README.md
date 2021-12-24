qrgap
=====
Transfer text between devices which are air-gapped (eg. a 4096 byte key from computer to smartphone). This code can be used alongside the QRStream app, available in F-Droid. One version of the script displays the qrstream backwards so that the qrcode windows can be viewed, scanned and then closed in the correct order. 

Dependencies
============
```sudo python3-pip
pip3 install qrcode```

Example:
========
```python3 qrgap_1.6.py textfile.txt
python3 qrgap_backwards_1.4.py textfile.txt```

Standard qrgap.py script
========================
When executed, the standard qrgap script opens as many windows as is needed to display the text file in successive qr codes. However, with the last qr code representing the end of the text file, when it comes to scanning this back in, it proves inconvenient. Therefore I have created the next script:

qrgap_backwards.py
==================
This opens the qrcode windows in reverse order so that when it comes to scanning the codes back in, the first block of data can be scanned first, and so on..
