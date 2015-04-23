def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_count = 0
a = fib(fib_count)
sum = 0
while a < 4000000:
    if (a%2==0):
        sum = sum + a
    fib_count = fib_count + 1
    a = fib(fib_count)

print(sum)
print(fib_count)
