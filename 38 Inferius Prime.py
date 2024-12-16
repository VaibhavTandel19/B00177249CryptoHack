#we are private key using modular inverse of the public exponent
# then decrypts the cipher text by raising the power of d modulo n
# then it converts decrpted  number back to string form to get flag #
# 

from Crypto.Util.number import inverse, long_to_bytes


p = 752708788837165590355094155871
q = 986369682585281993933185289261
n = p * q
phi = (p - 1) * (q - 1)
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


d = inverse(e, phi)


pt = pow(ct, d, n)  
decrypted = long_to_bytes(pt)  

print(decrypted.decode())

