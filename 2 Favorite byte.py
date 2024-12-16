#This is crypto hack Favourite byte lab 
# in this lab we are trying to decode the hex srting provided in the question
# We are doing XOR of string with every byte from 0 to 255 
# then we specify in line 13 that if the key is started with word crypto then print or try another byte


import binascii

str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded = binascii.unhexlify(str)
for xorkey in range(256):
    decoded = ''.join(chr(b^xorkey) for b in encoded)
    if decoded.startswith("crypto"):
        print (xorkey, decoded)