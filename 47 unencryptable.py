#we are decrypting  RSA-encrypted message by finding 2 prime number used in encryption
# and when we find the prime numbers we use them to find decryption key
# then we can reverse the encryption using the key#
!pip install gmpy2

from Crypto.Util.number import *
import gmpy2  

n = 0x7fe8cafec59886e9318830f33747cafd200588406e7c42741859e15994ab62410438991ab5d9fc94f386219e3c27d6ffc73754f791e7b2c565611f8fe5054dd132b8c4f3eadcf1180cd8f2a3cc756b06996f2d5b67c390adcba9d444697b13d12b2badfc3c7d5459df16a047ca25f4d18570cd6fa727aed46394576cfdb56b41
e = 0x10001
c = 0x5233da71cc1dc1c5f21039f51eb51c80657e1af217d563aa25a8104a4e84a42379040ecdfdd5afa191156ccb40b6f188f4ad96c58922428c4c0bc17fd5384456853e139afde40c3f95988879629297f48d0efa6b335716a4c24bfee36f714d34a4e810a9689e93a0af8502528844ae578100b0188a2790518c695c095c9d677b

DATA = bytes.fromhex("372f0e88f6f7189da7c06ed49e87e0664b988ecbee583586dfd1c6af99bf20345ae7442012c6807b3493d8936f5b48e553f614754deb3da6230fa1e16a8d5953a94c886699fc2bf409556264d5dced76a1780a90fd22f3701fdbcb183ddab4046affdc4dc6379090f79f4cd50673b24d0b08458cdbe509d60a4ad88a7b4e2921")
b = bytes_to_long(DATA)

assert (pow(b, e, n) == b)  

r = e - 1

def factor(_b, _r, _n):
    for i in range(2, 1000):
        if _r % i == 0:
            t = pow(_b, _r // i, _n)
            if gmpy2.gcd(t - 1, _n) != 1 and gmpy2.gcd(t - 1, _n) != _n:
                print("found p and q")
                p = gmpy2.gcd(t - 1, _n)
                q = _n // gmpy2.gcd(t - 1, _n)
                break
    return p, q

p, q = factor(b, e - 1, n)

tot = (p - 1) * (q - 1)

d = inverse(e, tot)

flag = long_to_bytes(pow(c, d, n)).decode()

print(flag)
