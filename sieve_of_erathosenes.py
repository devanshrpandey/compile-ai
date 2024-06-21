def sieve_of_eratosthenes_python(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(n+1) if primes[i]]

# Usage
import time

n = 389_238_191
start = time.process_time()
primes = sieve_of_eratosthenes_python(n)
end = time.process_time()
print(f"CPU time: {end - start:.4f} seconds")
num_primes = len(primes)
print(f"Found {num_primes} primes. Last prime is {primes[-1]}")