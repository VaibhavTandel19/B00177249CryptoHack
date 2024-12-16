# #This is cryptohack Modular Inverting lab
# We used Fermat's Little Theorem which is A^P-1 mod P is always 1 if P is prime number and A is not divisible by P
# 3^13-1  (mod13)
p = 29
ints = [14,6,11]
print [(i,j) for i in ints for j in range(29) if (j**2)%29 == i]