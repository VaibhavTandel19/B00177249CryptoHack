#This is cryptohack Extended GCD lab
## In this lab we used Euclidean algorithm again
# In this code we added  [gcd_val, x1, y1 = extendedgcd(q % p, p)] line so we can find coeffiecient 


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a % b)

def extendedgcd(p, q):
    if p == 0:
        return q, 0, 1
    gcd_val, x1, y1 = extendedgcd(q % p, p)     
    x = y1 - (q // p) * x1  
    y = x1
    return gcd_val, x, y


gcd_val, x, y = extendedgcd(26513, 32321)
print("GCD=", gcd_val)
print("x=", x)
print("y=", y)
