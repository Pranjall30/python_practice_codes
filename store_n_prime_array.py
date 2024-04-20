

def store_first_n_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return primes

print(store_first_n_primes(10))