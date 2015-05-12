import random
import sys
import math

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Use: python Pi.py N L")
    sys.exit()
if len(sys.argv) == 4:
    random.seed(int(sys.argv[3]))    

N = int(sys.argv[1])
L = float(sys.argv[2])
if L > 1:
    print("AssertionError: L should be smaller than 1")
    sys.exit()

def drop_needle(L):
    x       = random.random()
    theta   = random.vonmisesvariate(0,0)

    end_x   = x + L * math.cos(theta)

    if end_x > 1 or end_x < 0:
        return True
    else:
        return False


hits = 0
for turn in range(N):
    hits += drop_needle(L)


print(hits, "hits", "in", N, "tries") 
pi = 2 * L / (int(hits) / N)
print("Pi =",pi)
