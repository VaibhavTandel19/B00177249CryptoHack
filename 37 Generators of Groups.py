#in this if no smaller power of k mod p =k then k = genarator
# here we used a function generator which loop iterates through possible values of k
# then we find the first generator of p so we can get value of k #


def is_generator(k, p):
  for n in range(2, p):
    if pow(k, n, p) == k:
      return False
  return True

p = 28151
for k in range(p):
  if is_generator(k, p):
    print(k)
    break