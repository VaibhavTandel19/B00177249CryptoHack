#we are  using Diffie-Hellman key exchange to get a shared secret key
# then we will decrypt the encrypted flag using AES
# then we will use cryptographic function like AES and SHA-1 to connect secure communication and decrypt the flag#


from Crypto.Util.number import *
import json
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy.ntheory.residue_ntheory import discrete_log
import socket  


def json_recv(sock):
    """Receives JSON data from the socket."""
    data = b''
    while not data.endswith(b'\n'):
        data += sock.recv(1)
    return json.loads(data.decode())


def json_send(sock, hsh):
    """Sends JSON data to the socket."""
    request = json.dumps(hsh).encode()
    sock.sendall(request + b'\n')


def smooth_p(p):
    mul = 1
    i = 1
    while True:
        mul *= i
        if (mul + 1).bit_length() >= p.bit_length() and isPrime(mul + 1):
            return mul + 1
        i += 1


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret, iv, ciphertext):
  
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('socket.cryptohack.org', 13378))

    sock.recv(1024)  

   
    res = json_recv(sock)
    p = int(res["p"], 16)
    g = int(res["g"], 16)
    A = int(res["A"], 16)

    sock.recv(1024)  

 
    res = json_recv(sock)
    B = int(res["B"], 16)

    sock.recv(1024) 

 
    res = json_recv(sock)
    iv = res["iv"]
    ciphertext = res["encrypted"]

    
    s_p = smooth_p(p)
    print(f"Smooth p bit length: {s_p.bit_length()}")

    sock.recv(1024)  


    json_send(sock, {
        "p": hex(s_p),
        "g": hex(2),
        "A": hex(A)
    })

    sock.recv(1024)  


    res = json_recv(sock)
    B = int(res["B"], 16)
    b = discrete_log(s_p, B, 2)

    shared_secret = pow(A, b, p)

   
    flag = decrypt_flag(shared_secret, iv, ciphertext)
    print(f"Decrypted flag: {flag}")

    sock.close()

if __name__ == "__main__":
    main()
