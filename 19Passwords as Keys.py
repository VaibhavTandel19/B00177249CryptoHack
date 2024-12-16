#Passwords as Keys lab
# in this task we are using aes  the keys are generated by hashing each word from word.txt file using md5 to generate a key
# then decrypting it and confirming whether the results has crypto{}#


from Crypto.Cipher import AES
import hashlib
import random

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()

l = len(words)

for i in range(l):
    KEY = hashlib.md5(words[i].encode()).digest()
    decrypted = decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", KEY)
    if b'crypto' in decrypted:
        print(decrypted)