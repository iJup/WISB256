import sys
import time 
priem_lijst = []

def Zeef(n):
    n = n+1
    primes = dict()
    for i in range(2, n): primes[i] = True

    for i in primes:
        factors = range(i,n, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

N = int(sys.argv[1])
File = str(sys.argv[2])

T1 = time.perf_counter()
priem_lijst = Zeef(N)

f = open(File, 'w')
for priem in priem_lijst:
    f.write(str(priem) + '\n')
    
T2 = time.perf_counter()

print("Found", len(priem_lijst), "Prime numbers smaller than", N, "in", T2 - T1, "sec.")
