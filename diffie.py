p = 353
g = 3

A = int(pow(g, a, p))
B = int(pow(g, b, p))

ka = int(pow(B, a, p))
kb = int(pow(A, b, p))

print("Secret key at A(ka): ", str(ka))
print("Secret key at B(kb)= ", str(kb))