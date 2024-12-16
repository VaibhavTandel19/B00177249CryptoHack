# This is cryptohack (You either know, XOR you don't) lab
#In this lab we used our encrypted string and XOR it with crypto{ as this is mandatory in every answer 
# so we got yXORkey as a new key and again we did the XOR with the existing string 


def xor_bytes(data, key):

    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])


flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
key1 = 'myXORkey'.encode()
print(xor_bytes(flag, key1))