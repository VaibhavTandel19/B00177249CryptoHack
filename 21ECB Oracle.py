#we are decrypting a encryptedflag using AES in CBC using XOR 
# then in [decrypt_block2 = xor(response(block2), block1)] we are spliting it in blocks and then again using XOR to get the flag #


import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def response(byte_string):
	url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
	url += byte_string.hex()
	url += "/"
	r = requests.get(url)
	js = r.json()
	return bytes.fromhex(js["plaintext"])

def encrypt_flag():
	url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
	r = requests.get(url)
	js = r.json()
	return bytes.fromhex(js["ciphertext"])

def xor(a, b):
	return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

enc = encrypt_flag()

iv = enc[:16]
block1 = enc[16:32]
block2 = enc[32:]

decrypt_block1 = xor(response(block1), iv)
decrypt_block2 = xor(response(block2), block1)
print(decrypt_block1 + decrypt_block2)