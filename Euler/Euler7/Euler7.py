import math
import time

tests = int(input())
N = [int(input()) for i in range(tests)]

start = time.time()

def func(num):
    p = 3
    primes = [2]
    while len(primes) < num:
        prime = True
        for i in range(2, int(math.sqrt(p) + 1)):
            if p % i == 0: 
                prime = False
                break 
        if prime: 
            primes.append(p)
        p += 1
    return primes[-1]

for num in N:
    print(func(num))

end = time.time()
print(end - start)
