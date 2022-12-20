import numpy as np

N = 50000

ns = np.array(range(2,N))
primes = []
last_prime=2
while last_prime:
    primes.append(last_prime)
    ns = ns[ns%last_prime != 0]
    last_prime = ns[0] if len(ns) > 0 else None
print(primes[:500])
