result =0;

for x in range(0, 1000):
    if (x % 3 == 0):
        result = result + x

    if (x%5 == 0):
        result = result + x

    if(x%15 == 0):
        result = result - x

print(result)
