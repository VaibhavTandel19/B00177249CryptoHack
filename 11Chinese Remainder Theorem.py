# Chinese Remainder Theorem lab
#over here we first find M which is multiple of all pi and then we use Chinese Remainder Theorem(x = ai mod pi)  #


a = [2,3,5]
p = [5,11,17]
x = 0

M = int(np.prod(p))

for i in range(len(a)):
    bi = M // p[i]
    x += (a[i] * bi * pow(bi,p[i]-2,p[i])) % M

print(x%M)