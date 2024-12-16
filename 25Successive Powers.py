#we are already given that successive power of x modulo a three-digit prime p
# we will take different value of p  for x1 mod p = 588,665... 
# check for the value in which we get x value constant 



from Crypto.Util.number import inverse
import gmpy2

t = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

pval = max(t) + 1  

for p in range(pval, 1000000):  
    try:
        x = [(t[i] * inverse(t[i-1], p)) % p for i in range(1, len(t))]
        if len(set(x)) == 1:
            print("Found p:", p)
            print("x:", x)
            break  
    except Exception as e:
        print(f"Error for p={p}: {e}")
        pass
