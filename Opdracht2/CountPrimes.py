import sys
import math

bestand = str(sys.argv[1])
priem = []
tweeling = 0
file = open(bestand, 'r')


for line in file:
    getal = int(line.strip())
    priem.append(getal)

l = len(priem)
biggest = priem[l - 1]

N = int(priem[l-1])

nlogn = biggest / (math.log(biggest))
s1 = l * math.log(biggest) / biggest
c2 = 0.6601618
index = range(0, l -1)

for i in index:
    if priem[i+1] - priem[i] == 2:
        tweeling += 1

print("Largest Prime =", biggest)
print("--------------------")
print("pi(N) =", l)
a = float( N / math.log(N) )
print("N/log(N) =", a)
print("ratio =", (l / a) )
print("--------------------")
print("pi_2(N) =", tweeling)
c2 = 0.6601618
b = (2 * c2 * N) / (math.log(N) ** 2)
print("2CN/log(N)^2 =", b)
print("ratio =", (tweeling / b) )

