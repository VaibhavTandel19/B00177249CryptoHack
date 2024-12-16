#This is cryptohack GCD lab
# In this lab we used Euclidean algorithm
# example of Euclidean algorithm if 30/12 =2 and remainder is 6 and 12/ 6 = 2 then gcd is 6#

def gcd(a, b):
    while b:
        a, b = b, a % b  #Euclidean algorithm
    return a


a = 66528
b = 52920
print(gcd(a, b))
