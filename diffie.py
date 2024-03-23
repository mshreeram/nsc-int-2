p = 353
g = 3

priv_key_a = 97
priv_key_b = 233

pub_key_a = pow(g, priv_key_a, p)
pub_key_b = pow(g, priv_key_b, p)

shared_key_a = pow(pub_key_b, priv_key_a, p)
shared_key_b = pow(pub_key_a, priv_key_b, p)

print("Secret key at A(ka): ", str(shared_key_a))
print("Secret key at B(kb)= ", str(shared_key_b))